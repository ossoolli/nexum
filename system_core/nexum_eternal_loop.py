import time
import subprocess
import sys

# إضافة المسارات
sys.path.append('/home/madarmutaz/AI-Agents/system_core')

def run_pulse():
    print(f"\n✨ [Nexum-Pulse]: دورة تطور جديدة تبدأ في {time.ctime()}")
    
    # 1. تشغيل وكيل التطور لضخ أفكار جديدة
    subprocess.run(["python3", "/home/madarmutaz/AI-Agents/system_core/nexum_evolution_agent.py"])
    
    # 2. تشغيل المزامنة لرفع أي تحديثات جديدة لـ GitHub
    subprocess.run(["python3", "/home/madarmutaz/AI-Agents/system_core/auto_git_sync.py"])

if __name__ == "__main__":
    print("🚀 تفعيل التوجيه الذاتي لـ Nexum... الوكلاء الآن في وضع العمل الأبدي.")
    while True:
        try:
            run_pulse()
            # الانتظار لمدة ساعة بين كل "نبضة" تطور (يمكنك تقليلها للاختبار)
            time.sleep(3600) 
        except KeyboardInterrupt:
            print("\n🛑 تم إيقاف التفعيل الذاتي بطلب من القائد.")
            break
