import sys
from mdcliapi2 import MajorDomoClient

def main():
    verbose = '-v' in sys.argv
    client = MajorDomoClient("tcp://localhost:5555", verbose)
    requests = 3
    for i in range(requests):
        request = b"{'apple'}"
        try:
            client.send(b"W_FRUITS", request)
        except KeyboardInterrupt:
            print ("send interrupted, aborting")
            return

    count = 0
    #while count < requests:
    #    try:
    #        reply = client.recv()
    #        print ("Client : response msg  ===>>", reply)
    #    except KeyboardInterrupt:
    #        break
    #    else:
    #        # also break on failure to reply:
    #        if reply is None:
    #            break
    #    count += 1
    print ("%i requests/replies processed" % requests)

if __name__ == '__main__':
    main()
