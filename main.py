import logging
from telegram.ext import ApplicationBuilder
from decouple import config

# import handlers
from handlers.cmd_start import cmd_start
from handlers.event_button import event_button
from handlers.event_message import event_message

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(config("token")).build()

    application.add_handler(cmd_start)
    application.add_handler(event_button)
    application.add_handler(event_message)

    application.run_polling()