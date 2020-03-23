from yeelight import Bulb
import click
from json import loads as json_loads, dumps as json_dumps
from PIL import ImageEnhance
from time import sleep as time_sleep
from desktopmagic.screengrab_win32 import getDisplaysAsImages


def get_configs():
    configFile = open('configs.json', 'r')
    config = json_loads(configFile.read())
    configFile.close()
    return config


def set_configs(config):
    config_file = open('configs.json', 'w')
    config_file.write(json_dumps(config))
    config_file.close()


configs = get_configs()
BULB_IP = configs['bulb_ip']
MONITOR = configs['monitor']
BRIGHTNESS = configs['brightness']


def create_bulb():
    return Bulb(BULB_IP)


def compute_average_image_color():

    img = getDisplaysAsImages()[MONITOR]

    width, height = 150, 150
    img = ImageEnhance.Color(img).enhance(5)
    img = img.resize((width, height), resample=0)
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total/count, g_total/count, b_total/count)


############################ CLI #################


@click.group()
def main():
    pass


@main.command()
@click.argument('ip')
def setip(ip):
    configs = get_configs()
    configs['bulb_ip'] = ip
    set_configs(configs)

    print('Light Bulb IP changed to %s' % ip)


@main.command()
@click.argument('value')
def setbrightness(value):
    configs = get_configs()
    configs['brightness'] = int(value)
    set_configs(configs)

    print('Light Bulb brightness changed to %s' % value)


@main.command()
@click.argument('monitor')
def setmonitor(monitor):
    configs = get_configs()
    configs['monitor'] = int(monitor)
    set_configs(configs)

    print('Light Bulb monitor changed to %s' % monitor)


@main.command()
def configs():
    configs = get_configs()

    for key, value in configs.items():
        print("%s: %s" % (key, value))


@main.command()
def run():

    bulb = create_bulb()
    bulb.set_brightness(BRIGHTNESS)

    while(True):
        color = compute_average_image_color()

        try:
            bulb.set_rgb(color[0], color[1], color[2])
            print('Light Bulb rgb%s' % str(color))
            time_sleep(2)
        except:
            bulb = create_bulb()
            print('Create new Bulb instance')


if __name__ == "__main__":
    main()
