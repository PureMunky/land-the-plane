#!/usr/bin/env bash
# Download the Piper voice model used by this project.
#
# The default voice is en-US Ryan (medium quality) — a male American
# narration voice that works well for solo-host podcast pacing.
#
# We pull from the rhasspy/piper v0.0.2 GitHub release rather than
# Hugging Face because the GH-release URLs are reachable from more
# restricted networks (sandboxes, CI runners) and pin a known version.
set -euo pipefail

VOICE_DIR="$(dirname "$0")/../voices"
mkdir -p "$VOICE_DIR"
cd "$VOICE_DIR"

if [[ -f "en-us-ryan-medium.onnx" ]]; then
    echo "Voice already installed: $(pwd)/en-us-ryan-medium.onnx"
    exit 0
fi

URL="https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-en-us-ryan-medium.tar.gz"
echo "Downloading: $URL"
curl -L --fail -A "Mozilla/5.0" -o voice.tar.gz "$URL"
tar xzf voice.tar.gz
rm voice.tar.gz
echo "Installed:"
ls -lh en-us-ryan-medium.onnx en-us-ryan-medium.onnx.json
