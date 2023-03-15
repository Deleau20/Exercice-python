# tab = ["salut", 3, "bonsoir", 4]
# tab.pop(2)
# print(tab)


class Array:
    tab = []
    def __init__ (self,*args):
        self.tab = list(args)
        print(args)


    
    def linght(self):
        compter = 0
        for i in self.tab:
            compter += 1
        return compter
    


    def filter(self, filtre):
        bat = []
        for i in self.tab:
            if filtre(i):
                bat.append(i)
        return bat
    

    
    def mape(self, carre):
        carr =[]
        for i in self.tab:
            carr.append(carre(i))
        return carr
        
    def push(self, num):

        self.tab = self.tab + num
        return self.tab 


    def concat(self, tab_ext):
        for i in tab_ext:
            self.tab.append(i)
        return self.tab


a = Array(1,2,3,4,5,6)
b = a.push()
print(b)