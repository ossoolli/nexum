import re
import ast
import json

def force_repair_json(raw_data):
    try:
        # 1. Regex extraction
        matches = re.findall(r'\{.*\}', raw_data, re.DOTALL)
        if matches:
            raw_data = matches[0]
        
        # 2. Attempt standard load
        return json.loads(raw_data)
    except:
        try:
            # 3. Attempt ast.literal_eval
            return ast.literal_eval(raw_data)
        except:
            # 4. Attempt closing brackets
            fixed_data = raw_data + '}' * (raw_data.count('{') - raw_data.count('}'))
            result = json.loads(fixed_data)
            with open('shared_memory/audit_log.csv', 'a') as f:
                f.write('JSON Forcefully Repaired\n')
            return result
