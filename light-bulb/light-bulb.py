from yeelight import Bulb
import click
from json import loads as jsonLoads, dumps as jsonDumps


def getConfig():
    configFile = open('config.json', 'r')
    config = jsonLoads(configFile.read())
    configFile.close()
    return config

BULB_IP = getConfig()['bulbIp']

def createBulb():
    return Bulb(BULB_IP)



@click.group()
def main():
    pass


@main.command()
@click.argument('ip')
def setip(ip):
    configFile = open('config.json', 'r')
    config = jsonLoads(configFile.read())
    configFile.close()

    config['bulbIp'] = ip

    configFile = open('config.json', 'w')
    configFile.write(jsonDumps(config))
    configFile.close()

    print('Light Bulb IP changed to %s' % ip)


@main.command()
def on():
    bulb = createBulb()
    bulb.turn_on()
    print('Light Bulb on')


@main.command()
def off():
    bulb = createBulb()
    bulb.turn_off()
    print('Light Bulb off')


@main.command()
def toggle():
    bulb = createBulb()
    bulb.toggle()
    print('Light Bulb toggled')


@main.command()
def default():
    bulb = createBulb()
    bulb.set_brightness(100)
    bulb.set_color_temp(5862)
    print('Light Bulb default')


@main.command()
def soft():
    bulb = createBulb()
    bulb.set_brightness(1)
    bulb.set_rgb(0, 234, 255)
    print('Light Bulb soft')


@main.command()
def hell():
    bulb = createBulb()
    bulb.set_brightness(1)
    bulb.set_rgb(255, 0, 0)
    print('Light Bulb hell')


if __name__ == "__main__":
    main()
