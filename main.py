from entities.cow import Cow
from entities.dog import Dog


farm_cow = Cow()
farm_cow.breathe()
farm_cow.eat_vegetables()

house_dog = Dog()


print(f"Look! The cow is {farm_cow.breathe()} Surely, the cow was {farm_cow.eat_vegetables()} without any distractions.")
print(f"The dog of my house is {house_dog.eat_meet()} Did you know that the {house_dog.fang_size()}? Amazing!")