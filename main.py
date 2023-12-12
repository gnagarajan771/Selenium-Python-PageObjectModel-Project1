import sys

# Check Python version
if not (sys.version_info.major == 3 and sys.version_info.minor >= 10):
    print("This script requires Python 3.10 or higher!")
    print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)
