#!/bin/sh

# Run this script from any working directory.
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROGRAM="$SCRIPT_DIR/first.py"

if [ ! -f "$PROGRAM" ]; then
    printf 'Cannot find the program: %s\n' "$PROGRAM" >&2
    exit 1
fi

if command -v python3 >/dev/null 2>&1; then
    PYTHON=$(command -v python3)
elif command -v python >/dev/null 2>&1; then
    PYTHON=$(command -v python)
else
    # Check common macOS installer locations even when PATH is incomplete.
    for candidate in \
        /opt/homebrew/bin/python3 \
        /usr/local/bin/python3 \
        /Library/Frameworks/Python.framework/Versions/Current/bin/python3
    do
        if [ -x "$candidate" ]; then
            PYTHON=$candidate
            break
        fi
    done
fi

if [ -z "${PYTHON:-}" ]; then
    printf '%s\n' \
        'Could not find Python in PATH or the usual macOS install locations.' \
        'Run "python3 --version" and "which python3" to locate your installation.' >&2
    exit 127
fi

exec "$PYTHON" -u "$PROGRAM" "$@"
