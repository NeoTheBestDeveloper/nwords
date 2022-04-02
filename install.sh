#!/bin/sh

APP_PATH="$HOME/.local/share/nwords"
[ ! -d "$APP_PATH" ] && mkdir -p "$APP_PATH"

cp nw "$APP_PATH"
cp -r lib "$APP_PATH"

sudo ln -sf $APP_PATH/nw /usr/bin/nw
