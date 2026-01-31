#!/usr/bin/env python3
"""A fun animated hello script!"""
import time
import random
import sys

HELLO_ART = """
 ██╗  ██╗███████╗██╗     ██╗      ██████╗ ██╗
 ██║  ██║██╔════╝██║     ██║     ██╔═══██╗██║
 ███████║█████╗  ██║     ██║     ██║   ██║██║
 ██╔══██║██╔══╝  ██║     ██║     ██║   ██║╚═╝
 ██║  ██║███████╗███████╗███████╗╚██████╔╝██╗
 ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝
"""

COLORS = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]
RESET = "\033[0m"

GREETINGS = [
    "Welcome, friend!",
    "Nice to see you!",
    "Hope you're having a great day!",
    "You're awesome!",
    "Let's build something cool!",
    "Ready to code?",
]

def rainbow_print(text):
    """Print text with rainbow colors."""
    for i, line in enumerate(text.split('\n')):
        color = COLORS[i % len(COLORS)]
        print(f"{color}{line}{RESET}")
        time.sleep(0.1)

def sparkle():
    """Add some sparkle effect."""
    sparkles = "✨ 🌟 ⭐ 💫 🎉 🚀"
    print(f"\n{sparkles * 3}\n")

def main():
    print("\033[2J\033[H", end="")  # Clear screen
    rainbow_print(HELLO_ART)
    sparkle()
    greeting = random.choice(GREETINGS)
    print(f"  {greeting}\n")

if __name__ == "__main__":
    main()
