#!/usr/bin/env python3
"""
Sudoku Game Launcher
A simple script to check dependencies and launch the Sudoku game.
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['streamlit', 'pandas', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages

def install_dependencies(packages):
    """Install missing packages"""
    print(f"Installing missing packages: {', '.join(packages)}")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies. Please install manually:")
        print(f"pip install {' '.join(packages)}")
        return False

def main():
    print("🧩 Sudoku Game Launcher")
    print("=" * 30)
    
    # Check dependencies
    missing = check_dependencies()
    
    if missing:
        print(f"❌ Missing dependencies: {', '.join(missing)}")
        response = input("Would you like to install them automatically? (y/n): ")
        
        if response.lower() in ['y', 'yes']:
            if not install_dependencies(missing):
                return
        else:
            print("Please install the missing dependencies manually:")
            print(f"pip install {' '.join(missing)}")
            return
    else:
        print("✅ All dependencies are installed!")
    
    # Launch the game
    print("\n🚀 Starting Sudoku Game...")
    print("The game will open in your default browser.")
    print("Press Ctrl+C to stop the game.\n")
    
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'app.py'])
    except KeyboardInterrupt:
        print("\n👋 Game stopped. Thanks for playing!")
    except FileNotFoundError:
        print("❌ Error: Could not find app.py. Make sure you're in the correct directory.")
    except Exception as e:
        print(f"❌ Error starting the game: {e}")

if __name__ == "__main__":
    main() 