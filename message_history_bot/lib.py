from bot_lib import Handler, HandlerDisplayMode
from calmapp import App
from functools import wraps
from aiogram import BaseMiddleware
class MyApp(App):
    @wraps(App.__init__)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.messages = []

    def invoke(self, input_str):
        return input_str

    def dummy_command(self):
        return "Hey! I am a dummy"

    async def save_message(self, message):
        self.messages.append(message)

    def get_messages_count(self):
        return len(self.messages)

class MyHandler(Handler):
    name = "main"
    display_mode = HandlerDisplayMode.FULL
    commands = {
        "dummy_command_handler": "dummy_command",
        "get_messages_count_handler": "get_messages_count",
    }

    has_chat_handler = True

    async def chat_handler(self, message, app: MyApp):
        input_str = await self.get_message_text(message)
        output_str = app.invoke(input_str)
        await self.answer_safe(output_str, message)

    async def dummy_command_handler(self, message, app: MyApp):
        output_str = app.dummy_command()
        await self.answer_safe(output_str, message)

    async def get_messages_count_handler(self, message, app: MyApp):
        result = app.get_messages_count()
        output_str = f"Messages count: {result}"
        # output_str = app.dummy_command()
        await self.answer_safe(output_str, message)
        # await message.answer(output_str)

# class SaveIncomingMiddleware(BaseMiddleware):
#     async def on_process_message(self, message: types.Message, data: dict):
#         c.execute("INSERT INTO messages (chat_id, message_text, direction) VALUES (?, ?, ?)", (message.chat.id, message.text, 'incoming'))
#         conn.commit()

