from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
from json import loads as json_loads, dumps as json_dumps
import app


def create_image():
    width = 64
    height = 64

    color1 = '#0000ff'
    color2 = '#fc0000'

    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

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
