# =========================================
# IMPORTAÇÃO
# =========================================
import duckdb

# =========================================
# CONEXÃO (SALVA O BANCO)
# =========================================
con = duckdb.connect("analytics.duckdb")

# =========================================
# CARREGAR CSV
# =========================================
con.execute("""
CREATE OR REPLACE TABLE eventos AS 
SELECT * FROM read_csv_auto('eventos_site.csv')
""")

# =========================================
# DEBUG (VER COLUNAS)
# =========================================
print("\nColunas da tabela:")
print(con.execute("DESCRIBE eventos").fetchdf())

# =========================================
# FUNIL
# =========================================
print("\nFunil:")
funil = con.execute("""
SELECT 
  etapa,
  COUNT(DISTINCT user_id) AS usuarios
FROM eventos
GROUP BY etapa
ORDER BY 
  CASE 
    WHEN etapa = 'visita' THEN 1
    WHEN etapa = 'clique' THEN 2
    WHEN etapa = 'compra' THEN 3
  END
""").fetchdf()

print(funil)

# =========================================
# CONVERSÃO
# =========================================
print("\nConversão:")

conversao = con.execute("""
SELECT 
  COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END) AS visitas,
  COUNT(DISTINCT CASE WHEN etapa = 'clique' THEN user_id END) AS cliques,
  COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) AS compras,

  ROUND(
    COUNT(DISTINCT CASE WHEN etapa = 'clique' THEN user_id END) * 1.0 /
    COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END), 4
  ) AS taxa_clique,

  ROUND(
    COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) * 1.0 /
    COUNT(DISTINCT CASE WHEN etapa = 'clique' THEN user_id END), 4
  ) AS taxa_compra,

  ROUND(
    COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) * 1.0 /
    COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END), 4
  ) AS taxa_total

FROM eventos
""").fetchdf()

print(conversao)

# =========================================
# CONVERSÃO POR ORIGEM
# =========================================
print("\nConversão por origem:")

origem = con.execute("""
SELECT 
  origem_trafego,
  COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END) AS visitas,
  COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) AS compras,

  ROUND(
    COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) * 1.0 /
    COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END),
    4
  ) AS taxa_conversao

FROM eventos
GROUP BY origem_trafego
ORDER BY taxa_conversao DESC
""").fetchdf()

print(origem)

# =========================================
# CONVERSÃO POR DEVICE
# =========================================
print("\nConversão por device:")

device = con.execute("""
SELECT 
  device,
  COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END) AS visitas,
  COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) AS compras,

  ROUND(
    COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) * 1.0 /
    COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END),
    4
  ) AS taxa_conversao

FROM eventos
GROUP BY device
ORDER BY taxa_conversao DESC
""").fetchdf()

print(device)

# =========================================
# SALVAR TABELAS PARA LOOKER
# =========================================

# Funil
con.execute("""
CREATE OR REPLACE TABLE funil AS
SELECT 
  etapa,
  COUNT(DISTINCT user_id) AS usuarios
FROM eventos
GROUP BY etapa
""")

# Conversão geral
con.execute("""
CREATE OR REPLACE TABLE conversao AS
SELECT 
  COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END) AS visitas,
  COUNT(DISTINCT CASE WHEN etapa = 'clique' THEN user_id END) AS cliques,
  COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) AS compras
FROM eventos
""")

# Conversão por origem
con.execute("""
CREATE OR REPLACE TABLE conversao_origem AS
SELECT 
  origem_trafego,
  COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END) AS visitas,
  COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) AS compras
FROM eventos
GROUP BY origem_trafego
""")

# Conversão por device
con.execute("""
CREATE OR REPLACE TABLE conversao_device AS
SELECT 
  device,
  COUNT(DISTINCT CASE WHEN etapa = 'visita' THEN user_id END) AS visitas,
  COUNT(DISTINCT CASE WHEN etapa = 'compra' THEN user_id END) AS compras
FROM eventos
GROUP BY device
""")

print("\nTabelas criadas com sucesso no DuckDB!")

# =========================================
# EXPORTAÇÃO PARA CSV
# =========================================

con.execute("""
COPY funil TO 'funil.csv' (HEADER, DELIMITER ',')
""")

con.execute("""
COPY conversao_origem TO 'conversao_origem.csv' (HEADER, DELIMITER ',')
""")

con.execute("""
COPY conversao_device TO 'conversao_device.csv' (HEADER, DELIMITER ',')
""")

print("\nArquivos exportados com sucesso para o Looker!")