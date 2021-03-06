import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from Main import *
import json
import random
import requests


class menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def menu(self, ctx):
        author = ctx.message.author
        await ctx.send(
            embed=discord.Embed(title=f'{author}' + ", ""Welcome to the menu!"),
            components=[
                [Button(style=ButtonStyle.gray, label="Tube", emoji="โถ"),
                 Button(style=ButtonStyle.gray, label="Poker", emoji="๐"),
                 Button(style=ButtonStyle.gray, label="Doodle", emoji="๐๏ธ")],
                [Button(style=ButtonStyle.gray, label="Chance", emoji="๐ฒ"),
                 Button(style=ButtonStyle.gray, label="Ask", emoji="โ"),
                 Button(style=ButtonStyle.gray, label="Clear 10 messages", emoji="๐งน")],
            ],
        )

        response = await bot.wait_for("button_click")
        if response.channel == ctx.channel:
            if response.component.label == "Tube":
                data = {
                    "max_age": 86400,
                    "max_uses": 0,
                    "target_application_id": 755600276941176913,  # YouTube
                    "target_type": 2,
                    "temporary": False,
                    "validate": None
                }
                headers = {
                    "Authorization": "Bot {0}".format(Token),
                    "Content-type": "application/json"
                }

                if ctx.author.voice is not None:
                    if ctx.author.voice.channel is not None:
                        channel = ctx.author.voice.channel.id
                    else:
                        await ctx.channel.purge(limit=2)
                        await ctx.send("Please, join on the channel!")
                        await response.edit_origin()
                else:
                    await ctx.channel.purge(limit=2)
                    await ctx.send("Please, join on the channel!")
                    await response.edit_origin()

                responses = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites',
                                          data=json.dumps(data),
                                          headers=headers)
                link = json.loads(responses.content)

                await ctx.channel.purge(limit=2)
                await ctx.send(f'{author.mention}' + " " + f"https://discord.com/invite/{link['code']}")
                await response.edit_origin()

            elif response.component.label == "Poker":
                data = {
                    "max_age": 86400,
                    "max_uses": 0,
                    "target_application_id": 755827207812677713,  # Poker
                    "target_type": 2,
                    "temporary": False,
                    "validate": None
                }
                headers = {
                    "Authorization": "Bot {0}".format(Token),
                    "Content-type": "application/json"
                }

                if ctx.author.voice is not None:
                    if ctx.author.voice.channel is not None:
                        channel = ctx.author.voice.channel.id
                    else:
                        await ctx.channel.purge(limit=2)
                        await ctx.send("Please, join on the channel!")
                        await response.edit_origin()
                else:
                    await ctx.channel.purge(limit=2)
                    await ctx.send("Please, join on the channel!")
                    await response.edit_origin()

                responses = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites',
                                          data=json.dumps(data),
                                          headers=headers)
                link = json.loads(responses.content)

                await ctx.channel.purge(limit=2)
                await ctx.send(f'{author.mention}' + " " + f"https://discord.com/invite/{link['code']}")
                await response.edit_origin()

            elif response.component.label == "Doodle":
                data = {
                    "max_age": 86400,
                    "max_uses": 0,
                    "target_application_id": 878067389634314250,  # Doodle
                    "target_type": 2,
                    "temporary": False,
                    "validate": None
                }
                headers = {
                    "Authorization": "Bot {0}".format(Token),
                    "Content-type": "application/json"
                }

                if ctx.author.voice is not None:
                    if ctx.author.voice.channel is not None:
                        channel = ctx.author.voice.channel.id
                    else:
                        await ctx.channel.purge(limit=2)
                        await ctx.send("Please, join on the channel!")
                        await response.edit_origin()
                else:
                    await ctx.channel.purge(limit=2)
                    await ctx.send("Please, join on the channel!")
                    await response.edit_origin()

                responses = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites',
                                          data=json.dumps(data),
                                          headers=headers)
                link = json.loads(responses.content)

                await ctx.channel.purge(limit=2)
                await ctx.send(f'{author.mention}' + " " + f"https://discord.com/invite/{link['code']}")
                await response.edit_origin()

            elif response.component.label == "Clear 10 messages":
                messages = await ctx.channel.purge(limit=10)  # ะฟััะดะถะธะผ ัะพะพะฑัะตะฝะธั, +1 ั.ะบ. ะฝะฐัะต ัะพะถะต ัะดะฐะปะธััั
                await ctx.channel.purge(limit=2)
                await ctx.send(f"{len(messages)} messages were deleted")  # ะพะฟะพะฒะตััะตะผ ะพะฑ ัะดะฐะปะตะฝะธะธ ะธ ะบะพะปะธัะตััะฒะต ัะพะพะฑัะตะฝะธะน
                await response.edit_origin()

            elif response.component.label == "Chance":
                author = ctx.message.author  # ะฟะพะปััะฐะตะผ ะฐะฒัะพัะฐ ัะพะพะฑัะตะฝะธั.
                ran = random.randint(0, 100)  # ะณะตะฝะตัะธััะตะผ ัะปััะฐะนะฝะพะต ัะธัะปะพ ะฒ ะดะธะฐะฟะพะทะพะฝะต ะพั 0 ะดะพ 100 ะฒะบะปััะธัะตะปัะฝะพ.
                await ctx.channel.purge(limit=2)
                await ctx.send(
                    f' {author.mention}' + ", " + str(ran) + "%")  # ัะปะตะผ ะฒ ัะฐั ะฒะตัะพััะฝะพััั ัะฟะพะผะธะฝะฐั ะฐะฒัะพัะฐ ัะพะพะฑัะตะฝะธั
                await response.edit_origin()

            elif response.component.label == "Ask":
                ans = ['yes', 'no']  # ัะพะทะดะฐะตะผ ัะฟะธัะพะบ, ะฒะพะทะผะพะถะฝัั ะพัะฒะตัะพะฒ
                author = ctx.message.author  # ะฟะพะปััะฐะตะผ ะฐะฒัะพัะฐ ัะพะพะฑัะตะฝะธั.
                onezero = random.randint(0,
                                         1)  # ะฟะพะปััะฐะตะผ ัะปััะฐะนะฝะพะต ัะธัะปะพ, ะดะปั ัะพะณะพ ััะพะฑั ะฒััะฐัะธัั ัะปััะฐะนะฝัะน ะพัะฒะตั ะธะท ัะฟะธัะบะฐ
                await ctx.channel.purge(limit=2)
                await ctx.send(f'{author.mention}' + ", " + ans[onezero])  # ัะปัะผ ะฒ ัะฐั ะฒัะฟะพะปะฝะตะฝะฝัั ะบะพะผะฐะฝะดั
                await response.edit_origin()


def setup(bot):
    bot.add_cog(menu(bot=bot))
