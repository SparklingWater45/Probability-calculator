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
    
        for key,value in self.balls_dict.items():
            for i in range((value)):
                self.contents.append(key)
        
    def draw(self,num_ball):

        if num_ball > len(self.contents):
            return self.contents
        else: 
            output_balls = []
            for i in range(0,num_ball):
                rand_value = random.randint(0,len(self.contents)-1)
                output_balls.append(self.contents[rand_value])
                self.contents.pop(rand_value)
        
        return output_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
   
    #creates empty value dictionary of drawn items
    arr_drawn = []
    total = 0
    dict_drawn = {}
 
    for i in range(num_experiments):
        
        #make copy of object , otherwise the self.contents will become 0
        temp_hat = copy.deepcopy(hat)
        arr_drawn = temp_hat.draw(num_balls_drawn)
       
        
        #creates a key for all ball colours in hat
        #sets all keys to 0, for each loop run
        for i in hat.contents:
            dict_drawn[i] = 0
        
        #changes the keys in the dict to the amount of colours drawn
        for i in arr_drawn:
            dict_drawn[i] +=1

        temp_dict = {}
        
        for key in dict_drawn:
            if key in list(expected_balls.keys()):
                #if keys are equal then checks is correct
                if dict_drawn[key] >= expected_balls[key]:
                    temp_dict[key] = expected_balls[key]
                    
            #if created dictionary is the same as the expected
            if temp_dict == expected_balls:
                total +=1
    #m/n
    return total/num_experiments


    