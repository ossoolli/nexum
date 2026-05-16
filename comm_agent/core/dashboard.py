import time, csv, os, json

def get_savings():
    count = 0
    if os.path.exists('shared_memory/audit_log.csv'):
        with open('shared_memory/audit_log.csv', 'r') as f:
            count = sum(1 for row in f if 'Rejected' in row)
    return count

def display_ui():
    os.system('clear')
    print('=== Aegant-AI Commander Center ===')
    print(f'Savings Counter: {get_savings()} OpenAI calls prevented.')
    print(f'Status: Active | Mode: Monitoring | Refresh: 10s')
    print('----------------------------------')
    # Placeholder for resource monitoring
    print('Agents: Governor [OK], Tech-Master [OK], Architect [OK]')
    print('----------------------------------')

def get_command():
    cmd = input('Commander Input (FIX ALL / GATHER INTEL / exit): ')
    if cmd in ['FIX ALL', 'GATHER INTEL']:
        with open('shared_memory/decision_bus.json', 'w') as f:
            json.dump({'command': cmd, 'timestamp': time.time()}, f)
    return cmd

if __name__ == '__main__':
    while True:
        display_ui()
        cmd = get_command()
        if cmd == 'exit': break
        time.sleep(10)
