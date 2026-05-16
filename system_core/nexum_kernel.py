import json
import os
import datetime
import requests

class NexumKernel:
    def __init__(self):
        self.version = "v0.4.0-Beta"
        self.master_key = "NEXUM-SIGMA-99"
        self.vaults = {
            "BTC": {"addr": "bc1p0uuqerrwsqawe0cd74hetayxte0rdrnn9nd9n5h94se2fv7knw2qt4t7v9", "symbol": "bitcoin"},
            "TON": {"addr": "UQAVBa3YSDb-ExTzMVAEq6MfgKNyDbCt3FqLKhRekGMgHqlr", "symbol": "the-open-network"},
            "SOL": {"addr": "GuWPwyXQKXQ5ntMBLHCXqNnhvumdrMnGxAZ4xm2Jiyzf", "symbol": "solana"},
            "ETH": {"addr": "0xd9805c529d944ead2742Ebdbd6DC8Ad005A1E78", "symbol": "ethereum"},
            "TRX": {"addr": "TW94CS14t8EtswVoQWy4wMoUEZDdtnxcPz", "symbol": "tron"}
        }

    def get_market_data(self):
        try:
            ids = ",".join([v['symbol'] for v in self.vaults.values()])
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
            response = requests.get(url, timeout=5)
            return response.json()
        except:
            return {}

    def sync_dashboard(self):
        market = self.get_market_data()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html_content = f"""
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <title>NEXUM | Terminal v0.4.0</title>
            <style>
                :root {{ --gold: #d4af37; --bg: #050505; --card: #0f0f0f; --green: #00ff88; }}
                body {{ background-color: var(--bg); color: #fff; font-family: 'JetBrains Mono', monospace; margin: 0; padding: 20px; }}
                .terminal {{ max-width: 900px; margin: auto; border: 1px solid #222; border-radius: 8px; overflow: hidden; }}
                .header {{ background: #111; padding: 15px; border-bottom: 1px solid #222; display: flex; justify-content: space-between; align-items: center; }}
                .brand {{ color: var(--gold); font-size: 1.2rem; font-weight: bold; letter-spacing: 4px; }}
                .status-tag {{ font-size: 0.7rem; color: var(--green); border: 1px solid var(--green); padding: 2px 8px; border-radius: 4px; }}
                .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1px; background: #222; }}
                .asset-card {{ background: var(--card); padding: 20px; }}
                .asset-name {{ color: #888; font-size: 0.7rem; text-transform: uppercase; }}
                .asset-price {{ font-size: 1.5rem; margin: 10px 0; color: var(--gold); }}
                .asset-addr {{ font-size: 0.6rem; color: #444; word-break: break-all; }}
                .footer {{ padding: 15px; font-size: 0.6rem; color: #444; text-align: center; background: #0a0a0a; }}
            </style>
        </head>
        <body>
            <div class="terminal">
                <div class="header">
                    <div class="brand">NEXUM TERMINAL</div>
                    <div class="status-tag">CORE {self.version} :: ONLINE</div>
                </div>
                <div class="grid">
        """
        for ticker, data in self.vaults.items():
            price = market.get(data['symbol'], {}).get('usd', 'N/A')
            html_content += f"""
                    <div class="asset-card">
                        <div class="asset-name">{ticker} / USD</div>
                        <div class="asset-price">${price}</div>
                        <div class="asset-addr">{data['addr']}</div>
                    </div>"""
        html_content += f"""</div><div class="footer">SYNC: {timestamp} | NEXUM KERNEL {self.version}</div></div></body></html>"""
        with open("../index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        return True

if __name__ == "__main__":
    k = NexumKernel()
    k.sync_dashboard()
