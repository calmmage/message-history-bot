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
from calmapp.plugins import GptPlugin

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

@dp.update.outer_middleware()
async def message_history_middleware(
    handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
    event: Update,
    data: Dict[str, Any]
) -> Any:
    await app.save_message(event.model_dump(exclude_none=True))
    return await handler(event, data)

if __name__ == "__main__":
    run_bot(dp, bot)
