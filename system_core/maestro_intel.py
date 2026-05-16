import json
import os

def safe_generate_blueprint(target, name, logic):
    blueprint = {
        "target_type": str(target),
        "design_name": str(name),
        "logic_hash": str(logic)
    }
    
    path = "/home/madarmutaz/AI-Agents/blockchain_node/network_core/blueprints/"
    os.makedirs(path, exist_ok=True)
    
    file_name = f"order_{name}.json"
    full_path = os.path.join(path, file_name)
    
    with open(full_path, "w", encoding='utf-8') as f:
        json.dump(blueprint, f, indent=4, ensure_ascii=False)
    
    print(f"DATA_START")
    print(json.dumps({"status": "success", "file": file_name}))
    print(f"DATA_END")

if __name__ == "__main__":
    safe_generate_blueprint("SMART_CONTRACT", "ossoolli-Ownership-V1", "ISO31022_SIG")
