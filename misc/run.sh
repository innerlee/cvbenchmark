python misc/decord_speed.py 2>/dev/null | grep init: | awk '{ print $2 }' | datamash -H mean 1 sstdev 1
python misc/decord_speed.py 2>&1 | grep avformat_find_stream_info | awk '{ print $7 }' | sed 's/us//' | datamash -H mean 1 sstdev 1
