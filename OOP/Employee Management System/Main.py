# Main.py
import sys
from FrontEndManager import FrontEndManager

if __name__ == "__main__":
    # Optional file name from command-line
    file_name = sys.argv[1] if len(sys.argv) > 1 else None
    app = FrontEndManager(file_name)
    app.run()
