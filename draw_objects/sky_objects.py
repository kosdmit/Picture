import simple_draw as sd
import random


class SnowFlake:
    snowflakes_count = 0
    X_RANGE = 0, sd.resolution[0]
    Y_RANGE = sd.resolution[1]/2, sd.resolution[1]
    LENGTH_RANGE = 10, 20
    COLOR_RANGE = {'r': (100, 255), 'g': (100, 255), 'b': (255, 255)}
    FACTOR_A_RANGE = 0.7, 1.3
    FACTOR_B_RANGE = 0.7, 1.3
    FACTOR_C_RANGE = 0.7, 1.3

    def __init__(self):
        self.center = sd.get_point(x=random.randint(*SnowFlake.X_RANGE), y=random.randint(*SnowFlake.Y_RANGE))
        self.length = random.randint(*SnowFlake.LENGTH_RANGE)
        self._rg_component = random.randint(*SnowFlake.COLOR_RANGE['r'])
        self.color = (self._rg_component, self._rg_component,
                     random.randint(*SnowFlake.COLOR_RANGE['b']))
        self.factor_a = 0.6 * random.uniform(*SnowFlake.FACTOR_A_RANGE)
        self.factor_b = 0.35 * random.uniform(*SnowFlake.FACTOR_B_RANGE)
        self.factor_c = 60 * random.uniform(*SnowFlake.FACTOR_C_RANGE)


    def get_x(self):
        return self.center.x

    def get_y(self):
        return self.center.y

    def move(self, wind_speed):
        sd.square(sd.get_point(x=self.get_x()-self.length*1.2, y=self.get_y()-self.length*1.2), side=self.length*2.4,
                  color=sd.background_color, width=0)
        self.center = sd.get_point(x=self.get_x()+wind_speed, y=self.get_y()-2)
        sd.snowflake(self.center, self.length, self.color, self.factor_a, self.factor_b,
                     self.factor_c)


class Sun:
    X_RANGE = 0, sd.resolution[0]
    Y_RANGE = sd.resolution[1] * 3/4, sd.resolution[1]

    def __init__(self):
        self.centre_position = sd.get_point(x=random.randint(*Sun.X_RANGE), y=random.randint(*Sun.Y_RANGE))
        self.color = sd.COLOR_YELLOW
        self.radius = 70

        sd.circle(self.centre_position, self.radius, self.color, width=0)

    def draw(self):
        sd.circle(self.centre_position, self.radius, self.color, width=0)


