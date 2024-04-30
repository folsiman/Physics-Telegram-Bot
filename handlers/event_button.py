from random import randint
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
from telegram.constants import ParseMode
import json

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Анализирует CallbackQuery и обновляет текст сообщения."""

    query = update.callback_query
    await query.answer()

    if query.data == "mechanics":
        keyboard = [
            [
                InlineKeyboardButton("Динамика", callback_data="dinamics"),
                InlineKeyboardButton("Кинематика", callback_data="kinematics"),
                InlineKeyboardButton("Статика", callback_data="statics")
            ],
            [
                InlineKeyboardButton("Законы сохранения", callback_data="conservation_laws")
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text = f"Выберите подраздел механики!",
            reply_markup = reply_markup
        )
    elif query.data == "electrodynamics":
        keyboard = [
            [
                InlineKeyboardButton("Колебательный контур", callback_data="oscillating_circuit"),
                InlineKeyboardButton("Постоянный ток", callback_data="direct_current"),
                InlineKeyboardButton("Магнитное поле", callback_data="magnetic_field")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text = f"Выберите подраздел электродинамики!",
            reply_markup = reply_markup
        )
    elif query.data == "thermodynamics":
        keyboard = [
            [
                InlineKeyboardButton("Идеальный газ", callback_data="ideal_gas"),
                InlineKeyboardButton("фазовые переходы", callback_data="phase_transitions"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text = f"Выберите подраздел термодинамики!",
            reply_markup = reply_markup
        )
    elif query.data == "Molecular Physics":
        keyboard = [
            [
                InlineKeyboardButton("Молекулы", callback_data="molecules"),
                InlineKeyboardButton("Основное уравнение МКТ", callback_data="The_basic_equation_of_the_MCT"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text = f"Выберите подраздел Молекулярной физики!",
            reply_markup = reply_markup
        )

    async def replyTask(task_name):
        """Отправляет задачу в чат"""

        # Чтение задач из JSON
        with open('tasks.json', 'r', encoding='utf-8') as file:
            tasksJSON_data = json.load(file)
            
        # Проверка наличия задачи с указанным названием
        if task_name in tasksJSON_data:
            task = tasksJSON_data[task_name][0]  # Первая задача с указанным названием

            await query.edit_message_text( 
                text = f"{task['text']}\nПример ответа: 255",
                parse_mode = ParseMode.HTML
            )

    # Раздел - Механика   
    # динамика
    if query.data == "dinamics":
        random_task_number = randint(1, 10)

        task_name = f"dinamics_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    # кинематика
    elif query.data == "kinematics":
        random_task_number = randint(1, 10)

        task_name = f"kinematics_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    # статика
    elif query.data == "statics":
        random_task_number = randint(1, 8)

        task_name = f"statics_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    # законы сохранения
    elif query.data == "conservation_laws":
        random_task_number = randint(1, 10)

        task_name = f"conservation_laws_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    
    # Раздел - Электродинамика
    # колебательный контур
    if query.data == "oscillating_circuit":
        random_task_number = randint(1, 5)

        task_name = f"oscillating_circuit_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    # постоянный ток
    elif query.data == "direct_current":
        random_task_number = randint(1, 5)

        task_name = f"direct_current_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    # магнитное поле
    elif query.data == "magnetic_field":
        random_task_number = randint(1, 10)

        task_name = f"magnetic_field_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    
    # Раздел - Термодинамика
    # идеальный газ
    elif query.data == "ideal_gas":
        random_task_number = randint(1, 9)

        task_name = f"ideal_gas_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    # фазовые переходы
    elif query.data == "phase_transitions":
        random_task_number = randint(1, 7)

        task_name = f"phase_transitions_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    
    # Раздел - Молекулярная физика
    # молекулы
    elif query.data == "molecules":
        random_task_number = randint(1, 8)

        task_name = f"molecules_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name
    # основное уравнение МКТ
    elif query.data == "The_basic_equation_of_the_MCT":
        random_task_number = randint(1, 10)

        task_name = f"MKT_{random_task_number}"
        await replyTask(task_name)
        context.user_data['task'] = task_name

    # Вывод решения задачи
    if query.data == "show":
        user_task = context.user_data.get('task')

        async def replyTask(task_name):
            """Отправляет решение задачи в чат"""

            # Чтение задач из JSON
            with open('tasks.json', 'r', encoding='utf-8') as file:
                tasksJSON_data = json.load(file)
            
            # Проверка наличия задачи с указанным названием
            if task_name in tasksJSON_data:
                task = tasksJSON_data[task_name][0]  # Первая задача с указанным названием

                await query.message.reply_photo( photo = task["solution"], caption = f"Правильный ответ: {task['answer']}" )

        # Раздел - Механика
        # динамика
        for i in range(1, 11):
            if user_task == f"dinamics_{i}":
                await replyTask(f'dinamics_{i}')
        # кинематика
        for i in range(1, 11):
            if user_task == f"kinematics_{i}":
                await replyTask(f'kinematics_{i}')
        # статика
        for i in range(1, 9):
            if user_task == f"statics_{i}":
                await replyTask(f'statics_{i}')
        # законы сохранения
        for i in range(1, 11):
            if user_task == f"conservation_laws_{i}":
                await replyTask(f'conservation_laws_{i}')
        
        # Раздел - Электродинамика
        # колебательный контур
        for i in range(1, 6):
            if user_task == f"oscillating_circuit_{i}":
                await replyTask(f'oscillating_circuit_{i}')
        # постоянный ток
        for i in range(1, 6):
            if user_task == f"direct_current_{i}":
                await replyTask(f'direct_current_{i}')
        # магнитное поле
        for i in range(1, 11):
            if user_task == f"magnetic_field_{i}":
                await replyTask(f'magnetic_field_{i}')

        # Раздел - Термодинамика
        # идеальный газ
        for i in range(1, 10):
            if user_task == f"ideal_gas_{i}":
                await replyTask(f'ideal_gas_{i}')
        # фазовые переходы
        for i in range(1, 8):
            if user_task == f"phase_transitions_{i}":
                await replyTask(f'phase_transitions_{i}')
        
        # Раздел - Молекулярная физика
        # молекулярная физика
        for i in range(1, 9):
            if user_task == f"molecules_{i}":
                await replyTask(f'molecules_{i}')
        # основное уравнение МКТ
        for i in range(1, 11):
            if user_task == f"MKT_{i}":
                await replyTask(f'MKT_{i}')

event_button = CallbackQueryHandler(button)