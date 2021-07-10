# bot.py
import random
import discord
from discord.ext import commands
from Bot_Tictactoe import Action
import asyncio

with open("token") as token:
    TOKEN = token.read()

client = commands.Bot(command_prefix="~")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command(name="banana")
async def banana(context):
    await context.message.channel.send(
        "https://cdn.discordapp.com/attachments/626422692597202964/860522243036807218/crab_eating_Banana_video.gif")


@client.command(name="cherry")
async def cherry(context):
    await context.message.channel.send("https://tenor.com/view/crab-eating-food-gif-9038987")


@client.command(name="pet")
async def pet(context):
    await context.message.channel.send(
        "https://tenor.com/view/crab-crab-petting-crabs-jacque-cousteau-cousteau-gif-3530356")


@client.command(name="randomgif")
async def randomgif(context):
    all_crab_gifs = [
        "https://cdn.discordapp.com/attachments/626422692597202964/860522243036807218/crab_eating_Banana_video.gif",
        "https://tenor.com/view/crab-eating-food-gif-9038987",
        "https://tenor.com/view/crab-crab-petting-crabs-jacque-cousteau-cousteau-gif-3530356",
        "https://tenor.com/view/crab-gif-8966784",
        "https://tenor.com/view/fighting-crab-crab-with-a-knife-hes-got-a-knife-dont-touch-me-bro-get-off-gif-18793247",
        "https://tenor.com/view/cute-crab-delicious-strawberry-snacking-gif-16719471"]

    await context.message.channel.send(all_crab_gifs[random.randint(0, len(all_crab_gifs) - 1)])


@client.command(name="tictactoe")
async def tictactoe(context):  # I know, I should probably use "ctx" instead
    game_won = None
    action: Action = Action()
    board_values = ["▢" for i in range(1, 10, 1)]
    board = "{0}|{1}|{2}\n{3}|{4}|{5}\n{6}|{7}|{8}".format(
        board_values[0],
        board_values[1],
        board_values[2],
        board_values[3],
        board_values[4],
        board_values[5],
        board_values[6],
        board_values[7],
        board_values[8]
    )
    user_symbol = "X"
    bot_symbol = "O"

    board_embed = discord.Embed(title="TicTacToe", color=0xb11d14)
    board_embed.add_field(name=board, value="___", inline=False)
    board_embed.set_footer(text="Your Turn! Type a number between 1 and 9.")
    await context.channel.send(embed=board_embed)
    while True:  # the whole game loop

        # this is the user_input
        while True:
            print(board_values)
            value_error = False
            def check(user_input):
                try:
                    return user_input.author == context.author and user_input.channel == context.channel and \
                            int(user_input.content) in range(1, 10, 1)
                except ValueError:
                    global value_error
                    value_error = True
                    pass

            try:
                user_input = await client.wait_for("message", check=check, timeout=60)
            except asyncio.TimeoutError:
                await context.channel.send("Sorry, you took too long! The game is now closing")
                return
            if not value_error:

                if board_values[int(user_input.content)] == "▢":
                    board_values[int(user_input.content)-1] = user_symbol
                    # print(board_values)
                    # print(int(user_input.content)-1)
                    break

                else:   
                    await context.channel.send("whoops, that field is already taken! Please choose another one")
        game_won = action.win_detection(board_values)
        # this is a game_ended function I couldn't use because it isn't async, yet contains operations like await [...]
        if game_won is None:
            if action.draw_condition(board_values):
                await context.channel.send("IT'S A DRAW!")
                return
        if game_won:
            await context.channel.send(f"Contrats @{context.author}! You Won :crab:")
            return
        if game_won == False:
            await context.channel.send(" Oh no! D: You Lost.")
            return

        action.bot_turn(board_values)

        board = "{0}|{1}|{2}\n{3}|{4}|{5}\n{6}|{7}|{8}".format(
            board_values[0],
            board_values[1],
            board_values[2],
            board_values[3],
            board_values[4],
            board_values[5],
            board_values[6],
            board_values[7],
            board_values[8]
        )  # updating the board_values does not automatically update board, so I'm updating it "manually"
        board_embed.set_field_at(index=0, name=board, value="___", inline=False)
        await context.message.channel.send(embed=board_embed)

        game_won = action.win_detection(board_values)
        if game_won is None:
            if action.draw_condition(board_values):
                await context.channel.send("IT'S A DRAW!")
                return
        if game_won:
            await context.channel.send("Contrats @" + context.author + "! You Won :crab:")
            return
        if game_won == False:
            await context.channel.send(" Oh no! D: You Lost.")
            return

client.run(TOKEN)
