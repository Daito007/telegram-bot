from telethon import TelegramClient, events
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API credentials
bot_token = os.getenv('BOT_TOKEN')
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Initialize the Telegram bot client
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Function to calculate the hash of an image file
def calculate_image_hash(file_path):
    with open(file_path, 'rb') as f:
        img_data = f.read()
        img_hash = hashlib.md5(img_data).hexdigest()
    return img_hash

# Event handler for the /start command
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    welcome_message = (
        "Welcome! 🎉\n\n"
        "I'm your image hash bot. Send me a .jpg or .jpeg image, "
        "and I'll calculate its hash for you!\n"
        "If you send me any other type of file or text, I'll let you know it's not supported."
    )
    await event.respond(welcome_message)

# Event handler for new messages (image or file processing)
@bot.on(events.NewMessage)
async def handler(event):
    if event.message.text and event.message.text.startswith('/'):
        return

    if event.message.media:  # Check if the message contains media (file, photo, etc.)
        if event.message.photo or (event.message.file and event.message.file.mime_type == 'image/jpeg'):
            # Download the image file
            file_path = await event.message.download_media()

            # Check if the file is a .jpg or .jpeg
            if file_path.endswith(('.jpg', '.jpeg')):
                # Calculate and return the hash
                img_hash = calculate_image_hash(file_path)
                await event.respond(f"Image hash: {img_hash}")
                
                # Clean up and remove the file after processing
                os.remove(file_path)
            else:
                await event.respond("Error: Only .jpg and .jpeg files are supported.")
        else:
            # Respond with error if the file is not supported
            await event.respond("Error: Unsupported file format.")
    else:
        # Respond with error if it is not a media message (e.g., it's text)
        await event.respond("Error: Only image files are allowed, no text.")

# Start the bot
print("Bot is running...")
bot.run_until_disconnected()
