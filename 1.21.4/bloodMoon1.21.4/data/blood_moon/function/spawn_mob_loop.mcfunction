execute as @a at @s run function blood_moon:spawn_mobs
execute if data storage blood_moon:data is_blood_moon run schedule function blood_moon:spawn_mob_loop 10s