#capitalise classes; Point, BrianBrady
#__int__ is constructor, let class be used without defined x/y parameters
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(15, 20)
print(point.x)
