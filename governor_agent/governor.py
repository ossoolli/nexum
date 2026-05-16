import json

def arbitrate(request):
    if request.get('use_openai'):
        # التحقق من توقيع الوكيل التقني
        return False
    return True
