#!/bin/bash
path=$(/bin/pwd)
sudo nohup $path/bin/ngrokd -tlsKey=$path/server.key -tlsCrt=$path/server.crt -domain=weixin.lengqidong.com -httpAddr=:80 -httpsAddr=:443 -tunnelAddr=:44433 &> /dev/null &
