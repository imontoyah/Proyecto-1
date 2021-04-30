import collections
import math
from Abejas import *
from Octree1 import *

class Read:
    arr=[]
    maxX=-math.inf
    minX=math.inf
    maxY=-math.inf
    minY=math.inf
    minZ=math.inf
    maxZ=-math.inf

    def reader(self, file):
        archivo = open(file,'r')
        textoString=archivo.read()
        archivo.close()
        rows = textoString.split("\n")
        
        print("----The dataset contains "+str(len(rows)-2)+" bees----")
        for row in rows:
            column=row.split(",")
            if len(column)<3:
                break
            if column[0]== "Coordenada x de la abeja":
                continue
            x=float(column[0])
            y=float(column[1])
            z=float(column[2])

            if x < self.minX:
                self.minX = x
            if x > self.maxX:
                self.maxX=x
            if y < self.minY:
                self.minY = y
            if y > self.maxY:
                self.maxY = y
            if z < self.minZ:
                self.minZ = z
            if z > self.maxZ:
                self.maxZ = z
            bee = Bee(x,y,z)
            self.arr.append(bee)
            print(str(x)+","+str(y)+","+str(z))
        print("\n")
        print("--The colliding bees are at the following coordinates--")

        self.bees = self.arr
        midD=(self.minX - self.maxX)/2
        midW=(self.maxY - self.minY)/2
        midH=(self.maxZ - self.minZ)/2
        mins=[self.minX,self.minY,self.minZ]
        ph = math.sqrt(math.pow((midD)*111325,2)+math.pow((midW)*111325,2))
        diagonal = math.sqrt(math.pow(ph,2)+math.pow((midH),2))

        if (diagonal>100):
            tree = Octree()
            tree.octree(self.arr,mins,midD,midW,midH)
        else:
            self.choque()

    def choque(self):
        for bee in self.bees:
            print(str(bee.latitude) +", "+ str(bee.longitude) + ", " + str(bee.altitude))
r = Read()
r.reader("Prueba.txt")
j = Octree()

#str(bee.latitude) +", "+ str(bee.longitude) + ", " + str(bee.altitude)

