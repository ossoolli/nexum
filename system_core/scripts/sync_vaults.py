import json
import os
try:
    from nexum_kernel import NexumKernel
    kernel = NexumKernel()
    data = kernel.treasuries
except ImportError:
    data = {
        "BITCOIN": "bc1p0uuqerrwsqawe0cd74hetayxte0rdrnn9nd9n5h94se2fv7knw2qt4t7v9",
        "TON": "UQAVBa3YSDb-ExTzMVAEq6MfgKNyDbCt3FqLKhRekGMgHqlr",
        "SOLANA": "GuWPwyXQKXQ5ntMBLHCXqNnhvumdrMnGxAZ4xm2Jiyzf",
        "ETH_USDT": "0xd9805c529d944ead2742Ebdbd6DC8Ad005A1E78",
        "TRON_USDT": "TW94CS14t8EtswVoQWy4wMoUEZDdtnxcPz"
    }

os.makedirs('./reports/sovereign', exist_ok=True)
with open('./reports/sovereign/treasury_report.json', 'w') as f:
    json.dump(data, f, indent=4)

print("✅ [Success]: Treasury report generated at ./reports/sovereign/treasury_report.json")
