import discord  # this will now point to discord-self
from discord.ext import commands
import json
import aiohttp
import asyncio

class MyClient(discord.Client):
    def __init__(self, *, intents):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f"✅ Logged in as {self.user}")

    async def on_message(self, message: discord.Message):
        if (
            not message.author.bot
            and "@here" not in message.content
            and "@everyone" not in message.content
            and message.channel.id != 1382041806971212047  # Replace with the channel you want to exclude
        ):
            if any(keyword.lower() in message.content.lower() for keyword in keywords):
                await self.send_notif(message)

    async def send_notif(self, message: discord.Message):
        # Build jump link
        discord_link = f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}"

        # Format the message
        notification = (
            f"🦊 New keyword detected!\n"
            f"👤 {message.author.display_name}\n"
            f"📢 {message.guild.name} | {message.channel.name}\n"
            f"🔗 [Jump to Message]({discord_link})\n"
            f"💬 {message.content}"
        )

        # Send to Discord
        discord_channel = self.get_channel(d['channel_to_send_to'])
        if discord_channel:
            await discord_channel.send(notification)
            await asyncio.sleep(5)  # Wait 5 seconds before the next message

        # Send to Telegram
    #     await self.send_to_telegram(notification)

    # async def send_to_telegram(self, message: str):
        # telegram_url = f"https://api.telegram.org/bot{d['telegram_bot_token']}/sendMessage"
        # payload = {
        #     'chat_id': d['telegram_chat_id'],
        #     'text': message,
        #     'parse_mode': 'Markdown'
        # }

        # async with aiohttp.ClientSession() as session:
        #     async with session.post(telegram_url, data=payload) as response:
        #         if response.status != 200:
        #             print(f"❌ Failed to send message to Telegram. Status code: {response.status}, Response: {await response.text()}")

# Load config
with open("config.json") as f:
    d = json.load(f)

# Define the list of keywords and phrases
keywords = [
  "phrase", "stake", "wallet", "cant", "unstaking", "delegate", "undelegate", "error", "staking", "fail", "claim", "metamask", "help", "where", "validator", "fix", "bug", "issue", "status", "load", "not", "ada", "register", "unstake", "why", "what", "stop", "work", "broken", "drep", "reward", "pool", "add", "valid", "exit", "support", "withdraw", "token", "ledger", "migrate", "connecting", "node", "swap", "validate", "lock", "where to", "how to", "unbond", "bond", "attestation", "migration", "migrating", "liquidity", "trezor", "keystone", "hardware", "eth2", "unbonding", "bonding", "claiming", "stakers", "nethermind", "pryzm", "prysm", "lighthouse", "beaconchain", "exit validator", "0x", "dag", "delegation", "epoch", "dashboard", "admin", "ticket", "connected", "sync", "synchronize", "update", "bridge", "remove", "unlock", "locked", "done", "debug", "transaction", "transfer", "governance", "shelly", "byron", "daedalus", "cardano", "xrp", "pending", "process", "stuck", "nami", "eternl", "lace", "nautilius", "please", "errors", "can", "eta", "processing", "recover", "blocks", "mainnet", "live", "tracker", "cpu issues", "recovering", "shutdown", "access", "resync", "fixes", "validators", "approval", "contract", "credential", "credentials", "website", "missed", "32", "64", "asset", "amount", "prove", "balance", "vault", "wmtx", "farm", "farming", "application", "softnode", "collateral", "integration", "lottery", "bridging", "loading", "section", "delegating", "instruction", "fee", "error message", "funds", "zilliqa", "zil", "drained", "problem", "problems", "btc", "swapped", "holders", "holder", "txid", "tx", "sign", "hash", "control", "stucked", "safe", "flashbots", "bot", "mev", "compromised", "protect", "can't", "eth", "failed", "help me", "signing"
]

# Initialize bot
intent= discord.Client
client = MyClient(intents=intent)
client.run('MTM3NDkyMDM2MTU2MDI0NDMxNA.GGmehl.hOoe0K9fU6TLHR8kX6QmLFIxlUxs7F34OO96KM')
