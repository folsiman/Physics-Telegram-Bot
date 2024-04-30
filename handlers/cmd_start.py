from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает команду /start"""

    keyboard = [
        [
            InlineKeyboardButton("Механика", callback_data="mechanics"),
            InlineKeyboardButton("Электродинамика", callback_data="electrodynamics"),
            InlineKeyboardButton("Термодинамика", callback_data="thermodynamics")
        ],
        [
            InlineKeyboardButton("Молекулярная физика", callback_data="Molecular Physics")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = "Вас приветствует Телеграмм бот PHYSICS! Этот бот поможет вам подготовится к первой части ЕГЭ по физике. Чтобы начать заниматься, выберите раздел физики выюрав одну из кнопок ниже 👇",
        reply_markup = reply_markup
    )

cmd_start = CommandHandler("start", start)