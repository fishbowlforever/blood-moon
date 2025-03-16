function blood_moon:spawn_single_zombie
execute as @a run spreadplayers ~ ~ 0 50 false @e[tag=blood_moon.spread]
tag @e[tag=blood_moon.spread] remove blood_moon.spread

say Zombie
execute if data storage blood_moon:data is_blood_moon run schedule function blood_moon:spawn_mobs 1s

