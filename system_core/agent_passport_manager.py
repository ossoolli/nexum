import json

def save_passport(passport):
    with open(f"passports/{passport['identity']['did']}.json", 'w') as f:
        json.dump(passport, f, indent=4)

def initialize_agent_passport(agent_id, capabilities):
    passport = {
        "identity": {"did": f"did:nexum:{agent_id}", "status": "active"},
        "capabilities": capabilities,
        "economics": {"stake": 1000, "reputation": 50.0, "trust_score": 1.0},
        "limits": {"gas_quota": 500, "max_intent_value": 5000}
    }
    save_passport(passport)
    print(f"🏛️ [Maestro]: تم إصدار جواز سفر NAPS للوكيل {agent_id}")
