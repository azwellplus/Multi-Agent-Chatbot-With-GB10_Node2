#!/bin/bash

# Start ComfyUI server without Docker
# This script runs ComfyUI directly on the host

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMFYUI_DIR="$SCRIPT_DIR/ComfyUI"
VENV_DIR="$SCRIPT_DIR/comfyui-env"
PORT=8188

echo "========================================="
echo "ComfyUI Startup Script"
echo "========================================="
echo "ComfyUI Directory: $COMFYUI_DIR"
echo "Virtual Env: $VENV_DIR"
echo "Port: $PORT"
echo ""

# Check if directory exists
if [ ! -d "$COMFYUI_DIR" ]; then
    echo "❌ Error: ComfyUI directory not found: $COMFYUI_DIR"
    exit 1
fi

cd "$COMFYUI_DIR"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment found"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Check Python version
PYTHON_VERSION=$(python --version)
echo "✓ Python version: $PYTHON_VERSION"

# Install/upgrade dependencies
echo ""
echo "📥 Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q

echo "✓ Dependencies installed"

# Create necessary directories
mkdir -p models/checkpoints models/vae output input temp
echo "✓ Directories created"

# Check for models
MODEL_COUNT=$(find models/checkpoints -name "*.safetensors" -o -name "*.ckpt" 2>/dev/null | wc -l)
if [ "$MODEL_COUNT" -eq 0 ]; then
    echo ""
    echo "⚠️  Warning: No models found in models/checkpoints/"
    echo "   Please download a model (e.g., SDXL Base 1.0) to generate images"
    echo "   Example:"
    echo "   cd models/checkpoints"
    echo "   wget https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/resolve/main/v1-5-pruned-emaonly-fp16.safetensors"
    echo ""
else
    echo "✓ Found $MODEL_COUNT model(s)"
fi

# Start ComfyUI in background
echo ""
echo "========================================="
echo "🚀 Starting ComfyUI Server (BACKGROUND)"
echo "========================================="
echo "URL: http://localhost:$PORT"
echo "Log: $COMFYUI_DIR/comfyui.log"
echo "PID file: $COMFYUI_DIR/comfyui.pid"
echo "========================================="
echo ""

nohup python main.py --listen 0.0.0.0 --port $PORT --preview-method auto > comfyui.log 2>&1 &

# Save PID
echo $! > comfyui.pid
echo "✓ ComfyUI started in background with PID $(cat comfyui.pid)"

tail -100f comfyui.log
