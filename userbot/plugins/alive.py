"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Currently Alive, my Honey master!` **ᓚᘏᗢ**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     "`Bot created by:` [𝒉𝒐𝒏𝒆𝒚 🎭](tg://user?id=621788749)\n"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "**•Link Github :** [Click here](https://github.com/saskeuday/Haney)\n\n"
                     "• 𝒊 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒔𝒔𝒂𝒍 | 🍓🍯✨\n• 𝒌𝒊𝒔𝒔 𝒔𝒂𝒔𝒌𝒆 🥺🌿")
