import math

class Vector2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001

    # Arithmetic Methods
    # These are the methods that will allow us to add and subtract vectors, 
    # as well as multiply and divide a vector by a scalar

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        if scalar != 0:
            return Vector2(self.x / float(scalar), self.y / float(scalar))
        return None

    def __truediv__(self, scalar):
        return self.__div__(scalar)
    
    # Equality Methods
    # These methods allow us to check for equality between two vectors.
    
    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False
        
    # We have two types of magnitude methods here.
    # The 'magnitude' method returns the actual length of the vector
    # which requires a square root.
    
    def magnitudeSquared(self):
        return self.x**2 + self.y**2

    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())
    
    # The copy method allows us to copy any vector so we get a new instance of it.
    # The reason we want to do this is because of how Python stores its variables in memory.
    # The last two methods are just nice to have.
    # They just convert our vector into a tuple and an int tuple.
    # They really just make code cleaner later. 

    def copy(self):
        return Vector2(self.x, self.y)

    def asTuple(self):
        return self.x, self.y

    def asInt(self):
        return int(self.x), int(self.y)
    
    # String Method
    # This method doesn't affect the functionality of the game or anything,
    # it's really a convenience function so we can easily print out the vector.


    def __str__(self):
        return "<"+str(self.x)+", "+str(self.y)+">"
    
    
        