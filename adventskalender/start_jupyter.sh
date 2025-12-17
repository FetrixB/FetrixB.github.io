#!/bin/bash
. .venv/bin/activate

echo "🚀 Starting Jupyter Lab for nginx reverse proxy..."

# Stop any existing Jupyter processes running on port 8888
lsof -ti:8888 | xargs -r kill 2>/dev/null || true
sleep 2

# Start Jupyter without systemd-inhibit first to debug
echo "Starting Jupyter Lab..."
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
    --ServerApp.allow_remote_access=True \
    --ServerApp.allow_credentials=True \
    --ServerApp.tornado_settings='{"ws_ping_interval": 30000, "ws_ping_timeout": 30000}' \
    --ServerApp.terminado_settings='{"shell_command": ["/bin/bash"]}' \
    --log-level=INFO
