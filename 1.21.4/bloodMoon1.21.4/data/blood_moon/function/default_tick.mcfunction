scoreboard players add timekeeper blood_moon.world_time 1
execute if score timekeeper blood_moon.world_time matches 60.. if predicate blood_moon:nightfall run function blood_moon:start_blood_moon
