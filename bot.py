
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
        [InlineKeyboardButton("👤 My  Profile", callback_data="profile")],
        [InlineKeyboardButton("❓ How To Buy", callback_data="how")],
        [InlineKeyboardButton("🎧 Support", url=f"https://t.me/{SUPPORT.replace('@','')}")],
        [InlineKeyboardButton("📢 Proof Channel", url=PROOF)]
    ]

    await update.message.reply_text(
        "👋 Welcome to HUNTER GUILD GLORY BOT\n\nChoose an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await query.edit_message_text(
            f"""🛒 Buy Guild Glory

💰 Payment UPI:
`{UPI}`

📸 Payment ke baad screenshot Support par bhejo:
https://t.me/{SUPPORT.replace('@','')}
"""
        )

    elif query.data == "price":
        await query.edit_message_text(
            """💰 Price List

🥉 Bronze - ₹XX
🥈 Silver - ₹XX
🥇 Gold - ₹XX

Price update ke liye Support se contact karein.
"""
        )

    elif query.data == "orders":
        await query.edit_message_text(
            "📦 Order status ke liye Support se contact karein."
        )

    elif query.data == "profile":
        await query.edit_message_text(
            "👤 Profile feature coming soon."
        )

    elif query.data == "how":
        await query.edit_message_text(
            """❓ How To Buy

1. Buy Guild Glory par click karein.
2. UPI se payment karein.
3. Screenshot Support ko bhejein.
4. Order complete ho jayega.
"""
        )app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()