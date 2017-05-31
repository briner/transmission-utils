transmission-utils is a python script connecting to transmission through
their web-api. So to make it work, you must enable the web remote control
in transmission.

This tool allow to:
* move a directory containing files from a torrent to an other. This allow
you to move your ~/torrent directory to (eg) /mnt/my_external_hd/torrent
by asking transmission to do it. In that way, you keep you torrent alive.

* move a announce for the trackers. That way, if your favorite tracker
change its tracker from eg http://tracker.piratebay.se/announce to
https://tracker.piratebay.org/announce)
