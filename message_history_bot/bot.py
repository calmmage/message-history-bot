from aiogram import Dispatcher
from dotenv import load_dotenv
from aiogram.types import Update
from message_history_bot.lib import MyApp, MyHandler  # MyPlugin
from typing import List, Callable, Awaitable, Dict, Any
from bot_lib import (
    BotConfig,
    setup_dispatcher,
)
from bot_lib.demo import create_bot, run_bot

# plugins = [GptPlugin]  # MyPlugin,
# app = MyApp(plugins=plugins)
app = MyApp()
bot_config = BotConfig(app=app)

# set up dispatcher
dp = Dispatcher()

my_handler = MyHandler()
handlers = [my_handler]
setup_dispatcher(dp, bot_config, extra_handlers=handlers)

load_dotenv()
bot = create_bot()

if __name__ == "__main__":
    run_bot(dp, bot)
