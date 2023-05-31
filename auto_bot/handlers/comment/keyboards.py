from telegram import InlineKeyboardButton, InlineKeyboardMarkup

STAR = '\U00002b50'


def inline_comment_kb():
    keyboard = [
        [InlineKeyboardButton(STAR * 5, callback_data="5_Star")],
        [InlineKeyboardButton(STAR * 4, callback_data="4_Star")],
        [InlineKeyboardButton(STAR * 3, callback_data="3_Star")],
        [InlineKeyboardButton(STAR * 2, callback_data="2_Star")],
        [InlineKeyboardButton(STAR * 1, callback_data="1_Star")]
    ]
    return InlineKeyboardMarkup(keyboard)
