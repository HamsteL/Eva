import sys, os

if __name__ == "__main__":
    if len(sys.argv) > 1:
        os.popen("sudo atom "+ str(sys.argv[1]))
