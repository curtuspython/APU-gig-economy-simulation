import copy
from model import MarketModel
import pandas as pd
import global_vars
import matplotlib.pyplot as plt
import numpy as np
import model_features
import call_n_plots
import pickle

np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

if __name__ == "__main__":
    with open('Models/demand.pkl', 'rb') as inputData:
        demand_model = pickle.load(inputData)
    # demand_model = call_n_plots.model_with_demand_constraint()
    # with open('Models/demand.pkl', 'wb') as output:
    #    pickle.dump(demand_model, output, pickle.HIGHEST_PROTOCOL)
    demand_model.set_regulating_wage()
    demand_model.set_regulating_leisure()
    demand_model = call_n_plots.dumb_model(demand_model)
    call_n_plots.self_regulating_worker(demand_model)

