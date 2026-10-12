
import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Schubert Logistik Bot online: {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} Slash-Befehle synchronisiert.")
    except Exception as error:
        print(f"Fehler beim Synchronisieren: {error}")


@bot.tree.command(
    name="botstatus",
    description="Zeigt den Status des Schubert Logistik Bots."
)
async def botstatus(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🚛 Schubert Logistik Bot ist online!",
        ephemeral=True
    )


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError(
            "Der DISCORD_TOKEN ist nicht konfiguriert."
        )

    bot.run(TOKEN)
