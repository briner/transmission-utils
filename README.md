transmission-utils is a python script connecting to transmission through
their web-api. So to make it work, you must enable the web remote control
in transmission.

This tool allow to:
* move a directory of files from torrents to an other directory. This allow
you to move your ~/torrent directory to (eg) /mnt/my_external_hd/torrent
by asking transmission to do it. In that way, you keep you torrent alive.
```bash
transmission move-directory  ~/torrent /mnt/my_external_hd/torrent
```

* move a announce for the trackers. That way, if your favorite tracker
change its tracker from eg http://tracker.piratebay.se/announce to
https://tracker.piratebay.org/announce), you just have to type
```bash
./transmission-utils tracker move tracker.piratebay.org https://tracker.piratebay.org/announce
```
