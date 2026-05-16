import os
import sqlite3
import subprocess
from datetime import datetime

G, R, Y, C = "\033[92m", "\033[91m", "\033[93m", "\033[0m"

def check_process(keyword, port=None):
    if port:
        check = subprocess.run(f"netstat -tuln | grep :{port}", shell=True, capture_output=True, text=True)
    else:
        check = subprocess.run(f"ps aux | grep {keyword} | grep -v grep", shell=True, capture_output=True, text=True)
    return f"{G}🟢 ACTIVE{C}" if check.stdout else f"{R}🔴 OFFLINE{C}"

def get_db_stats():
    try:
        db_path = os.path.join(os.getcwd(), 'database_layer/shared_memory.db')
        if not os.path.exists(db_path): return f"{R}No DB{C}"
        conn = sqlite3.connect(db_path)
        count = conn.execute('SELECT COUNT(*) FROM proposals').fetchone()[0]
        conn.close()
        return f"{Y}{count}{C}"
    except Exception as e:
        return f"{R}Err{C}"

os.system('clear')
print(f"""
{Y}🏛️  AEGANT-AI | SOVEREIGN COMMAND CENTER{C}
{'-'*40}
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Amman, Jordan (GMT+3)

📡 {G}Flow-Master (8080):{C}      {check_process('automation_engine', 8080)}
🛡️ {G}Security Monitor:{C}       {check_process('log_watcher')}
🧠 {G}Shared Memory (SQL):{C}    {get_db_stats()} Proposals
📂 {G}Execution Path:{C}         {os.getcwd()}
{'-'*40}
{Y}STATUS:{C} Visuals Restored via Relative Paths.
""")
