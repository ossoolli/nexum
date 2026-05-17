import datetime

class NexumContextAgent:
    def __init__(self):
        self.version = "v0.7.1"
        self.files_map = {
            "main.py": "Command center via Telegram",
            "pulse.go": "High-speed market stream",
            "kernel.py": "System orchestration"
        }

    def explain_status(self):
        """وظيفة وكيل الشرح: كتابة تقرير فني لحظي"""
        report = f"--- NEXUM STATUS REPORT [{datetime.datetime.now()}] ---\n"
        for file, role in self.files_map.items():
            report += f"- {file}: {role} | STATUS: Active\n"
        
        with open("SYSTEM_CONTEXT.log", "w") as f:
            f.write(report)
        print("✅ [Context Agent]: System explanation updated.")

if __name__ == "__main__":
    NexumContextAgent().explain_status()
