import subprocess

def execute_infra_cmd(category):
    commands = {
        'git': 'git pull',
        'docker': 'docker system prune -f',
        'restart': 'systemctl restart aegant-ai'
    }
    cmd = commands.get(category)
    if cmd:
        return subprocess.check_output(cmd, shell=True).decode()
    return 'Invalid Category'
