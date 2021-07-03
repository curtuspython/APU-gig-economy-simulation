from pickle5 import pickle

import global_vars
from worker import Worker

with open('Models/demand.pkl', 'rb') as inputData:
    demand_model = pickle.load(inputData)


def set_regulating_wage(self):
    reg_wage = 0
    for agents in self.schedule.agents:
        if isinstance(agents, Worker):
            reg_wage = reg_wage + agents.get_wage_preferred()*0.9

    global_vars.regulatory_threshold_wage = reg_wage / global_vars.M
    print("Regulating Wage: " + str(global_vars.regulatory_threshold_wage))


def set_regulating_leisure(self):
    reg_leisure = 0
    for agents in self.schedule.agents:
        if isinstance(agents, Worker):
            reg_leisure = reg_leisure + agents.get_leisure_preferred()*0.9
    global_vars.regulatory_threshold_leisure = reg_leisure / global_vars.M
    print("Regulating Leisure: " + str(global_vars.regulatory_threshold_leisure))



