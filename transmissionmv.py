#!/usr/bin/env python

import os
import sys
import argparse

try:
	import transmissionrpc
except:
	print("Unable to 'import transmissionrpc' !")
	print("Create a venv for this:")
	print(" - python3 -m venv venv")
	print(" - bash venv/bin/activate")
	print(" - pip install -r requirements.txt")
	print(" - pip install ipython")
	print("Exit !")
	sys.exit(1)



def get_torrent_location(torrent):
	return torrent._fields["downloadDir"].value

def is_torrent_elligible(torrent, base_dir):
	downloadDir_field=torrent._fields["downloadDir"]
	dirty=downloadDir_field.dirty
	location=downloadDir_field.value
	if dirty:
		return False
	if location.find(base_dir) != 0:
		return False
	return True

def move_torrent(tc, torrent, cur_dir, new_dir):
	cur_location=get_torrent_location(torrent)
	first_file=torrent.files()[0]["name"]
	if not is_torrent_elligible(torrent, cur_dir):
		print("Torrent id({}), named({}), dir({})".format(torrent.id,
														  first_file[:20],
														  cur_location))
		print(" is not elligible for a move from ({}) to ({})".format(cur_dir,
																	  new_dir))
		print(" Skip it !")
		return
	new_location=cur_location.replace(cur_dir, new_dir)
	subdir=cur_location.replace(cur_dir,"")
	#
	if not os.path.isdir(new_location):
		print("create dir({})".format(new_location))
		os.makedirs(new_location)
	print("- move torent_id({}), named({}), subdir({})".format(torrent.id,
															   first_file[:20],
															   subdir))
	print("  to {}".format(new_location))
	tc.move_torrent_data(torrent.id, new_location, timeout=3600.0)
	return True

def main(cur_base_dir, new_base_dir):
	print("Check that we can connect to localhost")
	try:
		tc = transmissionrpc.Client('localhost', port=9091)
	except:
		print("Unable to instantiate a client to 'localhost:9091'.")
		print(" Uncheck 'Use authentication' in Transmission > Edit preferences > Remote.")
		print(" Check that 127.0.0.1 is allowed in 'Only allow these remote addresses'.")
		print("Exit !")
		sys.exit(1)
	print(" ok.")

	# list the torrent
	
	lt=tc.get_torrents()
	lt_in_base=[t for t in lt if is_torrent_elligible(t, cur_base_dir)]
	for t in lt_in_base:
		move_torrent(tc, t, cur_base_dir, new_base_dir)
	
	


if "__main__" == __name__:
		parser = argparse.ArgumentParser(description="Move files actually managed by Transmission to an other location")
		parser.add_argument("current_base_dir")
		parser.add_argument("new_base_dir")
		args=parser.parse_args()
		
		# test the arguments
		if not os.path.isdir(args.current_base_dir):
			print("current_base_dir({}) must exist !".format(args.current_base_dir))
			print("Exit !")
			sys.exit(1)
		if not os.path.isdir(args.new_base_dir):
			print("new_base_dir({}) must exist !".format(args.new_base_dir))
			print("Exit !")
			sys.exit(1)
		
		main(args.current_base_dir, args.new_base_dir)
