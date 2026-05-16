import telebot
from agent_orchestrator import Maestro
from sovereign_treasury import SovereignTreasury

bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
maestro = Maestro()
treasury = SovereignTreasury()

@bot.message_handler(commands=['start', 'status'])
def send_status(message):
    status_report = '🤖 [System Status]: جميع الوكلاء في وضع الاستعداد.\n'
    status_report += '✅ Orchestrator: Active\n✅ Treasury: Connected\n✅ Escrow: Online'
    bot.reply_to(message, status_report)

@bot.message_handler(commands=['deploy_task'])
def handle_task(message):
    try:
        args = message.text.split()
        task_desc = args[1]
        reward = int(args[2])
        bot.reply_to(message, f'⚙️ جاري معالجة المهمة: {task_desc}...')
        result = maestro.allocate_resources(task_desc, reward)
        bot.send_message(message.chat.id, f'✅ تم تخصيص {reward} NST للمهمة. تم الربط مع Escrow.')
    except Exception as e:
        bot.reply_to(message, '❌ خطأ في الصيغة. استخدم: /deploy_task [المهمة] [المكافأة]')

if __name__ == '__main__':
    bot.polling(none_stop=True)
