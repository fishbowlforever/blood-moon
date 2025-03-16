import os
from os import walk
from glob import iglob
from enum import Enum


NAMESPACE = "blood_moon"
VERSION = "1.21.4"
    
FUNCTION_PATH = f"bloodMoon{VERSION}/data/{NAMESPACE}/function/" #target path for generated functions

os.makedirs(FUNCTION_PATH, exist_ok=True) #uncomment to create target folder

class Enemy():
    def __init__(self, mobtype, weight, tags, texture):
        self.mobtype = mobtype
        self.weight = weight
        self.tags = tags + ["spread"]
        self.texture = texture
    
    def tags_to_list(self):
        res = "["
        for tag in self.tags:
            res += f"\"{NAMESPACE}.{tag}\","
        res += "]"
        return res
    
    def to_summon_command(self):
        return "summon "+ self.mobtype +""" ~ ~128 ~ {Tags: """+ self.tags_to_list() +""", ArmorItems:[{},{},{},{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:\""""+self.texture+""""}]}}}]}"""


def new_zombie(weight, tags, texture):
    return Enemy("minecraft:zombie", weight, tags + ["zombie"], texture)

def new_blood_zombie(weight, tags, texture):
    return new_zombie(weight, tags + ["blood_zombie"], texture)

enemies = [
    new_blood_zombie(10,[],"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYTVkMTQ2MmQ0NDc4MDU4YjZhMDFiNTI5NjExODUyYzZhMjE4NzAzOGFhMDY0NTY2NzI2ZDViNzI1ODMwNDdkNyJ9fX0="), # shot zombie (https://minecraft-heads.com/custom-heads/head/62933-zombie)
    new_blood_zombie(10,[],"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjUxMTc1YjUwM2VlNThhZmVlMDliNGIyMDczNTM5ZTQ5ZTEzM2UzNTFmNzJjMGEyODhlNWE0NmQ4ODNhOWJkOCJ9fX0="), # brain zombie (https://minecraft-heads.com/custom-heads/head/67853-zombie)
    new_blood_zombie(5,[],"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZmFhYzIyMzAxNTlhODAzZDI4Y2ZkZTY2NjJlYWYzNzlkYTg5YThhMDczYzdiZTIwYzZlN2U0MDhkZDg4NjFkMSJ9fX0="), # injured zombie (https://minecraft-heads.com/custom-heads/head/26692-injured-zombie)
    new_blood_zombie(2,[],"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDY5ZGIxODc2ODJkYTM3MDdhM2RiYzBhYzAzZGUxOGY2NzUyZDczODk5MjQ3NjEyMzZjM2I4NzBlYjkyMWM3OSJ9fX0="), # ultra bloodie zombie (https://minecraft-heads.com/custom-heads/head/26692-injured-zombie)
]

def calc_weight(array):
    res = 0
    for a in array:
        res += a.weight
    return res

with open(FUNCTION_PATH + "spawn_single_zombie.mcfunction","w+") as f:
    combined_weight = calc_weight(enemies)
    f.write(f"execute store result score @s blood_moon.rand run random value 1..{combined_weight}\n")
    entry = 1
    i = 1
    for enemy in enemies:
        f.write(f"execute if score @s blood_moon.rand matches {i}..{i + enemy.weight - 1} run {enemy.to_summon_command()}\n")
        i += enemy.weight
    
with open(FUNCTION_PATH + "spawn_all_zombies.mcfunction","w+") as f:
    for enemy in enemies:
        f.write(enemy.to_summon_command() + "\n")
