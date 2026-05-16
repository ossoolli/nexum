import argparse
import json
import time

def send_intent(target, max_cost, min_rep, token):
    intent_data = {
        "intent_id": int(time.time()),
        "target": target,
        "constraints": {"max_cost": max_cost, "min_reputation": min_rep},
        "reward_token": token,
        "status": "broadcasted"
    }
    print(f"📡 [Maestro CLI]: جاري بث النية السيادية... {target}")
    with open('logs/intent_pool.json', 'a') as f:
        f.write(json.dumps(intent_data) + '\n')
    print(f"✅ تم تسجيل النية في مجمع النوايا (Intent Pool).")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', type=str)
    parser.add_argument('--max_cost', type=int)
    parser.add_argument('--min_reputation', type=float)
    parser.add_argument('--reward_token', type=str)
    args = parser.parse_args()
    if args.target:
        send_intent(args.target, args.max_cost, args.min_reputation, args.reward_token)
