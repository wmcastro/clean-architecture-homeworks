from interfaces.herbivorous import InterfaceHerbivorous

class Cow(InterfaceHerbivorous):
    def breathe(self):
        return "breathing..."
    
    def eat(self):
        return "eating..."
    
    def sleep(self):
        return "sleeping..."
    
    def eat_vegetables(self):
        return "eating grass..."
