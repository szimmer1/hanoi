# main program
import sys
import hanoi

def solve(obj,n,f,t):
    if n is 1:
        obj.move(f,t)
        obj.out()
        return
    u = 3 - f - t
    solve(obj,n-1,f,u)
    obj.move(f,t)
    obj.out()
    solve(obj,n-1,u,t)

if len(sys.argv) < 2:
    print "Usage: python hanoi [disks]"
    sys.exit()

args = [int(i) for i in sys.argv[1:]]
towers = hanoi.Hanoi(args[0])
solve(towers,towers.size(),0,2)
