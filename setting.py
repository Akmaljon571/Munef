from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from environs import Env

env = Env()
env.read_env()
storage = MemoryStorage()

bot = Bot(token=env('BOT_TOKEN'))
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = int(env('ADMIN'))
