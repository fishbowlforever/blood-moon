function blood_moon:set_sleeping_percentage with storage blood_moon:data
data remove storage blood_moon:data is_blood_moon
tellraw @a ["the ",{"bold":true,"color":"dark_red","text":"Blood Moon"}," has ended."]
scoreboard players set timekeeper blood_moon.world_time 0
execute as @a run worldborder warning distance 100000
