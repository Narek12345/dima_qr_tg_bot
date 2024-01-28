from aiogram import executor
from handlers import client
from config import dp

# Регистрируем все хэндлеры.
client.register_client_handlers(dp)


if __name__ == '__main__':
	executor.start_polling(dp)