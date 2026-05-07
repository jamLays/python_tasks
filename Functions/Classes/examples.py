class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    pass

class Mammals(Animals):
    pass

class Giraffes(Mammals):
    pass

reginald = Giraffes()

class ThisIsMyClass:
    def this_is_class_function(self):
        print("this is a class function")
    def this_is_also_class_function(self):
        print("this is a class function")


class Animals(Animate):
    def breath(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass

class Mammals(Animals):
    def feed_with_milk(self):
        pass

class Giraffes(Mammals):
    def eat_trees_leaves(self):
        pass


reginald = Giraffes()
reginald.move()
reginald.eat_trees_leaves()

harold = Giraffes()
harold.move()


class Animals(Animate):
    def breath(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self, food):
        print('ест', food)

class Mammals(Animals):
    def feed_with_milk(self):
        print('кормит молоком')

class Giraffes(Mammals):
    def eat_trees_leaves(self):
        print('ест листья с деревьев')


# reginald = Giraffes()
# reginald.breath()
# reginald.eat_trees_leaves()
#
# harold = Giraffes()
# harold.move()

class Giraffes(Mammals):
    def __init__(self, weight):
        self.weight = weight

    def find_food(self):
        self.move()
        print('Я нашел еду!')
        self.eat_food()

    def eat_trees_leaves(self):
        print(self)
        self.eat_food("tres leaves")

    def dance_jig(self):
        self.move()
        self.move()

bigGiraff = Giraffes(150)
smallGiraff = Giraffes(100)


bigGiraff.eat_trees_leaves();
smallGiraff.eat_trees_leaves();

class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots

ozwald = Giraffes(100)
retrud = Giraffes(200)
print('oswald_spots number - ', ozwald.giraffe_spots)
print('retrud_spots number - ',retrud.giraffe_spots)

class Giraffes(Mammals):
    def left_foot_forward(self):
        print('левая нога впереди')
    def left_foot_back(self):
        print('левая нога сзади')
    def right_foot_forward(self):
        print('правая нога впереди')
    def right_foot_back(self):
        print('правая нога сзади')

    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()


harold = Giraffes()
harold.dance()










