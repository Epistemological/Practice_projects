
#normal usage of methods
ml = [5,9,3,6,8,11,4,3]
ml.sort()
min(ml)
max(ml)
ml.remove(5)
#create new class

class mylist(list):
    def remove_min(self): #instance method
        self.remove(min(self))
    def remove_max(self): #instance method
        self.remove(max(self))

x = [1,2,3,4,5,6,7,8]

y = mylist(x)
dir(y)
y.remove_min()
print(y)
y.remove_max()
print(y)



