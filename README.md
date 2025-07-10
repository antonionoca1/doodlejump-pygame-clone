# Doodle Jump Pygame

A vertical platformer game inspired by Doodle Jump, implemented in Python using Pygame. Guide your character upward by jumping on platforms, avoiding obstacles, and collecting power-ups!

## Features

- **Vertical Scrolling:** The world scrolls down as you ascend.
- **Player Character:** Automatically jumps when landing on a platform.
- **Platform Types:**
  - Normal: Static, disappear after one jump.
  - Moving: Move horizontally or vertically.
  - Breaking: Break/disappear after being touched.
  - Springs/Trampolines: Give a higher jump boost.
- **Obstacles/Enemies:** Monsters, black holes, and more.
- **Power-ups:** Temporary abilities like propeller hat (flight) and shield.
- **Scoring:** Points based on height achieved.
- **Game Over:** When you fall off the screen or hit an obstacle.

## User Interface

- **Main Menu:** Start game, High Scores, Exit.
- **In-Game HUD:** Shows current score and power-up status.
- **Game Over Screen:** Final score, high score, retry/return options.
- **High Score Board:** Displays top scores.

## Controls

- **Move:** Left/Right Arrow or A/D
- **Start:** Enter
- **Restart:** R (on game over screen)
- **Quit:** Esc
- **Pause:** P (optional)

## Graphics & Sound

- Simple, doodle-like, hand-drawn art style
- Sound effects: jump, platform break, power-up, hit obstacle, game over
- Upbeat looping background music

## Getting Started

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the game:
   ```sh
   # On Windows
   run.bat
   # Or
   python main.py
   ```

## Project Structure

- `main.py` - Main entry point
- `domain/` - Core game entities and types
- `services/` - Game logic and state management
- `ui/` - Rendering and user interface
- `assets/` - Art and sound assets

---

Enjoy playing and feel free to contribute or customize!
