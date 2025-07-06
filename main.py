import requests
import discord

TAVERN_ID = 782347341667631144
GALLERY_ID = 786628157838589952
CONTENT_TYPES = ["image/png", "image/jpeg", "video/mp4"]
DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"

def download_file(filepath, url):
   response = requests.get(url, params={"User-Agent": DEFAULT_USER_AGENT})
   with open(filepath, mode="wb") as file:
        file.write(response.content)

def get_filetype(filename):
    return filename.split(".")[-1].split(":")[0]

def get_save_path(message, filename):
    return f"C:\\Art\\{message.created_at.strftime("%Y-%m-%d_%H%M%S")}_{message.author.name}.{get_filetype(filename)}"

class Mereno(discord.Client):
    async def on_ready(self):
        print("All set, Sensei!")

    async def on_message(self, message):
        if message.channel.id == GALLERY_ID or message.guild.id != TAVERN_ID:
            for attachment in message.attachments:
                if attachment.content_type in CONTENT_TYPES:
                    download_file(get_save_path(message, attachment.filename), attachment.url)

            for embed in message.embeds:
                if embed.image:
                    download_file(get_save_path(message, embed.image.url), embed.image.url)

with open(r"C:\Development\Mereno\token.txt") as file:
    token = file.read()

client = Mereno(intents=discord.Intents.all())
client.run(token)