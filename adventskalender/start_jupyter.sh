#!/bin/sh
. .venv/bin/activate
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --ServerApp.allow_origin='*' --ServerApp.disable_check_xsrf=True
