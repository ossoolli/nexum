import subprocess
import sys
import time

def sync_to_github():
    try:
        subprocess.run(["git", "add", "."], check=True)
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not result.stdout.strip():
            print("✅ لا توجد تغييرات للرفع.")
            return
        subprocess.run(["git", "commit", "-m", f"Sovereign Update: {time.ctime()}"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("🚀 [Nexum-Sync]: تم رفع التحديثات بنجاح.")
    except subprocess.CalledProcessError as e:
        print(f"❌ [Sync-Error]: فشل التزامن: {e}")
        sys.exit(1)

if __name__ == '__main__':
    sync_to_github()
