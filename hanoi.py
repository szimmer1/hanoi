class HanoiException(Exception):
    def __init__(self, message = "moved big on small"):
        self.message = message
    def __str__(self):
        return repr(self.message)


class Hanoi():
   def __init__(self, disks = 3):
       self.moves = 0
       self.disks = disks
       self.pegs = [[],[],[]]
       for i in range(1,disks+1):
           self.pegs[0].append(i)

   def size(self):
       return self.disks

   def move(self, from_peg, to_peg):
       self.moves += 1
       t = self.pegs[to_peg]
       f = self.pegs[from_peg]
       disk = f.pop()
       if len(t) > 0 and disk < t[len(t)-1]:
           raise HanoiException(
                   dict(
                        from_peg=dict(peg=from_peg,state=f),
                        to_peg=dict(peg=to_peg,state=t),
                        bottom_disk=t[len(t)-1],
                        top_disk=disk
                        )
                   )
       else:
           t.append(disk)

   def out(self):
       print "Move "+str(self.moves)
       format_space_str = "{0:^"+str(self.disks*2+1)+"s}"
       for i in range( len(max(self.pegs,key = lambda peg:len(peg))) - 1, -1, -1):
           for peg in self.pegs:
               disk = ""
               if len(peg) > i:
                   for _ in range(2*(self.disks-peg[i])+1):
                       disk += "="
               print format_space_str.format(disk),
           print
       for peg in range(0,len(self.pegs)):
           print format_space_str.format(str(peg)),
       print
       print
