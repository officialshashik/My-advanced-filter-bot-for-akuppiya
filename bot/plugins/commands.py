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
                                    '𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿𝘀 🐣', url="https://t.me/apealkuppiya"
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
        InlineKeyboardButton('𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿𝘀 🐣', url='https://t.me/apealkuppiya'),
        InlineKeyboardButton('ᴀʟᴇᴠᴇʟ ᴋᴜᴘᴘɪʏᴀ ɢʀᴏᴜᴘ 🪶', url ='https://t.me/apealkuppiya')
    ],[
        InlineKeyboardButton('ᴀʟᴇᴠᴇʟ ᴋᴜᴘᴘɪʏᴀ ᴄʜᴀɴɴᴇʟ 🐣', url='https://t.me/alevelkuppiya1')
    ],[
        InlineKeyboardButton('𝗛𝗲𝗹𝗽 🙋🏻‍♂️', callback_data="help")
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
        InlineKeyboardButton('ᗩ/し ᏦᑌᑭᑭᏆᎩᗩᵀᴹ 🐣', callback_data='start'),
        InlineKeyboardButton('𝗔𝗯𝗼𝘂𝘁 💁🏻‍♂️', callback_data='about')
    ],[
        InlineKeyboardButton('𝗖𝗹𝗼𝘀𝗲 🌙', callback_data='close')
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
        InlineKeyboardButton('𝐇𝐨𝐦𝐞 🍃', callback_data='start'),
        InlineKeyboardButton('🌊𝗖𝗹𝗼𝘀𝗲', callback_data='close')
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
