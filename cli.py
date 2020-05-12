import app
import click

############################ CLI #################


@click.group()
def main():
    pass


@main.command()
@click.argument('ip', required=False)
def ip(ip):
    app.ip(ip)


@main.command()
def configs():
    app.configs()


@main.command()
def on():
    app.on()


@main.command()
def off():
    app.off()


@main.command()
def toggle():
    app.toggle()


@main.command()
@click.argument('scene_name', type=click.Choice(CONFIGS['scenes'].keys()))
def scene(scene_name):
    app.scene(scene_name)


#################### watch ####################

@main.group()
def watch():
    pass


@watch.command()
@click.argument('brightness', required=False)
def brightness(brightness):
    app.watch_brightness(brightness)


@watch.command()
@click.argument('monitor', required=False)
def monitor(monitor):
    app.watch_monitor(monitor)


@watch.command()
def run():
    app.watch_run()


######################################


if __name__ == "__main__":
    main()
