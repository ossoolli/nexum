import json
import os

def get_wealth_stats():
    # محاكاة قراءة سجلات المعماري لاستخراج بيانات العملة
    log_path = '/home/madarmutaz/AI-Agents/system_core/logs/architect.log'
    print(f'--- 📊 Nexum Wealth Dashboard ---')
    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            logs = f.readlines()
            minted = sum(1 for line in logs if 'Minting' in line) * 500
            burned = sum(1 for line in logs if 'Burn' in line) * 125
            print(f'Total Minted: {minted} NST')
            print(f'Total Burned: {burned} NST')
            print(f'Net Supply: {minted - burned} NST')
    else:
        print('Logs not found. Waiting for first pulse...')

if __name__ == '__main__':
    get_wealth_stats()
