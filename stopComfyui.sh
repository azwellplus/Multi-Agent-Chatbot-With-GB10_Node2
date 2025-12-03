#!/bin/bash

# Stop ComfyUI server started by start.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMFYUI_DIR="$SCRIPT_DIR/ComfyUI"
PID_FILE="$COMFYUI_DIR/comfyui.pid"

echo "========================================="
echo "🛑 Stopping ComfyUI Server"
echo "========================================="

# Check PID file exists
if [ ! -f "$PID_FILE" ]; then
    echo "❌ Error: PID file not found!"
    echo "   Expected: $PID_FILE"
    echo "   Is ComfyUI running or was it started?"
    exit 1
fi

PID=$(cat "$PID_FILE")

# Check if process is running
if ps -p "$PID" > /dev/null 2>&1; then
    echo "🔧 Stopping process with PID: $PID"
    kill "$PID"

    # Wait for process to stop
    sleep 1

    if ps -p "$PID" > /dev/null 2>&1; then
        echo "⚠️  Process did not stop gracefully, forcing..."
        kill -9 "$PID"
    else
        echo "✓ ComfyUI stopped successfully"
    fi

else
    echo "⚠️ Warning: No running process found for PID $PID"
fi

# Remove PID file
rm -f "$PID_FILE"
echo "✓ PID file removed"

echo "========================================="
echo "Log file: $COMFYUI_DIR/comfyui.log"
echo "========================================="
