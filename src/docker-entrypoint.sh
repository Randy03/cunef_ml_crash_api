#!/bin/bash

set -e

if ! whoami &> /dev/null; then
  if [ -w /etc/passwd ]; then
    echo "${USER_NAME:-default}:x:$(id -u):0:${USER_NAME:-default} user:${HOME}:/sbin/nologin" >> /etc/passwd
  fi
fi

python3 app.py &
cd shiny-dashboard && R -e 'library(shiny);runApp(host ="0.0.0.0",port=5001, launch.browser = FALSE)'
