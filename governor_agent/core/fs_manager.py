import os
import shutil
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class WorkspaceGovernor(FileSystemEventHandler):
    ROUTING_RULES = {'.pdf': 'shared_memory/docs', '.docx': 'shared_memory/docs', '.py': 'shared_memory/scripts'}
    def __init__(self, base_path):
        self.base_path = base_path
        self.governor_dir = os.path.join(base_path, 'governor_agent')
        self.log_file = os.path.join(self.governor_dir, 'logs', 'system.log')

    def log_action(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as f: f.write(f"[{timestamp}] {message}\n")

    def on_created(self, event):
        if not event.is_directory:
            ext = os.path.splitext(event.src_path)[1]
            if ext in self.ROUTING_RULES:
                dest_dir = os.path.join(self.base_path, self.ROUTING_RULES[ext])
                shutil.move(event.src_path, os.path.join(dest_dir, os.path.basename(event.src_path)))
                self.log_action(f"🚀 Routed {os.path.basename(event.src_path)} to {dest_dir}")

if __name__ == '__main__':
    target_path = "os.path.dirname(os.path.abspath(__file__))"
    observer = Observer()
    observer.schedule(WorkspaceGovernor(target_path), target_path, recursive=False)
    observer.start()
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt: observer.stop()
    observer.join()
