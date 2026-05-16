import os
import shutil

class ShadowErase:
    def __init__(self, chronicler):
        self.chronicler = chronicler
        self.target_paths = [
            "system_core/system_log.txt",
            ".kernel_state",
            "docs/invoices/",
            "*.log",
            "__pycache__/"
        ]

    def execute_destruction(self, secret_key):
        if secret_key == "NEXUM-SIGMA-99":
            print("🚨 [EMERGENCY]: تم تفعيل بروتوكول المحو الظلي! جاري سحق البيانات...")
            for path in self.target_paths:
                try:
                    if "*" in path:
                        os.system(f"rm -rf {path}")
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                    elif os.path.isfile(path):
                        os.remove(path)
                    print(f"🧹 [Wipe]: تم تطهير {path}")
                except Exception as e:
                    pass
            return True
        return False
