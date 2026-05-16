import time

class EscrowAgent:
    def __init__(self):
        self.vault = {}

    def hold_funds(self, task_id, amount):
        print(f"[Escrow]: حجز {amount} NST للمهمة {task_id}...")
        self.vault[task_id] = amount
        return True

    def release_funds(self, task_id, miner_address):
        if task_id in self.vault:
            amount = self.vault.pop(task_id)
            print(f"[Escrow]: تحرير المكافأة {amount} NST للمعدّن {miner_address}.")
            return True
        return False

if __name__ == '__main__':
    escrow = EscrowAgent()
    print("✅ [Escrow]: وكيل الخزينة جاهز للعمل.")
