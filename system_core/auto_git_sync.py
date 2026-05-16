import subprocess
import time

def sync_to_github():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Sovereign Update: {time.ctime()}"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🚀 [Nexum-Sync]: تم رفع التحديثات الجديدة إلى GitHub بنجاح.")
    except Exception as e:
        print(f"⚠️ [Sync-Error]: فشل التزامن. السبب: {e}")

if __name__ == '__main__':
    sync_to_github()
