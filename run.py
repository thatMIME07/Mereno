import discord

from main import Mereno

def main() -> None:
    with open(r"C:\Development\Mereno\token.txt") as file:
        token: str = file.read()

    client = Mereno(intents=discord.Intents.all())
    client.run(token)

if __name__ == "__main__":
    main()