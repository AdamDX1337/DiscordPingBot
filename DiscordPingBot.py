import discord
import random
import asyncio

intents = discord.Intents.default()
intents.members = True  # Ensure the bot can get member info

client = discord.Client(intents=intents)

TOKEN = 'TOKEN'
GUILD_ID = 'SERVER ID'
CHANNEL_ID = 'CHANNEL ID'
TIME = int(1800) #IN SECONDS (1800 = 5 minutes)

# List of messages to append to the ping
messages = [
    "Have a good day!",
    "Don't Forget to smile!",
    "I love HOI4!",
    "Hope you're having a great day!",
    "Make sure to stay safe!",
    "I wish every host has a safe game!",
    "My name is Modernth if you didn't know.",
    "Hi! Few things to start off with =] 1.Yes Im pinging you because you're a female HOI4 player, 'tis an awesome thing to see! 2. I'm Modernth. 3.Don't be intimidated, but I'm not a stereotypcial guy. If anything, I'll be the one in the kitchen =D.",
    "Remember to Subscribe to SilverXK and Modernth on YT",
    "Do not mention that one server that starts with an F and ends in UWG",
    "Silverhook is NOT a bitcoin miner, it does NOT mine all of your files and send it to <@1133902331663093851>",
    "Prehost is up, rehosting in 5 days",
    "Where is HOI4LobbyJoiner.exe?",
    "We (The DNB Committee) is 90% sure that <@1185594919180566608> does infact own # and sends it to people, make sure to block and report him in any and all servers you see",
    "#FuckRedBaron",
    "Did you know if you ask the Road to 56 mods really nicely, theyll send you a fresh copy of the newest HOI4 .pdb file"
]

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    guild = discord.utils.get(client.guilds, id=int(GUILD_ID))
    channel = client.get_channel(int(CHANNEL_ID))
    message_to_send = ""
    while True:
        members = [member for member in guild.members if not member.bot]
        if members:
            tempMSG = message_to_send
            member_to_ping = random.choice(members)
            message_to_send = random.choice(messages)
            while message_to_send == tempMSG:
                message_to_send = random.choice(messages)
            await channel.send(f'{member_to_ping.mention} {message_to_send}')
            print(f'Sent Message: {message_to_send}')
        await asyncio.sleep(TIME)  # Wait for 5 minutes

client.run(TOKEN)
