class HanoiException(Exception):
    def __init__(self, message = ""):
        self.message = message
    def __str__(self):
        return repr(self.message)


class Hanoi():

   def __init__(self, pegs = 3, disks = 3):
       self.disks = disks
       self.pegs = [[] for _ in range(0,pegs)]
       for i in range(1,disks+1):
           self.pegs[0].append(i)

   def move(self, from_peg, to_peg):
       f = self.pegs[from_peg]
       t = self.pegs[to_peg]
       disk = f.pop()
       if len(t) > 0 and disk < t[len(t)-1]:
           raise HanoiException("Moved large on small")
       else:
           t.append(disk)

   def out(self):
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
