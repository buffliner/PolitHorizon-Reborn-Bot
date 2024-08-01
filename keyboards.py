from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config

def get_mainKeyboard():
    mainButtons = [
        [
            InlineKeyboardButton(text='Support Request', 
                                 callback_data='request'),
            InlineKeyboardButton(text='Server Address',
                                 callback_data='ip_request')
        ],
        [
            InlineKeyboardButton(text='Return', 
                                 callback_data='return')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=mainButtons)
    return keyboard

def get_supportForm():
    supportButtons = [
        [
            InlineKeyboardButton(text='Form URL',
                                 url=config.form_url, 
                                )
        ],
        [
            InlineKeyboardButton(text='Return', 
                                 callback_data='return')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=supportButtons)
    return keyboard

def get_simpleKeyboard():
    simpleButtons = [
        [InlineKeyboardButton(text='Return', 
                                 callback_data='return')
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=simpleButtons)
    return keyboard

def get_supportKeyboard():
    supportButtons = [
        [
            InlineKeyboardButton(
                text='Requests',
                url='https://docs.google.com/spreadsheets/d/1cZnYjfUPvOi9oMTy8U5gpDwFVnmgpHtAjGHfwHO5DcA/edit?usp=sharing'
            )
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=supportButtons)
    return keyboard