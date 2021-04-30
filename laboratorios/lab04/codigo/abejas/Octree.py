import collections
import math
from Abejas import *

class Octree():
    midX = 0
    midY = 0
    midZ = 0
        
    def octree(self,bees,mins,midX,midY,midZ):
        self.midX = midX
        self.midY = midY
        self.midZ = midZ
        octree = []
        for i in range(8):
            ab = collections.deque()  
            octree.append(ab)
        
        for i in range(len(bees)):
            bee = Bee(self.midX,self.midY,self.midZ)
            bee = bees.pop()
            sector = self.hashing(bee,mins)
            octree[sector].insert(0,bee)
        diagonal = math.sqrt(math.pow((self.midX)*111325,2)+ math.pow((self.midY)*111325,2)+ math.pow((self.midZ)*111325,2))
        
        if diagonal > 100:
            for i in range (8):
                if(len(octree[i]) > 1):
                    self.nuevoOctree(octree[i],mins,i)
        else:
            for i in range (8):
                if(len(octree[i]) > 0):
                    self.choque(octree[i])
    
    def hashing(self,bee,mins):
        if bee.latitude <= mins[0] + self.midX:
            if bee.longitude <= mins[1] + self.midY:
                if bee.altitude <= mins[2] + self.midZ:
                    return 0
                else:
                    return 1
            else:
                if bee.altitude <= mins[2] + self.midZ:
                    return 2
                else:
                    return 3
        else:
            if bee.longitude <= mins[1] + self.midY:
                if bee.altitude <= mins[2] + self.midZ:
                    return 4
                else:
                    return 5
            else:
                if bee.altitude <= mins[2] + self.midZ:
                    return 6
                else:
                    return 7
    
    def choque(self,bees):
        for bee in bees:
            print(str(bee.latitude) +", "+ str(bee.longitude) + ", " + str(bee.altitude))
    
    def nuevoOctree(self,bees,mins,sector):
        if sector == 0:
            self.octree(bees,mins,(self.midX/2),(self.midY/2),(self.midZ/2))

        elif sector == 1:
            newZ = mins[2] + self.midZ
            mins.pop(2)
            mins.insert(2,newZ)
            self.octree(bees,mins,(self.midX/2),(self.midY/2),(self.midZ/2))

        elif sector == 2:
            newY = mins[1] + self.midY
            mins.pop(1)
            mins.insert(1,newY)
            self.octree(bees,mins,(self.midX/2),(self.midY/2),(self.midZ/2))

        elif sector  == 3:
            newZ = mins[2] + self.midZ
            mins.pop(2)
            mins.insert(2,newZ)
            newY = mins[1] + self.midY
            mins.pop(1)
            mins.insert(1,newY)
            self.octree(bees,mins,(self.midX/2),(self.midY/2),(self.midZ/2))

        elif sector == 4:
            nuevoX = mins[0] + self.midX
            mins.pop(0)
            mins.insert(0,nuevoX)
            self.octree(bees,mins,(self.midX/2),(self.midY/2),(self.midZ/2))

        elif sector == 5:
            nuevoX = mins[0] + self.midX
            mins.pop(0)
            mins.insert(0,nuevoX)
            nuevoZ = mins[2] + self.midZ
            mins.pop(2)
            mins.insert(2,nuevoZ)
            self.octree(bees,mins,(self.midX/2),(self.midY/2),(self.midZ/2))

        elif sector == 6:
            nuevoX = mins[0] + self.midX
            mins.pop(0)
            mins.insert(0,nuevoX)
            nuevoY = mins[1] + self.midY
            mins.pop(1)
            mins.insert(1,nuevoY)
            self.octree(bees,mins,(self.midX/2),(self.midY/2),(self.midZ/2))

        else:
            nuevoX = mins[0] + self.midX
            mins.pop(0)
            mins.insert(0,nuevoX)
            nuevoY = mins[1] + self.midY
            mins.pop(1)
            mins.insert(1,nuevoY)
            nuevoZ = mins[2] + self.midZ
            mins.pop(2)
            mins.insert(2,nuevoZ)
            self.octree(bees,mins,(self.midX/2),(self.midY/2),(self.midZ/2))
