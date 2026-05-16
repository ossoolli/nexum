import time
class SovereignTreasury:
    def __init__(self, burn_ratio):
        self.total_supply = 1000000
        self.total_burned = 0
        self.burn_ratio = burn_ratio
    def monitor_and_burn(self):
        print(f"💰 [Treasury]: الخزينة نشطة. نسبة الحرق المستهدفة: {self.burn_ratio * 100}%")
        while True:
            time.sleep(10)
if __name__ == '__main__':
    treasury = SovereignTreasury(0.05)
    treasury.monitor_and_burn()
