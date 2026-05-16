import os, pandas as pd, json
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self, client): self.client = client
    def execute_sql(self, query): return self.client.rpc('execute_sql', {'query': query}).execute()

class DataArchitect:
    def __init__(self):
        self.env = os.getenv('APP_ENV', 'development')
        self.db = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))
    
    def intelligent_analysis(self, data):
        df = pd.DataFrame(data)
        return df.describe()

    def update_shared_knowledge(self, insights):
        with open('/app/shared_memory/intelligence.json', 'w') as f:
            json.dump(insights, f)

if __name__ == '__main__':
    architect = DataArchitect()
    print(f'Agent running in {architect.env} mode')

def initialize_risk_table():
    sql = """
    CREATE TABLE IF NOT EXISTS ossoolli_risk_index (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        risk_type TEXT,
        risk_level INTEGER,
        raw_source TEXT,
        analysis_summary JSONB,
        created_at TIMESTAMPTZ DEFAULT NOW()
    );
    """
    try:
        architect = DataArchitect()
        db_manager = DatabaseManager(architect.db)
        db_manager.execute_sql(sql)
        architect.update_shared_knowledge({'risk_database_status': 'ready', 'table': 'ossoolli_risk_index'})
        print("Success: Risk table is live and knowledge updated.")
    except Exception as e:
        print(f"Error initializing table: {e}")
