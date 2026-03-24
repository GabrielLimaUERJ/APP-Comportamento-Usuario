# =========================================
# IMPORTAÇÃO
# =========================================
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

# =========================================
# parâmetros
# =========================================

num_users = 5000
start_date = datetime(2025, 1, 1)
days = 60

origens = ["google", "instagram", "facebook", "direto"]
devices = ["mobile", "desktop"]

eventos = []
event_id = 1

for user_id in range(1, num_users + 1):
    
    # número de visitas do usuário
    visitas = np.random.poisson(2) + 1
    
    for _ in range(visitas):
        
        data = start_date + timedelta(days=random.randint(0, days))
        origem = random.choice(origens)
        device = random.choice(devices)
        
        # VISITA
        eventos.append([
            event_id, user_id, data, "visita", origem, device
        ])
        event_id += 1
        
        # probabilidade de clique
        if random.random() < 0.4:
            eventos.append([
                event_id, user_id, data, "clique", origem, device
            ])
            event_id += 1
            
            # probabilidade de compra
            if random.random() < 0.25:
                eventos.append([
                    event_id, user_id, data, "compra", origem, device
                ])
                event_id += 1

df = pd.DataFrame(eventos, columns=[
    "event_id",
    "user_id",
    "data_evento",
    "etapa",
    "origem_trafego",
    "device"
])

df.to_csv("eventos_site.csv", index=False)

print("Dataset gerado:", df.shape)