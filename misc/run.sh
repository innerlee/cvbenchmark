python misc/decord_speed.py 2>/dev/null | grep init: | awk '{ print $2 }' | datamash -H mean 1 sstdev 1
