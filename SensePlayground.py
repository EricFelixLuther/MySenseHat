from sense_hat import SenseHat
import time
import random


class SensePlayGround(SenseHat):

    def __init__(self, rot=0, low_gamma=True):
        super(SensePlayGround, self).__init__()
        self.screen = [[0,0,0] for i in range(64)]
        self.set_rotation(rot)
        self.low_light = low_gamma
        self.WARIANTY = {1: {'len': 0, 'func': self.kolory1},
                         2: {'len': 0, 'func': self.kolory2},
                         3: {'len': 0, 'func': self.kolory3},
                         }
        for fun in self.WARIANTY.keys():
            self.WARIANTY[fun]['len'] = len([x for x in self.WARIANTY[fun]['func'](times=1)])
            
##        self.kolory.append(len([x for x in self.fun(times=1)])
##        self.KOLORY1_LEN = len([x for x in self.kolory1(times=1)])
##        self.KOLORY2_LEN = len([x for x in self.kolory2(times=1)])
##        self.KOLORY3_LEN = len([x for x in self.kolory3(times=1)])
##        self.WARIANTY = {1: {'len': self.KOLORY1_LEN, 'func': self.kolory1},
##                         2: {'len': self.KOLORY2_LEN, 'func': self.kolory2},
##                         3: {'len': self.KOLORY3_LEN, 'func': self.kolory3},
##                         }

    def __call__(self, *args):
        self.clear(args)

    def wys_tekst(self, tekst):
        self.show_message(tekst)

    def kolory_teczy(self, wariant, speed=0.001, razy=-1):
        for kolory in self.WARIANTY[wariant]['func'](razy):
            self.clear(kolory)
            time.sleep(speed)

    def kolory1(self, times=-1):
        while 1:
            for i in range(256):
                yield (0, 0, i)

            for i in range(256):
                yield (i, 0, 255)
            for i in range(255, -1, -1):
                yield (255, 0, i)

            for i in range(256):
                yield (255, i, 0)
            for i in range(255, -1, -1):
                yield (i, 255, 0)

            for i in range(256):
                yield(0, 255, i)

            for i in range(256):
                yield (i, 255, 255)

            for i in range(255, -1, -1):
                yield (i, i, i)

            if times > 0:
                times -= 1
            if times == 0:
                break

    def kolory2(self, times=-1):
        for i in range(256):
            yield (0, 0, i)
            
        while 1:
            for i in range(256):
                yield (i, 0, 255)
            for i in range(255, -1, -1):
                yield (255, 0, i)

            for i in range(256):
                yield (255, i, 0)
            for i in range(255, -1, -1):
                yield (i, 255, 0)

            for i in range(256):
                yield (0, 255, i)
            for i in range(255, -1, -1):
                yield (0, i, 255)

            if times > 0:
                times -= 1
            if times == 0:
                break

    def kolory3(self, times=-1):
        for i in range(256):
            yield (0, 0, i)
            
        while 1:
            for i in range(256):
                yield (i, 0, 255 - i)

            for i in range(256):
                yield (255 - i, i, 0)

            for i in range(256):
                yield (0, 255 - i, i)

            if times > 0:
                times -= 1
            if times == 0:
                break

    def budzik_sloneczny(self, godziny):
        time.sleep((godziny * 3600) - 750)
        for i in range(256):
            self.clear((i, i, i/2))
            time.sleep(3)

    def wariuj(self):
        while True:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.set_pixel(x, y, r, g, b)
            time.sleep(0.1)

    def klepsydra(self, czas, wariant=1):
        """
        @czas - int, czas trwania w sekundach
        """
        number_of_states = 256.0 * 3.0 * 64.0
        delay = czas / number_of_states
        for y in range(8):
            for x in range(8):
                rgb = [0,0,0]
                for l in range(3):
                    for v in range(256):
                        rgb[l] = v
                        self.set_pixel(x, y, rgb[0], rgb[1], rgb[2])
                        time.sleep(delay)

        for v in range(255, -1, -1):
            self.clear([v, v, v])
            time.sleep(0.01)
        for v in range(0, 256):
            self.clear([v, v, v])
            time.sleep(0.01)
        for v in range(255, -1, -1):
                self.clear([v, v, v])
                time.sleep(0.01)

    def temperatura(self):
        self.show_message(str(self.get_temperature()))

def yelder():
    for i in (1, 2, 3):
        yield i
    for i in ('a', 'b', 'c'):
        yield i
##---=== DOCS ===---##
##set_rotation(r, redraw)
##    r - int, (0, 90, 180, 270)
##    redraw - boolean
##flip_h(redraw)
##flip_v(redraw)
##set_pixels(pixel_list)
##    pixel_list - list, [R,G,B] * 64
##get_pixels()
##    RETURN list
##set_pixel(x, y, r, g, b)
##    x, y - ints
##    pixel - tuple/list (r,g,b)
##    r, g, b - ints (0-255)
##get_pixel(x, y)
##    x, y - ints
##load_image(file_path, redraw)
##    file_path - string
##clear(r, g, b)
##    colour - list/tuple (r,g,b)
##    r, g, b - ints (0-255)
##show_message(text_string, scroll_speed, text_colour, back_colour)
##    text_string - string
##    scroll_speed - float
##    text_colour, back_colour - list (r,g,b)
##show_letter(s, text_colour, back_colour)
##    s - string, a single character
##low_light = True or False
##gamma = list/tuple of len=32, containing ints 0-31
##gamma_reset()
##get_humidity()
##get_temperature() - calls get_temperature_from_humidity()
##get_temperature_from_humidity()
##get_temperature_from_pressure()
##get_pressure()
##set_imu_config(compass_enabled, gyro_enabled, accel_enabled)
##get_orientation_radians()
##    RETURNS dictionary
##get_orientation_degrees()
##get_orientation - calls get_orientation_degrees()
##get_compass()
##get_compass_raw()
##get_gyroscope()
##get_gyryoscope_raw()
##get_accelerometer()
##get_accelerometer_raw()
