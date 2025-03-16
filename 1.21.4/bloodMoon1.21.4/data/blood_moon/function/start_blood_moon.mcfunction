say blood moon is rising
execute store result storage blood_moon:data sleeping_percentage int 1 run gamerule playersSleepingPercentage
scoreboard players set timekeeper blood_moon.world_time 0
data modify storage blood_moon:data is_blood_moon set value true
gamerule playersSleepingPercentage 150
execute as @a run worldborder warning distance 2000000000

