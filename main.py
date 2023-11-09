
# Marvish Chandra

# Milkshake randomizer based on the milkshake mixins from Five Guys

import random

def randmomizerMS():
    mixins = ["Chocolate","Strawberry","Banana","Peanut Butter","Salted Caramel","Whipped Cream","OREO Cookies","Bacon","Vanilla","OREO Creme","Double Stuf","Reese's Cups"]
    # must be able to select at least two mixins
    random.shuffle(mixins)
    print(mixins[0])
    print(mixins[1])

randmomizerMS()


def calorieCounter():
    calMixins = {"Chocolate": 40,"Strawberry": 20,"Banana": 30,"Peanut Butter": 90,"Salted Caramel": 45,"Whipped Cream": 20,"OREO Cookies" : 65,"Bacon": 80,"Vanilla": 20,"OREO Creme": 90,"Double Stuf": 60,"Reese's Cups": 60}
    print(calMixins["Chocolate"])

calorieCounter()





