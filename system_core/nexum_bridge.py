import json
import os
import tempfile
import shutil

BLUEPRINT_PATH = "/home/madarmutaz/AI-Agents/blockchain_node/network_core/blueprints/"

def safe_request_build(agent_name, target_type, design_name, logic_details):
    blueprint = {
        "requester": str(agent_name),
        "target_type": str(target_type),
        "design_name": str(design_name),
        "logic_payload": logic_details
    }

    os.makedirs(BLUEPRINT_PATH, exist_ok=True)
    
    with tempfile.NamedTemporaryFile('w', delete=False, dir=BLUEPRINT_PATH, suffix='.tmp') as tf:
        json.dump(blueprint, tf, ensure_ascii=False, indent=4)
        temp_name = tf.name

    final_path = os.path.join(BLUEPRINT_PATH, f"REQ_{design_name}.json")
    shutil.move(temp_name, final_path)
    
    print(f"✨ [Nexum-Bridge]: تم تأمين ونشر المخطط: {design_name}")
