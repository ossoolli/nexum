def sovereign_preflight_check(agent_id, intent):
    passport = get_passport(agent_id)
    
    # 1. فحص الرهان (Stake Check)
    if passport['economics']['stake'] < intent['min_stake']:
        return "❌ فشل السيادة: الرهان غير كافٍ لتنفيذ هذه النية."
        
    # 2. فحص الصلاحية (Capability Check)
    if intent['type'] not in passport['capabilities']:
        return "❌ فشل السيادة: الوكيل غير مخول لهذه المهمة."
        
    # 3. فحص السمعة (Reputation Gate)
    if passport['economics']['trust_score'] < 0.7:
        return "⚠️ تحذير: مستوى الثقة منخفض، يتطلب موافقة بشرية."

    return "✅ تم تمرير الفحص السيادي."

def apply_slashing(agent_id, penalty_amount):
    passport = get_passport(agent_id)
    passport['economics']['stake'] -= penalty_amount
    passport['economics']['trust_score'] *= 0.9
    update_passport(passport)
    print(f"🔥 [Maestro]: تم حرق {penalty_amount} NST من رصيد {agent_id} بسبب فشل في الامتثال.")
