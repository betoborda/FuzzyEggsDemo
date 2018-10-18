"""
Egg boiling demo.
A simple app to compute the time required to boil an egg based on its size
feel free to modify and taylor to your needs
developed for didactic purposes by @jmaquin0
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#the crisp values for egg size is the antecedent
eggSize=ctrl.Antecedent(np.arange(40,70,0.5), 'Egg Size')

#the boiling time is the consequent
boilTime=ctrl.Consequent(np.arange(3,6,0.1), 'Boiling time')

#Determine the fuzzy sets for antecedents
eggSize['large'] = fuzz.smf(eggSize.universe,40,70)
eggSize['small'] = fuzz.zmf(eggSize.universe,40,70)

#view the fuzzy set.
#eggSize.view() #uncoment the line to view graphic (it can fails in windows)


#Determine the fuzzy sets for antecedents
boilTime['short'] = fuzz.zmf(boilTime.universe,3,6)
boilTime['long']  = fuzz.smf(boilTime.universe,3,6)
#view the fuzzy set.
#boilTime.view() #uncoment the line to view graphic (it can fails in windows)


#Simple conditional rules "IF antecedent THEN consequence"
rule1 = ctrl.Rule(eggSize['large'], boilTime['long'])
rule2 = ctrl.Rule(eggSize['small'], boilTime['short'])

#controller
boilerController=ctrl.ControlSystem([rule1,rule2])

#simulation
boilerSimulator=ctrl.ControlSystemSimulation(boilerController)

#input
rawEggSize=float(input("please input the weight of the egg (from 40 to 70 grams)"))
#ensure that is in range
clippedEggSize=np.clip(rawEggSize,40,70)
#load the value in the simulator
boilerSimulator.input['Egg Size']=clippedEggSize
#process
boilerSimulator.compute()
#output
resultTime=boilerSimulator.output['Boiling time']
print("you need %1.2f minutes to boil that egg" %resultTime)


