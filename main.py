# main program
import sys
import hanoi

if len(sys.argv) < 3:
    print "Usage: python hanoi [pegs] [disks]"
    sys.exit()

args = [int(i) for i in sys.argv[1:]]
towers = hanoi.Hanoi(args[0], args[1])
towers.out()
