from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

ALLOWED_USER_ID = 123456789 # استبدل بمعرف معتز

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[{"text": "لوحة التحكم", "web_app": {"url": "https://aegant-ai.github.io/dashboard"}}],[InlineKeyboardButton('📊 الحالة', callback_data='status'), InlineKeyboardButton('🛠️ إصلاح شامل', callback_data='fix_all')],
                [InlineKeyboardButton('💡 استخبارات', callback_data='intel'), InlineKeyboardButton('💰 سجل التوفير', callback_data='savings')]]
    await update.message.reply_text('مرحباً معتز، اختر أمراً:', reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.from_user.id != ALLOWED_USER_ID: return
    if query.data == 'fix_all':
        # استدعاء دالة الإصلاح التلقائي
        await query.answer('جاري تنفيذ الإصلاح الشامل...')
    await query.answer()

# إعداد التطبيق...
