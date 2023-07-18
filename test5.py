import copy
import random

class Hat:
    def __init__(self, **kwargs):

        self.contents = list()

        # Create dict of hat contents
        for key,value in kwargs.items():
            for item in range(value):
                self.contents.append(key)
    
    def draw(self, num):
        # Shallow copy of contents
        drawn = copy.copy(self.contents)

        # Check if num of balls is valid
        if num > len(self.contents):
            return drawn

        # Delete from random indexes until new list is made
        while len(drawn) > num:
            del drawn[random.randint(0, len(drawn) - 1)]

        # Return list
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # Initialize counter for expected outcome
    probability_counter = 0

    # Iteration for each experiment
    for sim in range(num_experiments):

        # Shallow copy expected outcome
        expected_balls_copy = copy.copy(expected_balls)

        # Fetch randomized draw list
        drawn_list = hat.draw(num_balls_drawn)
        drawn_list.append("End of list")
            
        # Iterate over draw list
        for item in drawn_list:

            # Modify copied outcome dict if list item exists in it 
            if item in expected_balls_copy:
                if expected_balls_copy[item] == 1:
                    del expected_balls_copy[item]
                else:
                    expected_balls_copy[item] -= 1
                continue
            
            # Check if the dict is empty and add to counter
            if len(expected_balls_copy) == 0:
                probability_counter += 1
                break
                    
    # Return probability value
    return probability_counter / num_experiments





hat1 = Hat(blue=3,red=2,green=6)
probability1 = experiment(hat=hat1, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=100000)
print(probability1)
