import random
import discord
from discord.ext import commands
import asyncio





class Action:

    def bot_turn(self, board_values):
        while True:
            bot_input = random.randint(0, 8)
            if board_values[bot_input] == "▢":
                board_values[bot_input] = "O"
                return

    def win_detection(self, board_values):
        # if win_detection returns True, you won the game. If False, you lost, if None it isn't finished
        x = "X"
        o = "O"
        if board_values[0] == x and board_values[1] == x and board_values[2] == x:
            return True
        elif board_values[3] == x and board_values[4] == x and board_values[5] == x:
            return True
        elif board_values[6] == x and board_values[7] == x and board_values[8] == x:
            return True
        elif board_values[0] == x and board_values[3] == x and board_values[6] == x:
            return True
        elif board_values[1] == x and board_values[4] == x and board_values[7] == x:
            return True
        elif board_values[3] == x and board_values[5] == x and board_values[8] == x:
            return True
        elif board_values[0] == x and board_values[4] == x and board_values[8] == x:
            return True
        elif board_values[2] == x and board_values[4] == x and board_values[6] == x:
            return True

        elif board_values[0] == o and board_values[1] == o and board_values[2] == o:
            return False  # if win_detection returns True, you won the game. If False, you lost, if None it isn't finished
        elif board_values[3] == o and board_values[4] == o and board_values[5] == o:
            return False
        elif board_values[6] == o and board_values[7] == o and board_values[8] == o:
            return False
        elif board_values[0] == o and board_values[3] == o and board_values[6] == o:
            return False
        elif board_values[1] == o and board_values[4] == o and board_values[7] == o:
            return False
        elif board_values[3] == o and board_values[5] == o and board_values[8] == o:
            return False
        elif board_values[0] == o and board_values[4] == o and board_values[8] == o:
            return False
        elif board_values[2] == o and board_values[4] == o and board_values[6] == o:
            return False
        else:
            return None

    def draw_condition(self, board_values):
        for i in board_values:
            if i == "▢":
                return False
        return True
