#!/bin/bash -x
port=9696
ip_address=$(ipconfig getifaddr en0)
echo $ip_address:$port
python3 -m http.server $port