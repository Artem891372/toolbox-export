#!/usr/bin/bash
set -e

BIN_DIR="$HOME/.local/bin"

echo "Installing toolbox-export fork..."

# Create bin directory if not exists
mkdir -p "$BIN_DIR"

install_script () {
    local file="$1"
    echo "Installing $file to $BIN_DIR"
    install -m 755 "$file" "$BIN_DIR/$file"
}

install_script toolbox-export.py
install_script toolbox-app.py

echo
echo "✔ Installation complete"
echo
echo "Make sure $BIN_DIR is in your PATH:"
echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
