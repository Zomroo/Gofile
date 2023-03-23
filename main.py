from telegram.ext import Updater, CommandHandler
from telegram
import config
import requests

# Define Telegram bot token
bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)

# Define API URLs
get_server_url = "https://api.gofile.io/getServer"
upload_file_url = "https://store1.gofile.io/uploadFile"
get_content_url = "https://api.gofile.io/getContent"
create_folder_url = "https://api.gofile.io/createFolder"
set_folder_option_url = "https://api.gofile.io/setFolderOption"
copy_content_url = "https://api.gofile.io/copyContent"
delete_content_url = "https://api.gofile.io/deleteContent"
get_account_details_url = "https://api.gofile.io/getAccountDetails"

# Define headers
headers = {"Token": config.GOFILE_API_KEY}

# Define start command handler
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Welcome to Gofile Bot. Send me a file to upload.')

# Define file upload handler
def upload_file(update, context):
    """Handle file upload and send the download link to the user."""
    file_id = update.message.document.file_id
    file = bot.getFile(file_id)
    file_name = file.file_path.split("/")[-1]
    file_url = f"https://api.telegram.org/file/bot{config.TELEGRAM_BOT_TOKEN}/{file.file_path}"
    server_response = requests.get(get_server_url, headers=headers).json()
    server_url = server_response["data"]["serverUrl"]
    payload = {"token": server_response["data"]["uploadServerToken"]}
    files = {"file": (file_name, requests.get(file_url).content)}
    upload_response = requests.post(upload_file_url, headers=headers, params=payload, files=files).json()
    download_url = upload_response["data"]["downloadPage"]
    update.message.reply_text(f"File uploaded successfully. Download link: {download_url}")

# Define main function
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = telegram.Updater(token=config.TELEGRAM_BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(telegram.ext.CommandHandler("start", start))

    # Add file upload handler
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.document, upload_file))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
