from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
from json import loads as json_loads, dumps as json_dumps
import app


def create_image():

    image = Image.open('./icon.png')
    image.thumbnail([64, 64], Image.ANTIALIAS)

    return image


def set_scene(icon, item):
    app.scene(str(item))


icon = icon('test', create_image(), menu=menu(
    item(
        'on',
        lambda icon, item: app.on()
    ),
    item(
        'off',
        lambda icon, item: app.off()
    ),
    item(
        'scenes',
        menu(lambda: (
            item(
                scene,
                set_scene
            )
            for scene in app.CONFIGS['scenes'].keys()
        ))
    )
))
icon.run()
