#!/bin/bash

echo "📋 Starting installation for Clipboard Logger..."

# Step 1: Install pip if not available
if ! command -v pip3 &> /dev/null; then
    echo "🐍 pip3 not found. Installing Python3 pip..."
    sudo apt update
    sudo apt install -y python3-pip
fi

# Step 2: Install pyperclip for clipboard access
echo "📦 Installing Python module: pyperclip"
pip3 install --user pyperclip

# Step 3: Install mousepad (you can change to gedit, nano, etc.)
echo "🖥️ Installing mousepad text editor..."
sudo apt install -y mousepad

# Step 4: Make the Python script executable
echo "🔧 Making script executable..."
chmod +x clipboard_logger.py

# Step 5: Prompt to run the script
read -p "🚀 Do you want to run the Clipboard Logger now? (y/n): " choice
if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
    echo "✅ Running Clipboard Logger..."
    python3 clipboard_logger.py
else
    echo "ℹ️ You can run it later using: python3 clipboard_logger.py"
fi

echo "🎉 Installation complete!"
