from discord.ext import tasks
import discord
import logging

import json

from threading import Thread
from time import sleep

import classroom_handler as ch
import ftc_handler as ftc

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

with open('discord_id.json') as file:
    id_data = json.load(file)

BOT_TOKEN = id_data['bot_token']
GUILD = discord.Object(id=int(id_data['guild_id']))

TEST_CHANNEL_ID = int(id_data['channel_id'])

TEST_CLASSROOM_ID = id_data['classroom_id']



# with open('announcements.json') as file:
#     announcement_data = json.load(file)

# FTC team ids
team_id = {
    "RGB": 22075
}


# parsing announcement 
def parse_announcement(announcement):
    announcement_message = announcement['creatorUserId'] + ' posted at ' + announcement['creationTime'] + ': ' + announcement['text']
    return announcement_message

# initialized message
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await get_new_announcement.start()

# message event
@client.event
async def on_message(message):

    # do not want our own message
    if message.author == client.user:
        return
    
    if message.content.startswith('?hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('?'):
        command = message.content[1:]
        if len(command) > 0:
            
            # getting all the announcements - JUST USED FOR DEVELOPMENT PURPOSES
            if command == 'get_announcements':
                announcements = ch.get_announcements(TEST_CLASSROOM_ID)
                for announcement in announcements:
                    announcement_message = parse_announcement(announcement)
                    await message.channel.send(announcement_message)

            elif command.startswith('game_data'):
                command_data = command.split()
                if len(command_data) == 1:
                    await message.channel.send("Please provide the team name, your options are: RGB, Packbots, and Tundra.")
                else:
                    team_name = command_data[1]
                    tn = team_id[team_name]

                    team_info = ftc.TeamData.team_info(2022, tn)



            



# message constantly looking for a new announcement in google classroom
@tasks.loop(seconds=5)
async def get_new_announcement():

    announcement = ch.get_announcements(TEST_CLASSROOM_ID)[0]

    channel = client.get_channel(TEST_CHANNEL_ID)

    with open('announcement_ids.txt') as file:
        announcement_list = file.readlines()
        announcement_set = set()
    
    for announcement_id in announcement_list:
        announcement_set.add(announcement_id)

    if announcement['id'] + '\n' not in announcement_set:
        announcement_message = parse_announcement(announcement)
        announcement_set.add(announcement['id'])
        first = True
        file = open('announcement_ids.txt', 'w')
        
        for id in announcement_set:
            file.write(id + '\n')
            if first: 
                first = False
            else:
                file = open('announcement_ids.txt', 'a')
        
        await channel.send(announcement_message)



# main method 
if __name__ == '__main__':
    # error logger
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    # running the client
    client.run(BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)

    