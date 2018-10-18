"""
Egg boiling demo.
A simple app to compute the time required to boil an egg based on its size
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

eggSize=ctrl.Antecedent(np.arange(40,70,0.5), 'Egg Size')
boilTime=ctrl.Consequent(np.arange(3,6,0.1), 'Boiling time')

eggSize['large'] = fuzz.zmf(eggSize.universe,40,70)
eggSize['small'] = fuzz.smf(eggSize.universe,40,70)

boilTime['short'] = fuzz.zmf(boilTime.universe,3,6)
boilTime['long']  = fuzz.smf(boilTime.universe,3,6)

#Simple conditional rules "IF antecedent THEN consequence"
rule1 = ctrl.Rule(eggSize['large'], boilTime['long'])
rule2 = ctrl.Rule(eggSize['small'], boilTime['short'])

#controller
boilerController=ctrl.ControlSystem([rule1,rule2])

#simulation
boilerSimulator=ctrl.ControlSystemSimulation(boilerController)

#input
boilerSimulator.input['Egg Size']=65
#process
boilerSimulator.compute()
#output
resultTime=boilerSimulator.output['Boiling time']
print(resultTime)


