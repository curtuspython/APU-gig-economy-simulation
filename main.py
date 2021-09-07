import copy

import model_outside
from model import MarketModel
import pandas as pd
import global_vars
import matplotlib.pyplot as plt
import numpy as np
import model_features
import call_n_plots
import pickle5 as pickle
import model_outside as mo

np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

if __name__ == "__main__":
    with open('Models/beauty_workers_1.pkl', 'rb') as inputData:
        demand_model = pickle.load(inputData)
    demand_model = call_n_plots.model_with_demand_constraint()
    #with open('Models/beauty_workers_1.pkl', 'wb') as output:
    #    pickle.dump(demand_model, output, pickle.HIGHEST_PROTOCOL)
    mo.set_regulating_leisure(demand_model)
    mo.set_regulating_wage(demand_model)
    print("################################### Model 1 ########################################")
    demand_model = call_n_plots.dumb_model(demand_model)
    demand_model_skill = copy.deepcopy(demand_model)
    demand_model_employer = copy.deepcopy(demand_model)
    print("Model 2 for beauty workers")
    call_n_plots.combined_model(demand_model)
