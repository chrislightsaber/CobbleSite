import discord
from discord.ext import commands
import pandas as pd
import os
from fuzzywuzzy import process
import numpy as np

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

EXCEL_FILE_PATH = r"C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDex.xlsx"

def refresh_data():
    return pd.read_excel(EXCEL_FILE_PATH)

a = ("normal")
b = ("fighting")
c = ("flying")
d = ("poison")
e = ("ground")
f = ("rock")
g = ("bug")
h = ("ghost")
i = ("steel")
j = ("fire")
k = ("water")
l = ("grass")
m = ("electric")
n = ("psychic")
o = ("ice")
p = ("dragon")
q = ("dark")
r = ("fairy")
def FindMonoWeakness(Type1):
    count = 0
    if Type1 != Type1:
        return("Type Not Entered")
    while (count < 1):
        owo = Type1.lower()
        print(owo)
        if owo == a:
            return("Weaknesses: Fighting\nResistances: none\nImmunities: Ghost")
        elif owo == b:
            return("Weaknesses: Fairy, Flying, Psychic \nResistances: Bug, Dark, Rock\nImmunities: None")
        elif owo == c:
            return("Weaknesses: Electric, Ice, Rock\nResistances: Bug, Fighting, Grass\nImmunities: Ground")
        elif owo == d:
            return("Weaknesses: Ground, Psychic\nResistances: Bug, Fairy, Fighting, Grass, Poison\nImmunities: None")
        elif owo == e:
            return("Weaknesses: Grass, Ice, Water\nResistances: Poison, Rock\nImmunities: Electric")
        elif owo == f:
            return("Weaknesses: Fighting, Grass, Ground, Steel, Water\nResistances: Fire, Flying, Normal, Poison\nImmunities: None")
        elif owo == g:
            return("Weaknesses: Fire, Flying, Rock\nResistances: Fighting, Grass, Ground\nImmunities: None")
        elif owo == h:
            return("Weaknesses: Dark, Ghost\nResistances: Bug, Poison\nImmunities: Fighting, Normal")
        elif owo == i:
            return("Weaknesses: Fighting, Fire, Ground\nResistances: Bug, Dragon, Fairy, Flying, Grass, Ice, Normal, Psychic, Rock, Steel\nImmunities: Poison")
        elif owo == j:
            return("Weaknesses: Ground, Rock, Water\nResistances: Bug, Fairy, Fire, Grass, Ice, Steel\nImmunities: None")
        elif owo == k:
            return("Weaknesses: Electric, Grass\nResistances: Fire, Ice, Steel, Water\nImmunities: None")
        elif owo == l:
            return("Weaknesses: Bug, Fire, Flying, Ice, Poison\nResistances: Electric, Grass, Ground, Water\nImmunities: None")
        elif owo == m:
            return("Weaknesses: Ground\nResistances: Electric, Flying, Steel\nImmunities: None")
        elif owo == n:
            return("Weaknesses: Bug, Dark, Ghost\nResistances: Fighting, Psychic\nImmunities: None")
        elif owo == o:
            return("Weaknesses: Fighting, Fire, Rock, Steel\nResistances: Ice\nImmunities: None")
        elif owo == p:
            return("Weaknesses: Dragon, Fairy, Ice\nResistances: Electric, Fire, Grass, Water\nImmunities: None")
        elif owo == q:
            return("Weaknesses: Bug, Fairy, Fighting\nResistances: Dark, Ghost\nImmunities: Psychic")
        elif owo == r:
            return("Weaknesses: Poison, Steel\nResistances: Bug, Dark, Fighting\nImmunities: Dragon")
        count = 1

def FindDuoWeakness(Type1,Type2):
    count = 0
    while (count < 1):
        owo = str(Type1) + " " + str(Type2)
        owo = owo.lower()
        print(owo)
        if owo == (a + " " + b) or owo == (b + " " + a):
            return("Weaknesses: Fairy, Fighting, Flying, Psychic\nResistances: Bug, Dark, Rock\nImmunities: Ghost")
        elif owo == (a + " " + c) or owo == (c + " " + a):
           return("Weaknesses: Electric, Ice, Rock\nResistances: Bug, Grass\nImmunities: Ghost, Ground")
        elif owo == (a + " " + d) or owo == (d + " " + a):
           return("Weaknesses: Ground, Psychic\nResistances: Grass, Poison, Bug, Fairy\nImmunities: Ghost")
        elif owo == (a + " " + e) or owo == (e + " " + a):
           return("Weaknesses: Fighting, Grass, Ice, Water\nResistances: Poison, Rock\nImmunities: Electric, Ghost")
        elif owo == (a + " " + f) or owo == (f + " " + a):
           return("Weaknesses: Water, Grass, Fighting, Ground\nResistances: Normal, Fire, Poison, Flying\nImmunities: Ghost")
        elif owo == (a + " " + g) or owo == (g + " " + a):
           return("Weaknesses: Fire, Flying, Rock\nResistances: Grass, Ground\nImmunities: Ghost")
        elif owo == (a + " " + h) or owo == (h + " " + a):
           return("Weaknesses: Dark\nResistances: Poison, Bug\nImmunities: Normal, Fighting, Ghost")
        elif owo == (a + " " + i) or owo == (i + " " + a):
           return("Weaknesses: Fire, Fighting, Ground\nResistances: Fire, Grass, Ice, Flying, Psychic, Bug, Rock, Dragon, Steel, Fairy\nImmunities: Poison, Normal")
        elif owo == (a + " " + j) or owo == (j + " " + a):
           return("Weaknesses: Fighting, Ground, Rock, Water\nResistances: Bug, Fairy, Fire, Grass, Ice, Steel\nImmunities: Ghost")
        elif owo == (a + " " + k) or owo == (k + " " + a):
           return("Weaknesses: Electric, Fighting, Grass\nResistances: Fire, Ice, Steel, Water\nImmunities: Ghost")
        elif owo == (a + " " + l) or owo == (l + " " + a):
           return("Weaknesses: Bug, Fighting, Fire, Flying, Ice, Poison\nResistances: Electric, Grass, Ground, Water\nImmunities: Ghost")
        elif owo == (a + " " + m) or owo == (m + " " + a):
           return("Weaknesses: Fighting, Ground\nResistances: Electric, Flying, Steel\nImmunities: Ghost")
        elif owo == (a + " " + m) or owo == (m + " " + a):
           return("Weaknesses: Fighting, Ground\nResistances: Electric, Flying, Steel\nImmunities: Ghost")
        elif owo == (a + " " + n) or owo == (n + " " + a):
           return("Weaknesses: Bug, Dark\nResistances: Psychic\nImmunities: Ghost")
        elif owo == (a + " " + o) or owo == (o + " " + a):
           return("Weaknesses: Fire, Fighting, Rock, Steel\nResistances: Ice\nImmunities: Ghost")
        elif owo == (a + " " + p) or owo == (p + " " + a):
           return("Weaknesses: Dragon, Fairy, Fighting, Ice\nResistances: Electric, Fire, Grass, Water\nImmunities: Ghost")
        elif owo == (a + " " + q) or owo == (q + " " + a):
           return("Weaknesses: Bug, Fairy, Fighting\nResistances: Dark\nImmunities: Ghost, Psychic")
        elif owo == (a + " " + r) or owo == (r + " " + a):
           return("Weaknesses: Poison, Steel\nResistances: Bug, Dark\nImmunities: Dragon, Ghost")
        elif owo == (b + " " + c) or owo == (c + " " + b):
           return("Weaknesses: Electric, Fairy, Flying, Ice, Psychic\nResistances: Bug, Dark, Fighting, Grass\nImmunities: Ground")
        elif owo == (b + " " + d) or owo == (d + " " + b):
           return("Weaknesses: Flying, Ground, Psychic\nResistances: Bug, Dark, Fighting, Grass, Poison, Rock\nImmunities: None")
        elif owo == (b + " " + e) or owo == (e + " " + b):
           return("Weaknesses: Water, Grass, Ice, Flying, Psychic, Fairy\nResistances: Poison, Bug, Rock, Dark\nImmunities: Electric")
        elif owo == (b + " " + f) or owo == (f + " " + b):
           return("Weaknesses: Fairy, Fighting, Grass, Ground, Psychic, Steel, Water\nResistances: Bug, Dark, Fire, Normal, Poison, Rock\nImmunities: None")
        elif owo == (b + " " + g) or owo == (g + " " + b):
           return("Weaknesses: Fairy, Fire, Flying, Psychic\nResistances: Bug, Dark, Fighting, Grass, Ground\nImmunities: None")
        elif owo == (b + " " + h) or owo == (h + " " + b):
           return("Weaknesses: Fairy, Flying, Ghost, Psychic\nResistances: Bug, Poison, Rock\nImmunities: Fighting, Normal")
        elif owo == (b + " " + i) or owo == (i + " " + b):
           return("Weaknesses: Fighting, Fire, Ground\nResistances: Bug, Dark, Dragon, Grass, Ice, Normal, Rock, Steel\nImmunities: Poison")
        elif owo == (b + " " + j) or owo == (j + " " + b):
           return("Weaknesses: Flying, Ground, Psychic, Water\nResistances: Bug, Dark, Fire, Grass, Ice, Steel\nImmunities: None")
        elif owo == (b + " " + k) or owo == (k + " " + b):
           return("Weaknesses: Electric, Fairy, Flying, Grass, Psychic\nResistances: Bug, Dark, Fire, Ice, Rock, Steel, Water\nImmunities: None")
        elif owo == (b + " " + l) or owo == (l + " " + b):
           return("Weaknesses: Fairy, Fire, Flying, Ice, Poison, Psychic\nResistances: Dark, Electric, Grass, Ground, Rock, Water\nImmunities: None")
        elif owo == (b + " " + m) or owo == (m + " " + b):
           return("Weaknesses: Ground, Psychic, Fairy\nResistances: Electric, Bug, Rock, Dark, Steel\nImmunities: None")
        elif owo == (b + " " + n) or owo == (n + " " + b):
           return("Weaknesses: Fairy, Flying, Ghost\nResistances: Fighting, Rock\nImmunities: None")
        elif owo == (b + " " + o) or owo == (o + " " + b):
           return("Weaknesses: Fairy, Fighting, Fire, Flying, Psychic, Steel\nResistances: Bug, Dark, Ice\nImmunities: None")
        elif owo == (b + " " + p) or owo == (p + " " + b):
           return("Weaknesses: Dragon, Fairy, Flying, Ice, Psychic\nResistances: Bug, Dark, Electric, Fire, Grass, Rock, Water\nImmunities: None")
        elif owo == (b + " " + q) or owo == (q + " " + b):
           return("Weaknesses: Fairy, Fighting, Flying\nResistances: Dark, Ghost, Rock\nImmunities: Psychic")
        elif owo == (b + " " + r) or owo == (r + " " + b):
           return("Weaknesses: Poison, Flying, Psychic, Steel, Fairy\nResistances: Fighting, Bug, Rock, Dark\nImmunities: Dragon")
        elif owo == (c + " " + d) or owo == (d + " " + c):
           return("Weaknesses: Electric, Ice, Psychic, Rock\nResistances: Bug, Fairy, Fighting, Grass, Poison\nImmunities: Ground")
        elif owo == (c + " " + e) or owo == (e + " " + c):
           return("Weaknesses: Ice, Water\nResistances: Bug, Fighting, Poison\nImmunities: Electric, Ground")
        elif owo == (c + " " + f) or owo == (f + " " + c):
           return("Weaknesses: Electric, Ice, Rock, Steel, Water\nResistances: Bug, Fire, Flying, Normal, Poison\nImmunities: Ground")
        elif owo == (c + " " + g) or owo == (g + " " + c):
           return("Weaknesses: Electric, Fire, Flying, Ice, Rock\nResistances: Bug, Fighting, Grass\nImmunities: Ground")
        elif owo == (c + " " + h) or owo == (h + " " + c):
           return("Weaknesses: Dark, Electric, Ghost, Ice, Rock\nResistances: Bug, Grass, Poison\nImmunities: Fighting, Ground, Normal")
        elif owo == (c + " " + i) or owo == (i + " " + c):
           return("Weaknesses: Electric, Fire\nResistances: Bug, Dragon, Fairy, Flying, Grass, Normal, Psychic, Steel\nImmunities: Ground, Poison")
        elif owo == (c + " " + j) or owo == (j + " " + c):
           return("Weaknesses: Electric, Rock, Water\nResistances: Bug, Fairy, Fighting, Fire, Grass, Steel\nImmunities: Ground")
        elif owo == (c + " " + k) or owo == (k + " " + c):
           return("Weaknesses: Electric, Rock\nResistances: Bug, Fighting, Fire, Steel, Water\nImmunities: Ground")
        elif owo == (c + " " + l) or owo == (l + " " + c):
           return("Weaknesses: Fire, Flying, Ice, Poison, Rock\nResistances: Fighting, Grass, Water\nImmunities: Ground")
        elif owo == (c + " " + m) or owo == (m + " " + c):
           return("Weaknesses: Ice, Rock\nResistances: Bug, Fighting, Flying, Grass, Steel\nImmunities: Ground")
        elif owo == (c + " " + n) or owo == (n + " " + c):
           return("Weaknesses: Dark, Electric, Ghost, Ice, Rock\nResistances: Fighting, Grass, Psychic\nImmunities: Ground")
        elif owo == (c + " " + o) or owo == (o + " " + c):
           return("Weaknesses: Electric, Fire, Rock, Steel\nResistances: Bug, Grass\nImmunities: Ground")
        elif owo == (c + " " + p) or owo == (p + " " + c):
           return("Weaknesses: Dragon, Fairy, Ice, Rock\nResistances: Bug, Fighting, Fire, Grass, Water\nImmunities: Ground")
        elif owo == (c + " " + q) or owo == (q + " " + c):
           return("Weaknesses: Electric, Fairy, Ice, Rock\nResistances: Dark, Ghost, Grass\nImmunities: Ground, Psychic")
        elif owo == (c + " " + r) or owo == (r + " " + c):
           return("Weaknesses: Electric, Ice, Poison, Rock, Steel\nResistances: Bug, Dark, Fighting, Grass\nImmunities: Dragon, Ground")
        elif owo == (d + " " + e) or owo == (e + " " + d):
           return("Weaknesses: Ground, Ice, Psychic, Water\nResistances: Bug, Fairy, Fighting, Poison, Rock\nImmunities: Electric")
        elif owo == (d + " " + f) or owo == (f + " " + d):
           return("Weaknesses: Ground, Psychic, Steel, Water\nResistances: Bug, Fairy, Fire, Flying, Normal, Poison\nImmunities: None")
        elif owo == (d + " " + g) or owo == (g + " " + d):
           return("Weaknesses: Fire, Flying, Psychic, Rock\nResistances: Bug, Fairy, Fighting, Grass, Poison\nImmunities: None")
        elif owo == (d + " " + h) or owo == (h + " " + d):
           return("Weaknesses: Dark, Ghost, Ground, Psychic\nResistances: Bug, Fairy, Grass, Poison\nImmunities: Fighting, Normal")
        elif owo == (d + " " + i) or owo == (i + " " + d):
           return("Weaknesses: Fire, Ground\nResistances: Normal, Grass, Ice, Flying, Bug, Rock, Dragon, Steel, Fairy\nImmunities: Poison")
        elif owo == (d + " " + j) or owo == (j + " " + d):
           return("Weaknesses: Ground, Psychic, Rock, Water\nResistances: Bug, Fairy, Fighting, Fire, Grass, Ice, Poison, Steel\nImmunities: None")
        elif owo == (d + " " + k) or owo == (k + " " + d):
           return("Weaknesses: Electric, Ground, Psychic\nResistances: Bug, Fairy, Fighting, Fire, Ice, Poison, Steel, Water\nImmunities: None")
        elif owo == (d + " " + l) or owo == (l + " " + d):
           return("Weaknesses: Fire, Flying, Ice, Psychic\nResistances: Electric, Fairy, Fighting, Grass, Water\nImmunities: None")
        elif owo == (d + " " + m) or owo == (m + " " + d):
           return("Weaknesses: Ground, Psychic\nResistances: Electric, Grass, Fighting, Poison, Flying, Bug, Steel, Fairy\nImmunities: None")
        elif owo == (d + " " + n) or owo == (n + " " + d):
           return("Weaknesses: Ground, Ghost, Dark\nResistances: Grass, Fighting, Poison, Fairy\nImmunities: None")
        elif owo == (d + " " + o) or owo == (o + " " + d):
           return("Weaknesses: Fire, Ground, Psychic, Rock, Steel\nResistances: Grass, Ice, Poison, Bug, Fairy\nImmunities: None")
        elif owo == (d + " " + p) or owo == (p + " " + d):
           return("Weaknesses: Dragon, Ground, Ice, Psychic\nResistances: Bug, Electric, Fighting, Fire, Grass, Poison, Water\nImmunities: None")
        elif owo == (d + " " + q) or owo == (q + " " + d):
           return("Weaknesses: Ground\nResistances: Dark, Ghost, Grass, Poison\nImmunities: Psychic")
        elif owo == (d + " " + r) or owo == (r + " " + d):
           return("Weaknesses: Ground, Psychic, Steel\nResistances: Grass, Fighting, Bug, Dark, Fairy\nImmunities: Dragon")
        elif owo == (e + " " + f) or owo == (f + " " + e):
           return("Weaknesses: Fighting, Grass, Ground, Ice, Steel, Water\nResistances: Fire, Flying, Normal, Poison, Rock\nImmunities: Electric")
        elif owo == (e + " " + g) or owo == (g + " " + e):
           return("Weaknesses: Fire, Flying, Ice, Water\nResistances: Fighting, Ground, Poison\nImmunities: Electric")
        elif owo == (e + " " + h) or owo == (h + " " + e):
           return("Weaknesses: Dark, Ghost, Grass, Ice, Water\nResistances: Bug, Poison, Rock\nImmunities: Electric, Fighting, Normal")
        elif owo == (e + " " + i) or owo == (i + " " + e):
           return("Weaknesses: Fighting, Fire, Ground, Water\nResistances: Bug, Dragon, Fairy, Flying, Normal, Psychic, Rock, Steel\nImmunities: Electric, Poison")
        elif owo == (e + " " + j) or owo == (j + " " + e):
           return("Weaknesses: Ground, Water\nResistances: Bug, Fairy, Fire, Poison, Steel\nImmunities: Electric")
        elif owo == (e + " " + k) or owo == (k + " " + e):
           return("Weaknesses: Grass\nResistances: Fire, Poison, Rock, Steel\nImmunities: Electric")
        elif owo == (e + " " + l) or owo == (l + " " + e):
           return("Weaknesses: Bug, Fire, Flying, Ice\nResistances: Ground, Rock\nImmunities: Electric")
        elif owo == (e + " " + m) or owo == (m + " " + e):
           return("Weaknesses: Grass, Ground, Ice, Water\nResistances: Flying, Poison, Rock, Steel\nImmunities: Electric")
        elif owo == (e + " " + n) or owo == (n + " " + e):
           return("Weaknesses: Bug, Dark, Ghost, Grass, Ice, Water\nResistances: Fighting, Poison, Psychic, Rock\nImmunities: Electric")
        elif owo == (e + " " + o) or owo == (o + " " + e):
           return("Weaknesses: Fighting, Fire, Grass, Steel, Water\nResistances: Poison\nImmunities: Electric")
        elif owo == (e + " " + p) or owo == (p + " " + e):
           return("Weaknesses: Dragon, Fairy, Ice\nResistances: Fire, Poison, Rock\nImmunities: Electric")
        elif owo == (e + " " + q) or owo == (q + " " + e):
           return("Weaknesses: Bug, Fairy, Fighting, Grass, Ice, Water\nResistances: Dark, Ghost, Poison, Rock\nImmunities: Electric, Psychic")
        elif owo == (e + " " + r) or owo == (r + " " + e):
           return("Weaknesses: Water, Grass, Ice, Steel\nResistances: Fighting, Bug, Rock, Dark\nImmunities: Electric, Dragon")
        elif owo == (f + " " + g) or owo == (g + " " + f):
           return("Weaknesses: Rock, Steel, Water\nResistances: Normal, Poison\nImmunities: None")
        elif owo == (f + " " + h) or owo == (h + " " + f):
           return("Weaknesses: Water, Grass, Ground, Ghost, Dark, Steel\nResistances: Fire, Poison, Flying, Bug\nImmunities: Normal, Fighting")
        elif owo == (f + " " + i) or owo == (i + " " + f):
           return("Weaknesses: Fighting, Ground, Water\nResistances: Bug, Dragon, Fairy, Flying, Ice, Normal, Psychic, Rock\nImmunities: Poison")
        elif owo == (f + " " + j) or owo == (j + " " + f):
           return("Weaknesses: Fighting, Ground, Rock, Water\nResistances: Bug, Fairy, Fire, Flying, Ice, Normal, Poison\nImmunities: None")
        elif owo == (f + " " + k) or owo == (k + " " + f):
           return("Weaknesses: Electric, Fighting, Grass, Ground\nResistances: Fire, Flying, Ice, Normal, Poison\nImmunities: None")
        elif owo == (f + " " + l) or owo == (l + " " + f):
           return("Weaknesses: Bug, Fighting, Ice, Steel\nResistances: Electric, Normal\nImmunities: None")
        elif owo == (f + " " + m) or owo == (m + " " + f):
           return("Weaknesses: Fighting, Grass, Ground, Water\nResistances: Electric, Fire, Flying, Normal, Poison\nImmunities: None")
        elif owo == (f + " " + n) or owo == (n + " " + f):
           return("Weaknesses: Bug, Dark, Ghost, Grass, Ground, Steel, Water\nResistances: Fire, Flying, Normal, Poison, Psychic\nImmunities: None")
        elif owo == (f + " " + o) or owo == (o + " " + f):
           return("Weaknesses: Fighting, Grass, Ground, Rock, Steel, Water\nResistances: Flying, Ice, Normal, Poison\nImmunities: None")
        elif owo == (f + " " + p) or owo == (p + " " + f):
           return("Weaknesses: Dragon, Fairy, Fighting, Ground, Ice, Steel\nResistances: Electric, Fire, Flying, Normal, Poison\nImmunities: None")
        elif owo == (f + " " + q) or owo == (q + " " + f):
           return("Weaknesses: Bug, Fairy, Fighting, Grass, Ground, Steel, Water\nResistances: Dark, Fire, Flying, Ghost, Normal, Poison\nImmunities: Psychic")
        elif owo == (f + " " + r) or owo == (r + " " + f):
           return("Weaknesses: Grass, Ground, Steel, Water\nResistances: Bug, Dark, Fire, Flying, Normal\nImmunities: Dragon")
        elif owo == (g + " " + h) or owo == (h + " " + g):
           return("Weaknesses: Dark, Fire, Flying, Ghost, Rock\nResistances: Bug, Grass, Ground, Poison\nImmunities: Fighting, Normal")
        elif owo == (g + " " + i) or owo == (i + " " + g):
           return("Weaknesses: Fire\nResistances: Bug, Dragon, Fairy, Grass, Ice, Normal, Psychic, Steel\nImmunities: Poison")
        elif owo == (g + " " + j) or owo == (j + " " + g):
           return("Weaknesses: Flying, Rock, Water\nResistances: Bug, Fairy, Fighting, Grass, Ice, Steel\nImmunities: None")
        elif owo == (g + " " + k) or owo == (k + " " + g):
           return("Weaknesses: Electric, Flying, Rock\nResistances: Fighting, Ground, Ice, Steel, Water\nImmunities: None")
        elif owo == (g + " " + l) or owo == (l + " " + g):
           return("Weaknesses: Bug, Fire, Flying, Ice, Poison, Rock\nResistances: Electric, Fighting, Grass, Ground, Water\nImmunities: None")
        elif owo == (g + " " + m) or owo == (m + " " + g):
           return("Weaknesses: Fire, Rock\nResistances: Electric, Fighting, Grass, Steel\nImmunities: None")
        elif owo == (g + " " + n) or owo == (n + " " + g):
           return("Weaknesses: Fire, Flying, Bug, Rock, Ghost, Dark\nResistances: Grass, Fighting, Ground, Psychic\nImmunities: None")
        elif owo == (g + " " + o) or owo == (o + " " + g):
           return("Weaknesses: Fire, Flying, Rock, Steel\nResistances: Grass, Ice, Ground\nImmunities: None")
        elif owo == (g + " " + p) or owo == (p + " " + g):
           return("Weaknesses: Ice, Flying, Rock, Dragon, Fairy\nResistances: Water, Electric, Fighting, Ground\nImmunities: None")
        elif owo == (g + " " + q) or owo == (q + " " + g):
           return("Weaknesses: Fire, Flying, Bug, Rock, Fairy\nResistances: Grass, Ground, Ghost, Dark\nImmunities: Psychic")
        elif owo == (g + " " + r) or owo == (r + " " + g):
           return("Weaknesses: Fire, Flying, Poison, Rock, Steel\nResistances: Bug, Dark, Fighting, Grass, Ground\nImmunities: Dragon")
        elif owo == (h + " " + i) or owo == (i + " " + h):
           return("Weaknesses: Dark, Fire, Ghost, Ground\nResistances: Bug, Dragon, Fairy, Flying, Grass, Ice, Psychic, Rock, Steel\nImmunities: Fighting, Normal, Poison")
        elif owo == (h + " " + j) or owo == (j + " " + h):
           return("Weaknesses: Dark, Ghost, Ground, Rock, Water\nResistances: Bug, Fairy, Fire, Grass, Ice, Poison, Steel\nImmunities: Fighting, Normal")
        elif owo == (h + " " + k) or owo == (k + " " + h):
           return("Weaknesses: Dark, Electric, Ghost, Grass\nResistances: Bug, Fire, Ice, Poison, Steel, Water\nImmunities: Fighting, Normal")
        elif owo == (h + " " + l) or owo == (l + " " + h):
           return("Weaknesses: Dark, Fire, Flying, Ghost, Ice\nResistances: Electric, Grass, Ground, Water\nImmunities: Fighting, Normal")
        elif owo == (h + " " + m) or owo == (m + " " + h):
           return("Weaknesses: Dark, Ghost, Ground\nResistances: Bug, Electric, Flying, Poison, Steel\nImmunities: Fighting, Normal")
        elif owo == (h + " " + n) or owo == (n + " " + h):
           return("Weaknesses: Dark, Ghost\nResistances: Poison, Psychic\nImmunities: Fighting, Normal")
        elif owo == (h + " " + o) or owo == (o + " " + h):
           return("Weaknesses: Dark, Fire, Ghost, Rock, Steel\nResistances: Bug, Ice, Poison\nImmunities: Fighting, Normal")
        elif owo == (h + " " + p) or owo == (p + " " + h):
           return("Weaknesses: Dark, Dragon, Fairy, Ghost, Ice\nResistances: Bug, Electric, Fire, Grass, Poison, Water\nImmunities: Fighting, Normal")
        elif owo == (h + " " + q) or owo == (q + " " + h):
           return("Weaknesses: Fairy\nResistances: Poison\nImmunities: Fighting, Normal, Psychic")
        elif owo == (h + " " + r) or owo == (r + " " + h):
           return("Weaknesses: Ghost, Steel\nResistances: Bug\nImmunities: Dragon, Fighting, Normal")
        elif owo == (i + " " + j) or owo == (j + " " + i):
           return("Weaknesses: Fighting, Ground, Water\nResistances: Bug, Dragon, Fairy, Flying, Grass, Ice, Normal, Psychic, Steel\nImmunities: Poison")
        elif owo == (i + " " + k) or owo == (k + " " + i):
           return("Weaknesses: Electric, Fighting, Ground\nResistances: Bug, Dragon, Fairy, Flying, Ice, Normal, Psychic, Rock, Steel, Water\nImmunities: Poison")
        elif owo == (i + " " + l) or owo == (l + " " + i):
           return("Weaknesses: Fighting, Fire\nResistances: Dragon, Electric, Fairy, Grass, Normal, Psychic, Rock, Steel, Water\nImmunities: Poison")
        elif owo == (i + " " + m) or owo == (m + " " + i):
           return("Weaknesses: Fighting, Fire, Ground\nResistances: Bug, Dragon, Electric, Fairy, Flying, Grass, Ice, Normal, Psychic, Rock, Steel\nImmunities: Poison")
        elif owo == (i + " " + n) or owo == (n + " " + i):
           return("Weaknesses: Dark, Fire, Ghost, Ground\nResistances: Dragon, Fairy, Flying, Grass, Ice, Normal, Psychic, Rock, Steel\nImmunities: Poison")
        elif owo == (i + " " + o) or owo == (o + " " + i):
           return("Weaknesses: Fighting, Fire, Ground\nResistances: Bug, Dragon, Fairy, Flying, Grass, Ice, Normal, Psychic\nImmunities: Poison")
        elif owo == (i + " " + p) or owo == (p + " " + i):
           return("Weaknesses: Fighting, Ground\nResistances: Bug, Electric, Flying, Grass, Normal, Psychic, Rock, Steel, Water\nImmunities: Poison")
        elif owo == (i + " " + q) or owo == (q + " " + i):
           return("Weaknesses: Fighting, Fire, Ground\nResistances: Dark, Dragon, Flying, Ghost, Grass, Ice, Normal, Rock, Steel\nImmunities: Poison, Psychic")
        elif owo == (i + " " + r) or owo == (r + " " + i):
           return("Weaknesses: Fire, Ground\nResistances: Bug, Dark, Fairy, Flying, Grass, Ice, Normal, Psychic, Rockl\nImmunities: Dragon, Poison")
        elif owo == (j + " " + k) or owo == (k + " " + j):
           return("Weaknesses: Electric, Ground, Rock\nResistances: Bug, Fairy, Fire, Ice, Steel\nImmunities: None")
        elif owo == (j + " " + l) or owo == (l + " " + j):
           return("Weaknesses: Poison, Flying, Rock\nResistances: Electric, Grass, Steel, Fairy\nImmunities: None")
        elif owo == (j + " " + m) or owo == (m + " " + j):
           return("Weaknesses: Ground, Rock, Water\nResistances: Bug, Electric, Fairy, Fire, Flying, Grass, Ice, Steel\nImmunities: None")
        elif owo == (j + " " + n) or owo == (n + " " + j):
           return("Weaknesses: Dark, Ghost, Ground, Rock, Water\nResistances: Fairy, Fighting, Fire, Grass, Ice, Psychic, Steel\nImmunities: None")
        elif owo == (j + " " + o) or owo == (o + " " + j):
           return("Weaknesses: Water, Fighting, Ground, Rock\nResistances: Grass, Ice, Bug, Fairy\nImmunities: None")
        elif owo == (j + " " + p) or owo == (p + " " + j):
           return("Weaknesses: Dragon, Ground, Rock\nResistances: Bug, Electric, Fire, Grass, Steel\nImmunities: None")
        elif owo == (j + " " + q) or owo == (q + " " + j):
           return("Weaknesses: Fighting, Ground, Rock, Water\nResistances: Dark, Fire, Ghost, Grass, Ice, Steel\nImmunities: Psychic")
        elif owo == (j + " " + r) or owo == (r + " " + j):
           return("Weaknesses: Water, Poison, Ground, Rock\nResistances: Fire, Grass, Ice, Fighting, Bug, Dark, Fairy\nImmunities: Dragon")
        elif owo == (k + " " + l) or owo == (l + " " + k):
           return("Weaknesses: Bug, Flying, Poison\nResistances: Ground, Steel, Water\nImmunities: None")
        elif owo == (k + " " + m) or owo == (m + " " + k):
           return("Weaknesses: Grass, Ground\nResistances: Fire, Flying, Ice, Steel, Water\nImmunities: None")
        elif owo == (k + " " + n) or owo == (n + " " + k):
           return("Weaknesses: Bug, Dark, Electric, Ghost, Grass\nResistances: Fighting, Fire, Ice, Psychic, Steel, Water\nImmunities: None")
        elif owo == (k + " " + o) or owo == (o + " " + k):
           return("Weaknesses: Electric, Fighting, Grass, Rock\nResistances: Ice, Water\nImmunities: None")
        elif owo == (k + " " + p) or owo == (p + " " + k):
           return("Weaknesses: Dragon, Fairy\nResistances: Fire, Steel, Water\nImmunities: None")
        elif owo == (k + " " + q) or owo == (q + " " + k):
           return("Weaknesses: Bug, Electric, Fairy, Fighting, Grass\nResistances: Dark, Fire, Ghost, Ice, Steel, Water\nImmunities: Psychic")
        elif owo == (k + " " + r) or owo == (r + " " + k):
           return("Weaknesses: Electric, Grass, Poison\nResistances: Bug, Dark, Fighting, Fire, Ice, Water\nImmunities: Dragon")
        elif owo == (l + " " + m) or owo == (m + " " + l):
           return("Weaknesses: Bug, Fire, Ice, Poison\nResistances: Electric, Grass, Steel, Water\nImmunities: None")
        elif owo == (l + " " + n) or owo == (n + " " + l):
           return("Weaknesses: Bug, Dark, Fire, Flying, Ghost, Ice, Poison\nResistances: Electric, Fighting, Grass, Ground, Psychic, Water\nImmunities: None")
        elif owo == (l + " " + o) or owo == (o + " " + l):
           return("Weaknesses: Bug, Fighting, Fire, Flying, Poison, Rock, Steel\nResistances: Electric, Grass, Ground, Water\nImmunities: None")
        elif owo == (l + " " + p) or owo == (p + " " + l):
           return("Weaknesses: Bug, Dragon, Fairy, Flying, Ice, Poison\nResistances: Electric, Grass, Ground, Water\nImmunities: None")
        elif owo == (l + " " + q) or owo == (q + " " + l):
           return("Weaknesses: Bug, Fairy, Fighting, Fire, Flying, Ice, Poison\nResistances: Dark, Electric, Ghost, Grass, Ground, Water\nImmunities: Psychic")
        elif owo == (l + " " + r) or owo == (r + " " + l):
           return("Weaknesses: Fire, Flying, Ice, Poison, Steel\nResistances: Dark, Electric, Fighting, Grass, Ground, Water\nImmunities: Dragon")
        elif owo == (m + " " + n) or owo == (n + " " + m):
           return("Weaknesses: Bug, Dark, Ghost, Ground\nResistances: Electric, Fighting, Flying, Psychic, Steel\nImmunities: None")
        elif owo == (m + " " + o) or owo == (o + " " + m):
           return("Weaknesses: Fighting, Fire, Ground, Rock\nResistances: Electric, Flying, Ice\nImmunities: None")
        elif owo == (m + " " + p) or owo == (p + " " + m):
           return("Weaknesses: Dragon, Fairy, Ground, Ice\nResistances: Electric, Fire, Flying, Grass, Steel, Water\nImmunities: None")
        elif owo == (m + " " + q) or owo == (q + " " + m):
           return("Weaknesses: Fighting, Ground, Bug, Fairy\nResistances: Electric, Flying, Ghost, Dark\nImmunities: Psychic")
        elif owo == (m + " " + r) or owo == (r + " " + m):
           return("Weaknesses: Ground, Poison\nResistances: Bug, Dark, Electric, Fighting, Flying\nImmunities: Dragon")
        elif owo == (n + " " + o) or owo == (o + " " + n):
           return("Weaknesses: Bug, Dark, Fire, Ghost, Rock, Steel\nResistances: Ice, Psychic\nImmunities: None")
        elif owo == (n + " " + p) or owo == (p + " " + n):
           return("Weaknesses: Bug, Dark, Dragon, Fairy, Ghost, Ice\nResistances: Electric, Fighting, Fire, Grass, Psychic, Water\nImmunities: None")
        elif owo == (n + " " + q) or owo == (q + " " + n):
           return("Weaknesses: Bug, Fairy\nResistances: None\nImmunities: Psychic")
        elif owo == (n + " " + r) or owo == (r + " " + n):
           return("Weaknesses: Ghost, Poison, Steel\nResistances: Fighting, Psychic\nImmunities: Dragon")
        elif owo == (o + " " + p) or owo == (p + " " + o):
           return("Weaknesses: Dragon, Fairy, Fighting, Rock, Steel\nResistances: Electric, Grass, Water\nImmunities: None")
        elif owo == (o + " " + q) or owo == (q + " " + o):
           return("Weaknesses: Bug, Fairy, Fighting, Fire, Rock, Steel\nResistances: Dark, Ghost, Ice\nImmunities: Psychic")
        elif owo == (o + " " + r) or owo == (r + " " + o):
           return("Weaknesses: Fire, Poison, Rock, Steel\nResistances: Bug, Dark, Ice\nImmunities: Dragon")
        elif owo == (p + " " + q) or owo == (q + " " + p):
           return("Weaknesses: Bug, Dragon, Fairy, Fighting, Ice\nResistances: Dark, Electric, Fire, Ghost, Grass, Water\nImmunities: Psychic")
        elif owo == (p + " " + r) or owo == (r + " " + p):
           return("Weaknesses: Fairy, Ice, Poison, Steel\nResistances: Bug, Dark, Electric, Fighting, Fire, Grass, Water\nImmunities: Dragon")
        elif owo == (q + " " + r) or owo == (r + " " + q):
           return("Weaknesses: Poison, Steel, Fairy\nResistances: Ghost, Dark\nImmunities: Psychic, Dragon")
        count = 1

@bot.event
async def on_ready():
    print('Bot is ready')

df = refresh_data()

class PokedexMenu(commands.Cog):
    def __init__(self, bot, ctx, entries, currentIndex):
        self.bot = bot
        self.ctx = ctx
        self.entries = entries
        #self.current_entry_index = 0
        print("TEST" + str(currentIndex))
        self.current_entry_index = currentIndex
        print(self.current_entry_index)
        self.message = None

    async def send_entry(self):
        print(f"Sending entry at index {self.current_entry_index}")
        print(self.entries)
        entry = self.entries[self.current_entry_index]
        print(f"Entry data: {entry}")

        if pd.isna(entry['ImageName']):  # Check if 'ImageName' is NaN
            image_path = os.path.join("C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDexImages", "DefaultImage.png")  # Adjust the name if necessary
        else:
            image_path = os.path.join("C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDexImages", entry['ImageName'])

        embed = discord.Embed(title=f"\\\\\\\\\\\\\\\\\\[ENTRY {entry['Dex Entry']}]\\\\\\\\\\\\\\\\\\")
        if os.path.isfile(image_path):
            file = discord.File(image_path, filename=os.path.basename(image_path))  # filename is taken from the image_path
            embed.set_image(url=f"attachment://{os.path.basename(image_path)}")  # Adjust the name if necessary
        else:
            default_image_path = os.path.join("C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDexImages", "DefaultImage.png")  # Adjust the name if necessary
            default_file = discord.File(default_image_path, filename="DefaultImage.png")  # Adjust the name if necessary
            embed.set_image(url=f"attachment://DefaultImage.png")  # Adjust the name if necessary

        embed.add_field(name="Entry", value=entry['Dex Entry'])
        embed.add_field(name="Name", value=entry['Name'])
        embed.add_field(name="Type", value=format_type_displayForDex(entry))
        embed.add_field(name="Rarity", value=entry['Rarity'])
        embed.add_field(name="Abilities", value=entry['Abilities'])
        embed.add_field(name="Evolves", value=entry['Evolves'])
        embed.add_field(name="Location", value=entry['Location'])
        embed.add_field(name="Notes", value=entry['Notes'])
        embed.add_field(name="Indexed By", value=entry['Indexed'])
        print(entry['Type3'])
        if entry['Type3'] == entry['Type3']:
            print("ONE")
            testing = FindDuoWeakness(entry['Type2'],entry['Type1'])
            embed.add_field(name="WRI", value=testing)
            embed.add_field(name="WRI2", value=FindDuoWeakness(entry['Type3'],entry['Type1']))
        elif entry['Type2'] == entry['Type2']:
            print("TWO")
            testing = FindDuoWeakness(entry['Type2'],entry['Type1'])
            print(entry['Type2'])
            print(testing)
            embed.add_field(name="WRI", value=testing)
        else:
           print("THREE")
           embed.add_field(name="WRI2", value=FindMonoWeakness(entry['Type1']))

        if os.path.isfile(image_path):
            if self.message:
                await self.message.delete()
            self.message = await self.ctx.send(file=file, embed=embed)
        else:
            if self.message:
                await self.message.delete()
            self.message = await self.ctx.send(file=default_file, embed=embed)

        if len(self.entries) > 1:
            await self.message.add_reaction("⬅️")  # Previous reaction
            await self.message.add_reaction("➡️")  # Next reaction


    

    async def next_entry(self):
        if self.current_entry_index < len(self.entries) - 1:
            self.current_entry_index += 1

    async def previous_entry(self):
        if self.current_entry_index > 0:
            self.current_entry_index -= 1

    async def update_message(self):
        # Delete the old message if it exists
        if self.message:
            await self.message.delete()

        # Send the new message and save it to self.message
        self.message = await self.ctx.send(file=file, embed=embed)

        # If there's more than one entry, add reactions to the message
        if len(self.entries) > 1:
            await self.message.add_reaction("⬅️")  # Previous reaction
            await self.message.add_reaction("➡️")  # Next reaction

    async def remove_reaction(self, reaction, user):
        try:
            await self.message.remove_reaction(reaction, user)
        except Exception as e:
            print(f"Couldn't remove reaction: {e}")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id != self.bot.user.id:
            emoji = str(reaction.emoji)
            if emoji == '➡️':
                self.current_entry_index = (self.current_entry_index + 1) % len(self.entries)  # Wrap around to the start if at the end
            elif emoji == '⬅️':
                self.current_entry_index = self.current_entry_index - 1 if self.current_entry_index > 0 else len(self.entries) - 1  # Wrap around to the end if at the start
            await self.send_entry()
            await reaction.remove(user)


    
    
@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id or isinstance(payload.channel_id, discord.DMChannel):
        return

    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = bot.get_user(payload.user_id)
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if member:
        ctx = await bot.get_context(message, cls=commands.Context)
        ctx.author = member
        ctx.user = user
        await bot.invoke(ctx)

    menu = menus.get(payload.channel_id)  # get the menu instance for this channel
    if not menu:  # if no menu, just return
        return
    
    if str(payload.emoji) == '⬅️':
        await menu.previous_entry()
    elif str(payload.emoji) == '➡️':
        await menu.next_entry()
    else:
        return

    await menu.remove_reaction(str(payload.emoji), bot.get_user(payload.user_id))
    await menu.send_entry()


menus = {}


@bot.command()
async def pokedex(ctx, *, pokemon_name: str):
    df = refresh_data()
    try:
        start_entry = int(pokemon_name)
        # Ensure the start entry is within the valid range
        if start_entry < 1 or start_entry > len(df):
            await ctx.send(f"Entry {start_entry} does not exist.")
            return

        start_index = start_entry - 1
        currentIndex = start_index
        print("START INT" + str(start_index))
        start_index = 0
        entries = df[int(start_index):].to_dict(orient='records')

    except ValueError:
        print(pokemon_name)
        row = df.loc[df['Name'].str.strip().str.lower() == pokemon_name.strip().lower()]
        print(pokemon_name.strip().lower())
       
        if row.empty:
            matches = process.extract(pokemon_name.lower(), df['Name'].str.lower(), limit=5)
            matched_names = " or ".join([f"{i+1}. {match[0]}" for i, match in enumerate(matches)])
            await ctx.send(f"No exact match found. Did you mean {matched_names}?")
            return
        print(row)
        currentIndex = row.index[0]
        print("START STRING" + str(currentIndex))
        start_index = 0
        entries = df[start_index:].to_dict(orient='records')

    menu = PokedexMenu(bot, ctx, entries, currentIndex)
    menus[ctx.channel.id] = menu  # save menu instance for this channel
    await menu.send_entry()
    
class ShinyDexMenu(commands.Cog):
    def __init__(self, bot, ctx, entries, currentIndex):
        self.bot = bot
        self.ctx = ctx
        self.entries = entries
        self.current_entry_index = currentIndex
        self.message = None

    async def send_entry(self):
        print(f"Sending entry at index {self.current_entry_index}")
        print(self.entries)
        entry = self.entries[self.current_entry_index]
        print(f"Entry data: {entry}")

        if pd.isna(entry['ShinyImageName']):  # Check if 'ImageShinyName' is NaN
            image_path = os.path.join("C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDexImages", "DefaultImage.png")
        else:
            image_path = os.path.join("C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDexImages", entry['ShinyImageName'])

        embed = discord.Embed(title=f"\\\\\\\\\\\\\\\\\\[ENTRY {entry['Dex Entry']}]\\\\\\\\\\\\\\\\\\")
        if os.path.isfile(image_path):
            file = discord.File(image_path, filename=os.path.basename(image_path))
            embed.set_image(url=f"attachment://{os.path.basename(image_path)}")
        else:
            default_image_path = os.path.join("C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDexImages", "DefaultImage.png")
            default_file = discord.File(default_image_path, filename="DefaultImage.png")
            embed.set_image(url=f"attachment://DefaultImage.png")

        embed.add_field(name="Entry", value=entry['Dex Entry'])
        embed.add_field(name="Name", value=entry['Name'])
        embed.add_field(name="Type", value=format_type_displayForDex(entry))
        embed.add_field(name="Rarity", value=entry['Rarity'])
        embed.add_field(name="Abilities", value=entry['Abilities'])
        embed.add_field(name="Evolves", value=entry['Evolves'])
        embed.add_field(name="Location", value=entry['Location'])
        embed.add_field(name="Notes", value=entry['Notes'])
        embed.add_field(name="Indexed By", value=entry['ShinyIndexed'])  # Changed to 'ShinyIndexed'

        if os.path.isfile(image_path):
            if self.message:
                await self.message.delete()
            self.message = await self.ctx.send(file=file, embed=embed)
        else:
            if self.message:
                await self.message.delete()
            self.message = await self.ctx.send(file=default_file, embed=embed)

        if len(self.entries) > 1:
            await self.message.add_reaction("⬅️")
            await self.message.add_reaction("➡️")

    #... The rest of the ShinyDexMenu class functions (they remain unchanged) ...

@bot.command()
async def shinydex(ctx, *, pokemon_name: str):
    df = refresh_data()

    try:
        start_entry = int(pokemon_name)
        if start_entry < 1 or start_entry > len(df):
            await ctx.send(f"Entry {start_entry} does not exist.")
            return

        start_index = start_entry - 1
        currentIndex = start_index
        print("START INT" + str(start_index))
        start_index = 0
        entries = df[int(start_index):].to_dict(orient='records')

    except ValueError:
        print(pokemon_name)
        row = df.loc[df['Name'].str.strip().str.lower() == pokemon_name.strip().lower()]
        print(pokemon_name.strip().lower())
       
        if row.empty:
            matches = process.extract(pokemon_name.lower(), df['Name'].str.lower(), limit=5)
            matched_names = " or ".join([f"{i+1}. {match[0]}" for i, match in enumerate(matches)])
            await ctx.send(f"No exact match found. Did you mean {matched_names}?")
            return
        print(row)
        currentIndex = row.index[0]
        print("START STRING" + str(currentIndex))
        start_index = 0
        entries = df[start_index:].to_dict(orient='records')

    menu = ShinyDexMenu(bot, ctx, entries, currentIndex)  # Changed to ShinyDexMenu
    menus[ctx.channel.id] = menu
    await menu.send_entry()




@bot.event
async def on_command_completion(ctx):
    print(f"Command {ctx.command} used by {ctx.author}")


import shutil

import os

@bot.command()
async def Moves(ctx, *, Pokename: str):
    df = refresh_data()

    if df.loc[df['Name'].str.lower() == Pokename.lower()].empty:
        await ctx.send(f"No Pokemon named {Pokename} found.")
        return

    if 'Moves' not in df.columns:
        await ctx.send(f"No 'Moves' attribute found.")
        return

    moves = df.loc[df['Name'].str.lower() == Pokename.lower(), 'Moves'].values[0]

    await ctx.send(f"The moves for {Pokename} are: {moves}")


@bot.command()
async def Basestats(ctx, *, Pokename: str):
    df = refresh_data()

    if df.loc[df['Name'].str.lower() == Pokename.lower()].empty:
        await ctx.send(f"No Pokemon named {Pokename} found.")
        return

    if 'Basestats' not in df.columns:
        await ctx.send(f"No 'Basestats' attribute found.")
        return

    base_stats_string = df.loc[df['Name'].str.lower() == Pokename.lower(), 'Basestats'].values[0]

    # Parse the base stats string into a dictionary
    base_stats = parse_basestats(base_stats_string)

    # Calculate the total of all base stats
    total_base_stats = sum(base_stats.values())

    await ctx.send(f"The Base-Stats for {Pokename} are: {base_stats}, with a BST     of: {total_base_stats}")


    
   

import re

@bot.command()
async def PokeEdit(ctx, *, args: str):
    # Regular expression to match the name, attribute, and new value
    regex = r'"([^"]*)"\s+"([^"]*)"\s+"([^"]*)"'
    match = re.search(regex, args)

    if not match:
        await ctx.send("Invalid command format. Use: !PokeEdit \"Pokename\" \"attribute\" \"new_value\"")
        return

    Pokename, attribute, new_value = match.groups()

    df = refresh_data()

    if df.loc[df['Name'].str.lower() == Pokename.lower()].empty:
        await ctx.send(f"No Pokemon named {Pokename} found.")
        return

    if attribute not in df.columns:
        await ctx.send(f"No attribute named {attribute} found.")
        return

    # If attribute is 'Moves', split new_value by commas and then join them back into a string
    if attribute.lower() == 'moves':
        new_value = ', '.join([move.strip() for move in new_value.split(',')])

    df.loc[df['Name'].str.lower() == Pokename.lower(), attribute] = new_value

    if attribute.lower() == 'name':
        old_image_path = os.path.join('C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDexImages', Pokename + '.png')
        new_image_path = os.path.join('C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDexImages', new_value + '.png')

        if os.path.exists(old_image_path):
            os.rename(old_image_path, new_image_path)
        else:
            await ctx.send(f"No image found for {Pokename}. No image was renamed.")

        df.loc[df['Name'].str.lower() == new_value.lower(), 'ImageName'] = new_value + '.png'

    df.to_excel(EXCEL_FILE_PATH, index=False)

    await ctx.send(f"Updated the '{attribute}' field for {Pokename} to {new_value}.")

def parse_basestats(basestats):
    if pd.isnull(basestats):
        return {}
    stats_dict = {}
    for stat in basestats.split(','):
        key, val = [s.strip() for s in stat.split(':')]
        stats_dict[key] = int(val)
    return stats_dict

@bot.command()
async def Topstats(ctx, stat_type: str, top_n: int):
    df = refresh_data()
    stat_type = stat_type.lower()
    df['Basestats'] = df['Basestats'].apply(parse_basestats)

    # Calculate 'BST' for all Pokemon
    df['BST'] = df['Basestats'].apply(lambda stats: sum(stats.values()) if stats else None)

    if stat_type != 'bst':
        df = df[df['Basestats'].apply(lambda stats: bool(stats) and stat_type in stats)]
        if df.empty:
            await ctx.send(f"No Pokemon with the stat '{stat_type}' found.")
            return
        # Add stat_type column to dataframe
        df[stat_type] = df['Basestats'].apply(lambda stats: stats[stat_type] if stat_type in stats else 0)
        # Get top_n pokemon based on stat_type
        stat_data = df.sort_values(by=stat_type, ascending=False).head(top_n)
        output = '\n'.join([f"{row['Name']}: {row[stat_type]}" for _, row in stat_data.iterrows()])
    else:
        # If 'bst' is the requested stat_type, sort by 'BST'
        stat_data = df.sort_values(by='BST', ascending=False).head(top_n)
        output = '\n'.join([f"{row['Name']}: {row['BST']}" for _, row in stat_data.iterrows()])

    await ctx.send(output)

@bot.command()
async def EVyield(ctx, *, Pokename: str):
    df = refresh_data()

    if df.loc[df['Name'].str.lower() == Pokename.lower()].empty:
        await ctx.send(f"No Pokemon named {Pokename} found.")
        return

    if 'EVYield' not in df.columns:
        await ctx.send(f"No 'EVYield' attribute found.")
        return

    ev_yield = df.loc[df['Name'].str.lower() == Pokename.lower(), 'EVYield'].values[0]

    await ctx.send(f"The EV Yield for {Pokename} is: {ev_yield}")

@bot.command()
async def EV(ctx, ev_type: str, top_n: int):
    df = refresh_data()
    ev_type = ev_type.lower()
    df['EVYield'] = df['EVYield'].apply(parse_basestats)

    df = df[df['EVYield'].apply(lambda evs: bool(evs) and ev_type in evs)]
    if df.empty:
        await ctx.send(f"No Pokemon with the EV '{ev_type}' found.")
        return

    # Add ev_type column to dataframe
    df[ev_type] = df['EVYield'].apply(lambda evs: evs[ev_type] if ev_type in evs else 0)
    # Get top_n pokemon based on ev_type
    ev_data = df.sort_values(by=ev_type, ascending=False).head(top_n)
    output = '\n'.join([f"{row['Name']}: {row[ev_type]}" for _, row in ev_data.iterrows()])

    await ctx.send(output)






@bot.command()
async def CanLearn(ctx, *, movename: str):
    df = refresh_data()

    if 'Moves' not in df.columns:
        await ctx.send("No 'Moves' attribute found.")
        return

    # Check if moves is a string and contains ':' before splitting
    matching_pokemon = df[df['Moves'].apply(lambda moves: any(movename.lower() in move.split(":")[1].lower() for move in moves.split(", ") if ':' in move) if isinstance(moves, str) else False)]

    if matching_pokemon.empty:
        await ctx.send(f"No Pokemon can learn {movename}.")
    else:
        pokemon_names = matching_pokemon['Name'].tolist()
        await ctx.send(f"Pokemon that can learn {movename} are: {', '.join(pokemon_names)}")




@bot.command()
async def PokeSubmit(ctx, *, args: str):
    # Regular expression to match the Pokemon name and indexed_by_name
    regex = r'"([^"]*)"\s+"([^"]*)"'
    match = re.search(regex, args)

    if not match:
        await ctx.send("Invalid command format. Use: !PokeSubmit \"Pokename\" \"indexed_by_name\"")
        return

    Pokename, indexed_by_name = match.groups()
    df = refresh_data()

    if not df.loc[df['Name'].str.lower() == Pokename.lower()].empty:
        # Update the 'Indexed' field for the existing Pokemon
        df.loc[df['Name'].str.lower() == Pokename.lower(), 'Indexed'] = indexed_by_name.capitalize()

        # Handle image if exists
        if ctx.message.attachments:
            # We'll assume that the first attachment is the image
            attachment = ctx.message.attachments[0]

            # Construct the path where we'll save the image
            save_path = os.path.join(r'F:\CobbleDexImages', Pokename + '.png')

            try:
                # Save the image to the constructed path
                await attachment.save(save_path)
                # Update 'ImageName' in the DataFrame
                df.loc[df['Name'].str.lower() == Pokename.lower(), 'ImageName'] = Pokename + '.png'
                await ctx.send(f"Updated the 'Indexed By' field for {Pokename} to {indexed_by_name.capitalize()} and updated image.")
            except Exception as e:
                await ctx.send(f"Failed to save the image due to the following error: {e}")
        else:
            await ctx.send(f"Updated the 'Indexed By' field for {Pokename} to {indexed_by_name.capitalize()}. No image was attached.")

        df.to_excel(EXCEL_FILE_PATH, index=False)  # Save the updated DataFrame back to the Excel file
        return




    # If we're here, that means no existing Pokemon was found
    # Calculate new index and entry number
    last_index = df['Index'].max() if not df['Index'].empty else 0
    new_index = last_index + 1
    new_entry_number = f'#{new_index:04d}'

    # So, we'll create a new row and append it to the DataFrame
    new_row = {'Name': Pokename, 'Indexed': indexed_by_name.capitalize(), 'ImageName': Pokename + '.png', 'Index': new_index, 'Dex Entry': new_entry_number}
    new_df = pd.DataFrame([new_row])  # Create a new DataFrame from the new_row dictionary
    df = pd.concat([df, new_df], ignore_index=True)  # Concatenate the new DataFrame with the old one

    df.to_excel(EXCEL_FILE_PATH, index=False)  # Save the updated DataFrame back to the Excel file

    # Now, we'll save the submitted image to the appropriate folder
    if ctx.message.attachments:
        # We'll assume that the first attachment is the image
        attachment = ctx.message.attachments[0]

        # Construct the path where we'll save the image
        save_path = os.path.join(r'F:\CobbleDexImages', Pokename + '.png')

        # Save the image to the constructed path
        await attachment.save(save_path)

        await ctx.send(f"Added new Pokemon {Pokename} indexed by {indexed_by_name.capitalize()} with image saved to DexImage folder")
    else:
        await ctx.send("No image was attached.")



@bot.command()
async def ShinySubmit(ctx, *, args: str):
    # Regular expression to match the Pokemon name and indexed_by_name
    regex = r'"([^"]*)"\s+"([^"]*)"'
    match = re.search(regex, args)

    if not match:
        await ctx.send("Invalid command format. Use: !ShinySubmit \"Pokename\" \"indexed_by_name\"")
        return

    Pokename, indexed_by_name = match.groups()
    df = refresh_data()

    if not df.loc[df['Name'].str.lower() == Pokename.lower()].empty:
        # Update the 'ShinyIndexed' field for the existing Pokemon
        df.loc[df['Name'].str.lower() == Pokename.lower(), 'ShinyIndexed'] = indexed_by_name.capitalize()

        # Handle image if exists
        if ctx.message.attachments:
            # We'll assume that the first attachment is the image
            attachment = ctx.message.attachments[0]

            # Construct the path where we'll save the image
            save_path = os.path.join(r'F:\CobbleDexImages', 'Shiny' + Pokename + '.png')

            try:
                # Save the image to the constructed path
                await attachment.save(save_path)
                await ctx.send(f"Updated the 'ShinyIndexed By' field for {Pokename} to {indexed_by_name.capitalize()} and updated shiny image.")
            except Exception as e:
                await ctx.send(f"Failed to save the shiny image due to the following error: {e}")

            df.loc[df['Name'].str.lower() == Pokename.lower(), 'ShinyImageName'] = 'Shiny' + Pokename + '.png'

        else:
            await ctx.send(f"Updated the 'ShinyIndexed By' field for {Pokename} to {indexed_by_name.capitalize()}. No shiny image was attached.")

    else:
        # If we're here, that means no existing Pokemon was found
        # Calculate new index and entry number
        last_index = df['Index'].max() if not df['Index'].empty else 0
        new_index = last_index + 1
        new_entry_number = f'#{new_index:04d}'

        # So, we'll create a new row and append it to the DataFrame
        new_row = {'Name': Pokename, 'ShinyIndexed': indexed_by_name.capitalize(), 'ShinyImageName': 'Shiny' + Pokename + '.png', 'Index': new_index, 'Dex Entry': new_entry_number}
        new_df = pd.DataFrame([new_row])  # Create a new DataFrame from the new_row dictionary
        df = pd.concat([df, new_df], ignore_index=True)  # Concatenate the new DataFrame with the old one

        # Handle image if exists
        if ctx.message.attachments:
            # We'll assume that the first attachment is the image
            attachment = ctx.message.attachments[0]

            # Construct the path where we'll save the image
            save_path = os.path.join(r'F:\CobbleDexImages', 'Shiny' + Pokename + '.png')

            try:
                # Save the image to the constructed path
                await attachment.save(save_path)
                await ctx.send(f"Added new Pokemon {Pokename} shiny indexed by {indexed_by_name.capitalize()} with shiny image saved to DexImage folder")
            except Exception as e:
                await ctx.send(f"Failed to save the shiny image due to the following error: {e}")
        else:
            await ctx.send(f"Added new Pokemon {Pokename} shiny indexed by {indexed_by_name.capitalize()}. No shiny image was attached.")

    df.to_excel(EXCEL_FILE_PATH, index=False)  # Save the updated DataFrame back to the Excel file



def format_type_displayForDex(entry):
    types = [entry['Type1'], entry['Type2'], entry['Type3']]
    types = [type_ for type_ in types if type_ is not np.nan]  # Remove nan values
    if len(types) == 1:
        return types[0]
    elif len(types) == 2:
        return types[0] + ', ' + types[1]
    elif len(types) == 3:
        return types[0] + ', ' + types[1] + ' or ' + types[0] + ', ' + types[2]


def format_type_display(row):
    type1 = ""
    type2 = ""
    
    if isinstance(row, dict):
        type1 = row['Type1'] if 'Type1' in row else ""
        type2 = row['Type2'] if 'Type2' in row else ""
    elif isinstance(row, pd.DataFrame) or isinstance(row, pd.Series):
        type1 = row['Type1'].values[0] if not pd.isna(row['Type1'].values[0]) else ""
        type2 = row['Type2'].values[0] if not pd.isna(row['Type2'].values[0]) else ""
    else:
        raise ValueError("Row should be a DataFrame, a Series, or a dictionary.")
    
    if type1 == "" and type2 == "":
        return "Unknown"
    elif type1 != "" and type2 != "":
        return f"{type1}, {type2}"
    else:
        return type1 if type1 != "" else type2

import time
@bot.command()
async def Weakness(ctx, *args):
    test = [arg.lower() for arg in args]
    print(test)
    if len(test) > 1:
        chosentype = test[1] + " " + test[0]
        await ctx.send(FindDuoWeakness(test[1],test[0]))
    else:
        chosentype = test[0]
        await ctx.send(FindMonoWeakness(chosentype))

    


    
       
        


        

@bot.command()
async def Typefind(ctx, *args):
    df = refresh_data()
    types = [arg.lower() for arg in args]

    if len(types) == 1:
        filtered_df = df[(df['Type1'].str.lower() == types[0]) |
                         (df['Type2'].str.lower() == types[0]) |
                         (df['Type3'].str.lower() == types[0])]
    else:
        # Check for the presence of both types in either order (Type1 and Type2, or Type1 and Type3)
        filtered_df = df[((df['Type1'].str.lower() == types[0]) & (df['Type2'].str.lower() == types[1])) |
                         ((df['Type1'].str.lower() == types[1]) & (df['Type2'].str.lower() == types[0])) |
                         ((df['Type1'].str.lower() == types[0]) & (df['Type3'].str.lower() == types[1])) |
                         ((df['Type1'].str.lower() == types[1]) & (df['Type3'].str.lower() == types[0]))]

    if not filtered_df.empty:
        pokemon_list = filtered_df['Name'].tolist()
        capitalized_types = [type.capitalize() for type in types]
        await ctx.send(f"Pokémon with type(s) {', '.join(capitalized_types)}: {', '.join(pokemon_list)}")
    else:
        await ctx.send(f"Could not find specified type.")

@bot.command()
async def Shinies(ctx):
    df = refresh_data()

    # Filter rows where 'ShinyIndexed' is not null or empty
    shiny_indexed_pokemon = df[df['ShinyIndexed'].notna() & df['ShinyIndexed'].str.strip().ne('')]

    message = "Shiny Indexed Pokémon:\n"
    for _, pokemon in shiny_indexed_pokemon.iterrows():
        message += f"{pokemon['Name']} (Indexed by {pokemon['ShinyIndexed']})\n"

    if not shiny_indexed_pokemon.empty:
        await ctx.send(message)
    else:
        await ctx.send("No Shiny Indexed Pokémon found.")


@bot.command()
async def CountShinyIndexed(ctx):
    df = refresh_data()

    indexed_counts = df['ShinyIndexed'].value_counts()

    message = "Shiny Indexed Occurrences:\n"
    for idx, count in indexed_counts.items():
        message += f"{idx}: {count} Shiny Indexed Pokémon\n"

    total = indexed_counts.sum()
    message += f"\nTotal Shiny Indexed Pokémon: {total}"

    await ctx.send(message)


@bot.command()
async def CountIndexed(ctx):
    df = refresh_data()

    indexed_counts = df['Indexed'].value_counts()

    message = "Indexed Occurrences:\n"
    for idx, count in indexed_counts.items():
        message += f"{idx}: {count} Indexed Pokémon\n"

    total = indexed_counts.sum()
    message += f"\nTotal Indexed Pokémon: {total}"

    await ctx.send(message)

@bot.command()
async def CountTypes(ctx):
    df = refresh_data()

    # Single types
    type1_counts = df['Type1'].value_counts()
    type2_counts = df['Type2'].value_counts()
    type3_counts = df['Type3'].value_counts()
    single_types_counts = type1_counts.add(type2_counts, fill_value=0).add(type3_counts, fill_value=0)

    message = "Single Type Occurrences:\n" + ', '.join(f"{t}: {c}" for t, c in single_types_counts.items())

  

   
   

    # Add the double type counts to the message
   

    # Calculate and print the total occurrences
    total_counts = single_types_counts.sum()
    message += f"\n\nTotal Occurrences: {total_counts}"

    await ctx.send(message)

@bot.command()
async def CountDTypes(ctx):
    df = refresh_data()

    message = ""
        # Double types
    double_types_counts1 = df.groupby(['Type1', 'Type2']).size()
    double_types_counts2 = df.groupby(['Type2', 'Type1']).size()
    double_types_counts3 = df.groupby(['Type1', 'Type3']).size()
    double_types_counts4 = df.groupby(['Type3', 'Type1']).size()

    # Add all double type counts together, treating (Type1, Type2) the same as (Type2, Type1), etc.
    double_types_counts = double_types_counts1.add(double_types_counts2, fill_value=0)\
                                             .add(double_types_counts3, fill_value=0)\
                                             .add(double_types_counts4, fill_value=0).reset_index()

    # Sort the types in alphabetical order for display
    double_types_counts['types'] = double_types_counts[['Type1', 'Type2']].apply(lambda x: sorted(x), axis=1)

    # Convert the list back to a string with the types separated by a comma
    double_types_counts['types'] = double_types_counts['types'].apply(lambda x: ', '.join(x))

    # Sort the data frame by the 'types' column and reset the index
    double_types_counts = double_types_counts.sort_values(by='types').reset_index(drop=True)

    # Add the double type counts to the message
    message += "\n\nDouble Type Occurrences:\n" + ', '.join(f"{row['types']}: {row[0]}" for _, row in double_types_counts.iterrows())

    # Calculate and print the total occurrences
    total_counts = double_types_counts[0].sum()
    message += f"\n\nTotal Occurrences: {total_counts}"

    await ctx.send(message)



@bot.command()
async def Pokehelp(ctx):
    embed = discord.Embed(title="Bot Commands", description="These are the available commands for this bot.")
    embed.add_field(name="!Pokedex [page number] or [pokemon name]", value="View a page of the Pokédex where you can flip through Pokedex Pages with reactions.")
    embed.add_field(name="!Shinies", value="List all Shiny Indexed Pokémon.")
    embed.add_field(name="!CountIndexed", value="Count the number of Pokémon indexed by each name.")
    embed.add_field(name="!CountShinyIndexed", value="Count the number of Shiny Indexed Pokémon.")
    embed.add_field(name="!Typefind [type1] [type2]", value="Find all Pokémon that have the specified types.")
    embed.add_field(name="!CountTypes", value="Count the number of occurrences of each single and double type.")
    embed.add_field(name="!PokeSubmit \"Pokename\" \"indexed_by_name\"", value="Submit a new Pokémon to the Pokédex.")
    embed.add_field(name="!ShinySubmit \"Pokename\" \"indexed_by_name\"", value="Submit a new Shiny Pokémon to the Pokédex.")
    embed.add_field(name="!PokeEdit \"Pokename\" \"attribute\" \"new_value\"", value="Edit the attribute of an existing Pokémon in the Pokédex.")
    await ctx.send(embed=embed)



bot.run('MTExOTcyNzIwNTE0MDkyNjU2NQ.GPOZxp.28LcTxVvbNhJcIVyhUYV7Vxokja8uNdMbg1jOo')
