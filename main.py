import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

# ── Configuration ──────────────────────────────────────────────────────────────
TOKEN = os.environ.get("DISCORD_TOKEN")  # Stocké dans les variables d'environnement

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None  # On désactive la commande help par défaut
)

# ── Chargement des cogs ────────────────────────────────────────────────────────
COGS = [
    "cogs.moderation",
    "cogs.logs",
    "cogs.tickets",
    "cogs.antispam",
]

@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync les commandes slash
    print(f"✅ Bot connecté en tant que {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(bot.guilds)} serveur(s)"
        )
    )

async def main():
    async with bot:
        for cog in COGS:
            try:
                await bot.load_extension(cog)
                print(f"  ✔ Cog chargé : {cog}")
            except Exception as e:
                print(f"  ✘ Erreur chargement {cog} : {e}")
        keep_alive()
        await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
