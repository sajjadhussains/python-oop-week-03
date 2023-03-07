import math


class Distance:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def find_distance(self):
        dif1=self.x2-self.x1
        dif2 = self.y2 - self.y1
        result = math.sqrt((dif1**2+dif2**2))
        return result
new_obj = Distance(1,2,4,6)
print(new_obj.find_distance())