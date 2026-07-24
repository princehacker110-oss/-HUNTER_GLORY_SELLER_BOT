
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

SUPPORT = "@HUNTER_GULD_GLORY_SELLER"
PROOF = "https://t.me/+uN5pFowY-IMyMTNl"
UPI = "8102709706-4@ybl"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 Buy Guild Glory", callback_data="buy")],
        [InlineKeyboardButton("💰 Price List", callback_data="price")],
        [InlineKeyboardButton("📦 My Orders", callback_data="orders")],
        [InlineKeyboardButton("👤 My Profile", callback_data="profile")],
        [InlineKeyboardButton("❓ How To Buy", callback_data="how")],
        [InlineKeyboardButton("🎧 Support", url=f"https://t.me/{SUPPORT.replace('@','')}")],
        [InlineKeyboardButton("📢 Proof Channel", url=PROOF)]
    ]

    await update.message.reply_text(
        "👋 Welcome to HUNTER GUILD GLORY BOT\n\nChoose an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )