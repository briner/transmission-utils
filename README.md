transmission-utils is a python script connecting to transmission through
their web-api. So to make it work, you must enable the web remote control
in transmission.

This tool allow to:
* move a directory of files from torrents to an other directory without
breaking transmission knowledge on where the files reside. You can then
move your directory (eg):
from  ~/torrent directory to  /mnt/my_external_hd/torrent
```bash
./transmission move-directory  ~/torrent /mnt/my_external_hd/torrent
```

* move an announce from one tracker to an other. Move (eg):
from http://tracker.piratebay.se/announce to https://tracker.piratebay.org/announce
```bash
./transmission-utils tracker move tracker.piratebay.org https://tracker.piratebay.org/announce
```
