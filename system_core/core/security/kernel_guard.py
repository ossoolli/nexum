def check_security_clearance(user_id, command):
    FOUNDER_ID = "Mutaz_Ismail_Tailakh"
    SENSITIVE_PATTERNS = [".env", "cat <<", "git push", "0x", "bc1", "TW9"]
    
    if any(pattern in command for pattern in SENSITIVE_PATTERNS):
        if user_id == FOUNDER_ID:
            return True
        return False
    return True
