from yeelight import Bulb
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
    config_file.write(json_dumps(config, indent=4))
    config_file.close()


CONFIGS = get_configs()


def create_bulb():
    return Bulb(CONFIGS['bulb_ip'])


def compute_average_image_color():

    img = getDisplaysAsImages()[CONFIGS['watch_monitor']]

    width, height = 150, 150
    img = ImageEnhance.Color(img).enhance(1)
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

def ip(ip):
    configs = get_configs()

    if(ip):
        configs['bulb_ip'] = ip
        set_configs(configs)
        print('Light Bulb IP changed to %s' % ip)
    else:
        print(configs['bulb_ip'])


def configs():
    configs = get_configs()

    for key, value in configs.items():
        print("%s: %s" % (key, value))


def on():
    bulb = create_bulb()
    bulb.turn_on()
    print('Light Bulb on')


def off():
    bulb = create_bulb()
    bulb.turn_off()
    print('Light Bulb off')


def toggle():
    bulb = create_bulb()
    bulb.toggle()
    print('Light Bulb toggled')


def scene(scene_name):
    bulb = create_bulb()
    scene = CONFIGS['scenes'][scene_name]

    bulb.set_brightness(scene['brightness'])

    if 'rgb' in scene:
        r, g, b = scene['rgb']
        bulb.set_rgb(r, g, b)
    elif 'color_temp' in scene:
        bulb.set_color_temp(scene['color_temp'])

    print('Light Bulb scene %s' % scene_name)


#################### watch ####################

def watch_brightness(brightness):
    configs = get_configs()

    if(brightness):
        configs['watch_brightness'] = int(brightness)
        set_configs(configs)
        print('Light Bulb brightness changed to %s' % brightness)
    else:
        print(configs['watch_brightness'])


def watch_monitor(monitor):
    configs = get_configs()

    if(monitor):
        configs['watch_monitor'] = int(monitor)
        set_configs(configs)
        print('Light Bulb monitor changed to %s' % monitor)
    else:
        print(configs['watch_monitor'])


def watch_run():

    print('Watching monitor %s' % CONFIGS['watch_monitor'])

    bulb = create_bulb()
    bulb.set_brightness(CONFIGS['watch_brightness'])
    bulb.duration = 1800

    while(True):
        color = compute_average_image_color()

        try:
            bulb.set_rgb(color[0], color[1], color[2])
            print('Light Bulb rgb%s' % str(color))
            time_sleep(2)
        except:
            bulb = create_bulb()
            bulb.duration = 1800
            print('Create new Bulb instance')
