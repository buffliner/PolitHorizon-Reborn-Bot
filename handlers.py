from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.methods import SendMessage

import keyboards
import config

router = Router()

@router.message(Command('start'))
async def startup(msg: Message):
    #await msg.answer(f'Welcome to PHR Bot!\nSelect option:', reply_markup=keyboards.get_mainKeyboard())
    await msg.answer(f'Bot in the test mode.\nServer is not launched')

@router.callback_query(F.data == 'request')
async def request(cq: CallbackQuery):
    await cq.message.edit_text('Support URL', reply_markup=keyboards.get_supportForm())
    return SendMessage(
        chat_id=config.SupportID,
        text='Check requests',
        reply_markup=keyboards.get_supportKeyboard()
    )

@router.callback_query(F.data == 'ip_request')
async def ip_request(cq: CallbackQuery):
    await cq.message.edit_text(f'IP: {config.ip_address}', reply_markup=keyboards.get_simpleKeyboard())

@router.callback_query(F.data == 'return')
async def Return(cq: CallbackQuery):
    await cq.message.edit_text(f'Welcome to PHR Bot!\nSelect option:', reply_markup=keyboards.get_mainKeyboard())