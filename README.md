# Yeelight Bulb Controller

Control your Yeelight Bulb

## Requirements
- Use [Python 3](https://www.python.org) (or later) to execute
- Enable **LAN Control** option in your Yeelight App
- I tested it with [Yeelight LED Light Bulb (Color)](https://www.mi.com/us/yeelight-led-light-bulb), but it should work on other models

## How to use
### **Configure your device in ```configs.json```:**
```json
{
    "bulb_ip": "192.168.0.44",
    "watch_brightness": 1,
    "watch_monitor": 1,
    "scenes": {
        "default": {
            "brightness": 100,
            "color_temp": 5862
        },
        "softblue": {
            "brightness": 1,
            "rgb": [
                0,
                234,
                255
            ]
        },
        "synthwave": {
            "brightness": 20,
            "rgb": [
                138,
                43,
                226
            ]
        }
    }
}
```

### ```bulb_ip```
IP of your device in LAN.
> Make sure the **LAN Control** option is enabled in your Yeelight App.

### ```watch_brightness```
Bulb brightness for [watch](#Watch) feature.

### ```watch_monitor```
Monitor for Watch feature.
> 0 = main monitor<br>
> 1 = second monitor<br>
> ...

### ```scenes```
You can define scenes for yout bulb.
```json
{
    "brightness": 20,
    "rgb": [138, 43, 226],
    "color_temp": 2000
}
```
> - Object key is the scene name
> - Use ```rgb``` or ```color_temp```, not use both.

### **Run command:**

Available commands:
- **```ip [device_ip]```**: Set device IP
- **```on```**: Turn ON
- **```off```**: Turn OFF
- **```toggle```**: Toggle
- **```scene [scene_name]```**: Set scene

## Watch

The watch feature get de current predominant color in your monitor and then set the bulb color.

Watch commands:
- **```watch brightness [value]```**: Set device brightness during watch
- **```watch monitor [value]```**: Set monitor to watch
- **```watch monitor run```**: Run watch
