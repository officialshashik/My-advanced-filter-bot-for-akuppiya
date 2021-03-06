#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'ππ²ππ²πΉπΌπ½π²πΏπ π£', url="https://t.me/apealkuppiya"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode=enums.ParseMode.HTML)
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('ππ²ππ²πΉπΌπ½π²πΏπ π£', url='https://t.me/apealkuppiya'),
        InlineKeyboardButton('α΄Κα΄α΄ α΄Κ α΄α΄α΄α΄ΙͺΚα΄ Ι’Κα΄α΄α΄ πͺΆ', url ='https://t.me/apealkuppiya')
    ],[
        InlineKeyboardButton('α΄Κα΄α΄ α΄Κ α΄α΄α΄α΄ΙͺΚα΄ α΄Κα΄Ι΄Ι΄α΄Κ π£', url='https://t.me/alevelkuppiya1')
    ],[
        InlineKeyboardButton('ππ²πΉπ½ ππ»ββοΈ', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('α©/γ α¦αα­α­αα©α©α΅α΄Ή π£', callback_data='start'),
        InlineKeyboardButton('ππ―πΌππ ππ»ββοΈ', callback_data='about')
    ],[
        InlineKeyboardButton('ππΉπΌππ² π', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('ππ¨π¦π π', callback_data='start'),
        InlineKeyboardButton('πππΉπΌππ²', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )
