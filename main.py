import simple_draw as sd
import draw_objects.sky_objects as sky_objects
import random

SNOWFLAKE_COUNT = 50
wind_speed = random.randint(-5, 5)


frame = 0
snowflakes_list = [sky_objects.SnowFlake() for i in range(SNOWFLAKE_COUNT)]


while True:
    if frame % 30 == 0:
        wind_speed = random.randint(-5, 5)

    sd.start_drawing()

    for snowflake in snowflakes_list:
        snowflake.move(wind_speed)





    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break
    frame += 1
sd.pause()
