#!/bin/bash
. .venv/bin/activate

echo "🚀 Starting Jupyter Lab with minimal reverse proxy config..."

jupyter lab \
    --ServerApp.base_url=/jupyter/ \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --ServerApp.allow_origin='*' \
    --ServerApp.disable_check_xsrf=True \
    --ServerApp.token='' \
    --ServerApp.password='' \
    --ServerApp.trust_xheaders=True \
    --log-level=INFO &

echo "Jupyter started in background"
