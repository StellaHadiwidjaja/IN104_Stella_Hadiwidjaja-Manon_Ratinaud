# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:07:54 2021

@author: a2ste
"""

class Sharks:
    def __init__(self,name,home,weight):
        self.name = name
        self.home = home
        self.weight = weight
        
    def getName(self):
        return self.name
    
    def swimGracefully(self):
        print("Wow, " + self.getName() + " is swimming so gracefully!")
        
        
class Whale_Sharks(Sharks):
    def __init__(self, name, home,weight, snacks, personality):
        super().__init__(name, home,weight)
        self.favoritesnack = snacks
        self.personality = personality
        
        
    def krillTime(self,snackWeight):
        self.weight += snackWeight
        print("Yummy! " + self.getName() + " ate " + str(snackWeight) + " kilos of " + self.favoritesnack )
        print(self.weight)
        
    def beCute(self):
        print("Awww, issoo cuteee!")
    
        
class Great_Whites(Sharks):
    def __init__(self, name, home,weight, teeth, age):
        super().__init__(name, home,weight)
        self.teeth = teeth
        self.age = age

    def scareHumans(self):
        print("So many teeth! Humans are scared" )
        
    def teethReplacement(self):
        self.teeth += 100
        print(self.getName()+ " has more teeth!")
        
james = Whale_Sharks("James","Gorontalo, Indonesia", 1000,"Krill","Friendly")
sharky = Great_Whites("Sharky","Guadalupe",1000,100,10)