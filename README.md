# Steal an Egg AFK

A simple Python script for Roblox's **Steal an Egg** that automates character movement to help prevent AFK disconnections while farming speed on the treadmill.

## How It Works

Every **600 seconds (10 minutes)**, the script automatically:

1. Makes the character jump to leave the treadmill.
2. Waits 1 second.
3. Moves slightly to the left to return to the treadmill.
4. Repeats the process continuously.

## Technologies

- **Python**
- **PyDirectInput** — keyboard input simulation

## Installation

Install the required library:

```bash
pip install pydirectinput
```

## Usage

Run the script:

```bash
python afk.py
```

Switch to the Roblox window within 5 seconds and keep it active.

Press `Ctrl + C` in the terminal to stop the script.

## Configuration

```python
INTERVAL = 600
LEFT_DURATION = 0.08
JUMP_DURATION = 0.3
START_DELAY = 5
```

All values are in seconds and can be adjusted as needed.

**Note:** The script does not guarantee prevention of AFK disconnections and may be subject to game rules.
