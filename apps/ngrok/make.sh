#!/bin/sh

# git clone https://github.com/inconshreveable/ngrok
### 请使用下面的地址，修复了无法访问的包地址
git clone https://github.com/tutumcloud/ngrok.git ngrok
cd ngrok
mkdir crt
cd crt

domain="yourdomain.com"

openssl genrsa -out rootCA.key 2048
openssl req -x509 -new -nodes -key rootCA.key -subj "/CN=$domain" -days 5000 -out rootCA.pem
openssl genrsa -out device.key 2048
openssl req -new -key device.key -subj "/CN=$domain" -out device.csr
openssl x509 -req -in device.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out device.crt -days 5000

cp rootCA.pem ../assets/client/tls/ngrokroot.crt
cp device.crt ../assets/server/tls/snakeoil.crt
cp device.key ../assets/server/tls/snakeoil.key
