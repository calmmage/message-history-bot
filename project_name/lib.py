from bot_lib import Handler, HandlerDisplayMode
from calmapp import App


class MyApp(App):
    def invoke(self, input_str):
        return input_str

    def dummy_command(self):
        return "Hey! I am a dummy"


class MyHandler(Handler):
    name = "main"
    display_mode = HandlerDisplayMode.FULL
    commands = {
        "dummy_command_handler": "dummy_command",
    }

    has_chat_handler = True

    async def chat_handler(self, message, app: MyApp):
        input_str = await self.get_message_text(message)
        output_str = app.invoke(input_str)
        await message.answer(output_str)

    async def dummy_command_handler(self, message, app: MyApp):
        output_str = app.dummy_command()
        await message.answer(output_str)
