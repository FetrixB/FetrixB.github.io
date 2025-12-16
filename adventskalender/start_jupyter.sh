#!/bin/sh
. .venv/bin/activate
# Inhibit system sleep while Jupyter is running
systemd-inhibit --what=sleep --who="Jupyter Lab" --why="Server running" jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --ServerApp.allow_origin='*' --ServerApp.disable_check_xsrf=True
