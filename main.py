import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env.
load_dotenv()

# Читаем переменные окружения.
BOT_TOKEN = os.getenv('BOT_TOKEN')
WATEWMARK_SIZE = os.getenv('WATEWMARK_SIZE')
PATH_TO_WATERMARK = os.getenv('PATH_TO_WATERMARK')
CHANNEL_LINK = os.getenv('CHANNEL_LINK')
CHANNEL_ID = os.getenv('CHANNEL_ID')
