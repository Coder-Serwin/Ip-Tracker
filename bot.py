import discord
import requests
import time
import asyncio
import os

client = None

class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)
            channeln = client.get_channel(906776389749981194)
            ip_addr = os.getenv("IP_ADDR")
            await channeln.send(ip_addr)
            await client.close()

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
