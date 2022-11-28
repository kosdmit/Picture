import simple_draw as sd
import draw_objects.sky_objects as sky_objects
import random

SNOWFLAKE_COUNT = 50
wind_speed = random.randint(-5, 5)


frame = 0
snowflakes_list = list()

snowflakes_list = sky_objects.create_snowflakes(SNOWFLAKE_COUNT, snowflakes_list)
sd.start_drawing()
sun = sky_objects.Sun()
rainbow = sky_objects.Rainbow()
while True:
    if frame % 30 == 0:
        wind_speed = random.randint(-5, 5)


    for snowflake in snowflakes_list:
        sun.draw()
        rainbow.draw()
        snowflake.move(wind_speed)
        if snowflake.is_fallen and not snowflake.is_child_exist:
            sky_objects.create_snowflakes(1, snowflakes_list)
            snowflake.is_child_exist = True







    sd.finish_drawing()
    sd.sleep(0.01)
    if sd.user_want_exit():
        break
    frame += 1
sd.pause()
