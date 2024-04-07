from interfaces.carnivorous import InterfaceCarnivorous

class Dog(InterfaceCarnivorous):
    def breathe(self):
        return "breathing..."
    
    def eat(self):
        return "eating..."
    
    def sleep(self):
        return "sleeping..."
    
    def eat_meet(self):
        return "eating chicken..."
    
    def fang_size(self):
        return "dog's teeth are 28mm"
    
