import math
from random import *
from abc import ABC, abstractmethod

class DefenseStrategy(ABC):
    """Abstract class of defense method"""
    @ abstractmethod
    def defense(self, dmg,mask):
        return "Please implement this method"
  
class B_lucky(DefenseStrategy):
    def defense(self,dmg,mask):
        mask.used_time+=300
        return choice([0,0,0,0,int(0.5*dmg),int(0.8*dmg),dmg])
    
class A_lucky(DefenseStrategy):
    def defense(self,dmg,mask):
        mask.used_time+=250
        return choice([0,0,0,0,0,int(0.5*dmg)]) 
    