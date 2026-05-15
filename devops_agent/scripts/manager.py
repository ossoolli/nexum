import git
import docker

def check_repo_status(path):
    repo = git.Repo(path)
    return repo.is_dirty()

def check_containers():
    client = docker.from_env()
    return {c.name: c.status for c in client.containers.list()}

if __name__ == '__main__':
    print(f'Repo Status: Dirty={check_repo_status(".")}')
    print(f'Containers: {check_containers()}')
