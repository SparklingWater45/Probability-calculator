import copy
import random
from typing import Counter
# Consider using the modules imported above.

class Hat:

    def __init__(self,**kwargs):
        self.balls_dict = {}
        self.contents = []
        self.total = 0
        
        for key,value in kwargs.items():
            self.balls_dict[key] = value
            self.total += value

        # print(self.total)
    
        for key,value in self.balls_dict.items():
            for i in range((value)):
                self.contents.append(key)
        
        # print('original contents = ',self.contents)
        
    def draw(self,num_ball):
        #draws random balls from contents array
        if num_ball > len(self.contents):
            return self.contents
        else: 
            output_balls = []

            for i in range(0,num_ball):
                rand_value = random.randint(0,len(self.contents)-1)
                output_balls.append(self.contents[rand_value])
                # self.contents.pop(rand_value)
                # self.total += -1
        
            # print('new contents ',self.contents)
            # print('output = ',output_balls)
            return output_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #creates dictionary of drawn items
    temp_dict = {}

    
    for i in range(num_experiments):
        temp_arr = hat.draw(num_balls_drawn)
        
        
        

hat = Hat(blue=4, green=6, red=2)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1,},
    num_balls_drawn=4,
    num_experiments=50)
# print("Probability:", probability)

# # Run unit tests automatically
# main(module='test_module', exit=False)
