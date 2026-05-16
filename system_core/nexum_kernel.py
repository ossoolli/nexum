import json
import os
import datetime

class NexumKernel:
    def __init__(self):
        self.version = "v0.4.5-Pro"
        self.vaults = [
            {"name": "BITCOIN", "symbol": "BTC", "color": "#f7931a"},
            {"name": "SOLANA", "symbol": "SOL", "color": "#14f195"},
            {"name": "ETHEREUM", "symbol": "ETH", "color": "#627eea"}
        ]

    def build_pro_terminal(self):
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>NEXUM | Professional Terminal</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body {{ background: #050505; color: #fff; font-family: 'Inter', sans-serif; }}
                .glass-card {{ background: rgba(15, 15, 15, 0.7); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.05); }}
                .trading-grid {{ display: grid; grid-template-columns: 2fr 1fr; gap: 20px; }}
            </style>
        </head>
        <body class="p-6">
            <nav class="flex justify-between items-center mb-8 p-4 glass-card rounded-xl">
                <div class="text-2xl font-black tracking-tighter text-yellow-500">NEXUM <span class="text-white">PRO</span></div>
                <div class="text-xs text-gray-500 tracking-widest uppercase">System Status: <span class="text-green-500">Operational</span></div>
            </nav>
            <div class="max-w-7xl mx-auto">
                <div class="trading-grid">
                    <div class="glass-card p-6 rounded-2xl h-[450px]">
                        <div class="flex justify-between mb-4">
                            <h2 class="text-sm font-bold text-gray-400 uppercase">Market Intelligence</h2>
                            <span class="text-xs text-yellow-600">{self.version}</span>
                        </div>
                        <canvas id="marketChart"></canvas>
                    </div>
                    <div class="space-y-4">
        """
        for v in self.vaults:
            html += f"""
                        <div class="glass-card p-5 rounded-xl hover:border-yellow-500/30 transition-all">
                            <div class="flex justify-between items-center">
                                <span class="text-xs text-gray-500">{v['name']}</span>
                                <div class="w-2 h-2 rounded-full" style="background: {v['color']}"></div>
                            </div>
                            <div class="text-xl font-mono mt-2 tracking-tighter">$ --.---</div>
                        </div>
            """
        html += """
                    </div>
                </div>
            </div>
            <script>
                const ctx = document.getElementById('marketChart').getContext('2d');
                new Chart(ctx, { type: 'line', data: { labels: ['12:00', '13:00', '14:00', '15:00', '16:00', '17:00'], datasets: [{ label: 'NEXUM Index', data: [12, 19, 15, 25, 22, 30], borderColor: '#d4af37', tension: 0.4, fill: true, backgroundColor: 'rgba(212, 175, 55, 0.05)' }] }, options: { responsive: true, maintainAspectRatio: false } });
            </script>
        </body>
        </html>
        """
        with open("index.html", "w") as f: f.write(html)

if __name__ == "__main__":
    kernel = NexumKernel()
    kernel.build_pro_terminal()
