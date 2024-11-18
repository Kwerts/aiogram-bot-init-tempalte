from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def any_message_echo(message: Message):
    await message.answer(text=message.text)
