pm2 stop light-tray
pm2 delete light-tray
pm2 start tray.py --interpreter python3 --name light-tray