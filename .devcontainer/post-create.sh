#!/bin/bash
set -e

echo "Installing Python dependencies ..."
pip install --upgrade pip
pip install -r requirements.txt --quiet

echo "Installing optional Marp CLI ..."
npm install -g @marp-team/marp-cli || echo "WARN  Marp CLI install failed; workshop notebooks are still ready."

echo "Post-create setup complete."
