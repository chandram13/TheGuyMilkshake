
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





