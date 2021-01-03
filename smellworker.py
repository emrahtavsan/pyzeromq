import sys
from mdwrkapi import MajorDomoWorker

def main():
    verbose = '-v' in sys.argv
    worker = MajorDomoWorker("tcp://localhost:5555", b"W_SMELL", verbose)
    reply = None
    while True:
        request = worker.recv(reply, "W_SMELL")
        #print ("Worker: response msg ===>>", request)
        if request is None:
            break # Worker was interrupted
        reply = request # Echo is complex... :-)


if __name__ == '__main__':
    main()
