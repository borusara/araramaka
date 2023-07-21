from pyrogram import Client, filters
import os
import psycopg2
from moviepy.editor import VideoFileClip

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', and 'YOUR_BOT_TOKEN' with your API ID, API HASH, and Bot token from Telegram
API_ID = 27565584
API_HASH = 'bb9e0e8f7da356036f981bd41697703c'
BOT_TOKEN = '6216387988:AAGEPVhBcJtEVG5T37efpRiGDfduPYohhaw'

# Replace 'YOUR_ELEPHANTSQL_URL' with your actual ElephantSQL URL
ELEPHANTSQL_URL = 'postgres://pufqvopy:qbHTUM9KLFFP0UPcEPHObgu4YVQjqy37@arjuna.db.elephantsql.com/pufqvopy'

# Create the ElephantSQL connection
conn = psycopg2.connect(ELEPHANTSQL_URL)
cur = conn.cursor()

# Function to convert mp4 to mp3
def mp4_to_mp3(file_path):
    mp3_file_path = file_path.replace('.mp4', '.mp3')
    video_clip = VideoFileClip(file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3_file_path)
    audio_clip.close()
    video_clip.close()
    return mp3_file_path

# Handler for text messages
@Client.on_message(filters.command("start"))
def start(_, update):
    update.reply_text("Send me an mp4 file, and I'll convert it to mp3!")

# Handler for media messages (documents)
@Client.on_message(filters.document)
def convert_mp4_to_mp3(_, update):
    if update.document.mime_type == "video/mp4":
        file_path = app.download_media(update.document, file_name="temp.mp4")
        mp3_file_path = mp4_to_mp3(file_path)
        update.reply_audio(mp3_file_path)
        os.remove(file_path)
        os.remove(mp3_file_path)

# Run the bot
if __name__ == "__main__":
    # Initialize the Pyrogram Client
    app = Client("file_converter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

    # Run the Pyrogram Client until the program is interrupted
    app.run()

    # Close the ElephantSQL connection when the program ends
    conn.close()
