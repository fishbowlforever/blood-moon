function blood_moon:spawn_single_zombie
spreadplayers ~ ~ 0 50 false @e[tag=blood_moon.spread]
tag @e[tag=blood_moon.spread] remove blood_moon.spread
effect give @e[tag=blood_moon.blood_zombie] minecraft:strength infinite 0 true

