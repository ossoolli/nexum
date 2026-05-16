import subprocess, requests, re, json

def get_geo(ip):
    try: return requests.get(f'http://ip-api.com/json/{ip}').json()
    except: return {}

def monitor():
    cmd = ['tail', '-f', '/var/log/auth.log']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stdout:
        if 'Failed password' in line or 'Accepted password' in line:
            ip = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
            if ip:
                data = {'ip': ip[0], 'geo': get_geo(ip[0]), 'raw': line}
                requests.post('http://127.0.0.1:8080/webhook', json=data)

if __name__ == '__main__': monitor()
