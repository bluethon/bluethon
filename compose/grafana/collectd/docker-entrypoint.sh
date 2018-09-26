#!/bin/sh

set -e

export GRAPHITE_HOST=$(hostname -i)

envtpl /etc/collectd/collectd.conf.tpl

#envsubst "`env | awk -F = '{printf " $$%s", $$1}'`" \
#    < /var/www/html/static/config_template.js \
#    > /var/www/html/static/config.js

exec "$@"
