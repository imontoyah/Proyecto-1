class hash_table:
    def __init__(self):
        self.table = [None] * 10

    def Hash_func(self, key):
        aux = 0
        for i in range(0,len(key)):
            aux += ord(key[i])
        return aux % 10
 
    def put(self,key,value): # Metodo para ingresar elementos
        hash = self.Hash_func(key)
        if self.table[hash] is None:
            self.table[hash] = (value,key)

    def get(self,key): # Metodo para buscar elementos
        hash = self.Hash_func(key)
        if self.table[hash] is None:
            return None
        else:
            return self.table[hash][0]

hash = hash_table()
hash.put('Isabella', 37158)
hash.put('Camilo', 455483)
hash.put('Inea', 54423)
hash.put('Fernando', 841172)
print(hash.get('Isabella'))
print(hash.get('Inea'))
print(hash.get('Fernando'))
print(hash.table)
