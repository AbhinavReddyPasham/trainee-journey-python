class Vector2d:
    def __init__(self, x,y):
        self.x=x;
        self.y=y;  
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __repr__(self):
        
        return f"Vector2d({self.x},{self.y})"
v1=Vector2d(3,4)
v2=Vector2d(3,4)
v3=v1+v2
if v1==v2:
    print("v1 and v2 are equal")
print(v3.x,v3.y)
print(v3)