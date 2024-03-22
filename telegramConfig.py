import telegram

# Entering the telegram bot parameters
Telegram_bot_token = input("Please enter your Telegram bot token: ")
Telegram_chat_id = input("Please enter your telegram chatId: ")

# Sending the message to the the prefered chat Id
bot = telegram.Bot(token=Telegram_bot_token)

bot.send_message(chat_id=Telegram_chat_id, text="wake up masaa imefika bana")
