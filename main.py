
# Marvish Chandra

# Milkshake randomizer based on the milkshake mixins from Five Guys
import random

def randmomizerMS():
    mixinsDict = {"Chocolate": 40,"Strawberry": 20,"Banana": 30,"Peanut Butter": 90,"Salted Caramel": 45,"Whipped Cream": 20,"OREO Cookies": 65,"Bacon": 80,"Vanilla": 20,"OREO Creme": 90,"Double Stuf": 60,"Reese's Cups": 150}
    # must be able to select at least two mixins

    keys = mixinsDict()
    random.shuffle(keys)

    for mixin in keys:
        print(mixin, mixinsDict[mixin])




