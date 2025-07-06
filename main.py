import discord

from utils import *

TAVERN_ID = 782347341667631144
GALLERY_ID = 786628157838589952
CONTENT_TYPES = ["image/png", "image/jpeg", "video/mp4"]

def get_save_path(message, filename: str) -> str:
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