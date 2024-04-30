from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, MessageHandler, filters
import json

async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Проверяет ответ пользователя на задачу"""

    user_task = context.user_data.get('task')

    # Чтение задач из JSON
    with open('tasks.json', 'r', encoding='utf-8') as file:
        tasksJSON_data = json.load(file)
            
        # Проверка наличия задачи с указанным названием
        if user_task in tasksJSON_data:
            task = tasksJSON_data[user_task][0]  # Первая задача с указанным названием

            if task['answer'] == update.message.text:
                del context.user_data['task']
                await update.message.reply_text("Ответ правильный!")
            else:
                keyboard = [
                    [
                        InlineKeyboardButton("Показать", callback_data="show")
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)

                await update.message.reply_text(
                    text = "Ответ неправильный! Хотите ли вы посмотреть решение с объяснением?",
                    reply_markup = reply_markup
                )

event_message = MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer)