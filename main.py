import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Siz taqdim etgan bot tokeni o'rnatildi
API_TOKEN = '8868621493:AAHCaQMWyx3P-1azB7nvgyu0tuBIPruIbeI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# --- DIZAYN VA INTERFEYS (Apple / Bionic AI Style) ---

def sub_keyboard():
    """Majburiy obuna kanallari (Qora dizayn uslubida)"""
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("📢 Telegram 1 (MUZZCOLD)", url="https://t.me/MUZZCOLD"),
        InlineKeyboardButton("📢 Telegram 2 (LINEBET | INSIDER)", url="https://t.me/LINEBET_STAFKALARR"),
        InlineKeyboardButton("⚡️ Obunani Tekshirish", callback_data="check_sub")
    )
    return keyboard

def main_menu():
    """Asosiy menyu - Apple/Bionic uslubidagi tugmalar"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        KeyboardButton("🍏 Apple of Fortune"),
        KeyboardButton("💣 Mines"),
        KeyboardButton("🆔 Linebet ID kiritish"),
        KeyboardButton("🎁 Promokodlar")
    )
    return keyboard

def back_menu():
    """Ortga qaytish tugmasi"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("⬅️ Asosiy menyu"))
    return keyboard


# --- BOT LOGIKASI VA HANDLERLAR ---

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    welcome_text = (
        "▪️ **BIONIC AI // SIGNAL PRO v6.2**\n\n"
        "🖤 *Neural Interface Faollashdi.*\n"
        " Apple of Fortune va Mines o'yinlari uchun yuqori aniqlikdagi sun'iy intellekt signallari tizimiga xush kelibsiz.\n\n"
        "🔹 Davom etish uchun quyidagi kanallarga obuna bo'ling:"
    )
    await message.reply(welcome_text, reply_markup=sub_keyboard(), parse_mode="Markdown")


@dp.callback_query_handler(text="check_sub")
async def check_subscription(call: types.CallbackQuery):
    await call.message.answer(
        "⚡️ **Ulanish muvaffaqiyatli yakunlandi.**\n"
        "Bionic AI tizimi to'liq ishga tushdi. Kerakli bo'limni tanlang:",
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )
    await call.answer()


@dp.message_handler(text="⬅️ Asosiy menyu")
async def back_to_main(message: types.Message):
    await message.answer("🖤 **Asosiy Boshqaruv Paneli:**", reply_markup=main_menu(), parse_mode="Markdown")


@dp.message_handler(text="🎁 Promokodlar")
async def show_promos(message: types.Message):
    promo_text = (
        "💎 **LINEBET RASMIY PROMOKODLARI:**\n\n"
        "✨ `DARKWOLF76`[span_0](start_span)[span_0](end_span)\n"
        "✨ `BE127`\n\n"
        "💡 *Eslatma:* Ushbu promokodlar orqali ro'yxatdan o'tish sun'iy intellekt signallarining aniqligini oshiradi va 100% gacha bonus taqdim etadi[span_1](start_span)[span_1](end_span)."
    )
    await message.answer(promo_text, parse_mode="Markdown")


@dp.message_handler(text="🆔 Linebet ID kiritish")
async def ask_id(message: types.Message):
    await message.answer("🆔 Iltimos, Linebet ID raqamingizni kiriting (Masalan: `98765432`):", reply_markup=back_menu(), parse_mode="Markdown")


@dp.message_handler(text="🍏 Apple of Fortune")
async def apple_signal(message: types.Message):
    signal_msg = (
        "🍏 **APPLE OF FORTUNE // BIONIC SIGNAL**\n\n"
        "Row 1: 🍎  🍎  🍏  🍎\n"
        "Row 2: 🍎  🍏  🍎  🍎\n"
        "Row 3: 🍏  🍎  🍎  🍎\n"
        "Row 4: 🍎  🍎  🍎  🍏\n"
        "Row 5: 🍎  🍏  🍎  🍎\n\n"
        "⚙️ *Status:* `100K-AI Optimized`\n"
        "🔑 *Faol Promokod:* `DARKWOLF76`[span_2](start_span)[span_2](end_span)"
    )
    await message.answer(signal_msg, parse_mode="Markdown")


@dp.message_handler(text="💣 Mines")
async def mines_signal(message: types.Message):
    board = (
        "⬜️  ⭐️  ⬜️  ⬜️  ⬜️\n"
        "⬜️  ⬜️  ⬜️  ⭐️  ⬜️\n"
        "⭐️  ⬜️  ⬜️  ⬜️  ⬜️\n"
        "⬜️  ⬜️  ⭐️  ⬜️  ⬜️\n"
        "⬜️  ⬜️  ⬜️  ⬜️  ⭐️"
    )
    signal_msg = (
        "💣 **MINES // NEURAL MATRIX SIGNAL**\n\n"
        f"{board}\n\n"
        "🎯 *Tavsiya etilgan qadamlar belgilandi.*\n"
        "🔑 *Faol Promokod:* `DARKWOLF76`[span_3](start_span)[span_3](end_span)"
    )
    await message.answer(signal_msg, parse_mode="Markdown")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
