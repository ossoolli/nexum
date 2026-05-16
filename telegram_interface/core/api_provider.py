import json
import pandas as pd

def get_system_data():
    audit = pd.read_csv('shared_memory/audit_log.csv').to_dict(orient='records')
    with open('shared_memory/intelligence.json', 'r') as f:
        intel = json.load(f)
    return {'audit': audit, 'intelligence': intel}
