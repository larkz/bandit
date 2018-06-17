import numpy as np 
import scipy as sc 
from scipy.stats import beta

class ThompsonExperiment:
    
    p_val = None
    a = None #number of successes
    b = None #number of failures

    def __init__(self, p):
        self.p_val = p
        self.a = 1
        self.b = 1
    
    def __play(self):
        return np.random.uniform() < self.p_val
            
    def playUpdate(self):
        if self.__play():
            self.a = self.a + 1 # add 1 to success
        else:
            self.b = self.b + 1 # add 1 to failure

    def sample(self): 
        return np.random.beta(self.a, self.b)


class ThompsonBandit:
    
    p_val = None
    a = None #number of successes
    b = None #number of failures
    num_plays = None

    def __init__(self, p):
        self.p_val = p
        self.a = 1
        self.b = 1
        self.num_plays = 0
    
    def sample(self):
        return float(np.random.beta(self.a, self.b))
        
    def play(self): 
        play_result = np.random.uniform() < self.p_val
        return play_result

    def play_update(self):
        self.num_plays = self.num_plays + 1
        if self.play():
            self.a = self.a + 1 # add 1 to success
        else:
            self.b = self.b + 1 # add 1 to failure
        

    






























