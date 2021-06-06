import copy
import random
from model import MarketModel
import pandas as pd
import global_vars
import matplotlib.pyplot as plt
import model_features
import pickle
import numpy as np


def model_with_demand_constraint(choice=1):
    unemployment = list()
    demand_model = MarketModel(global_vars.N, global_vars.M, 3, True)
    initial_demand = list()

    df = pd.DataFrame(columns=['Employer 1', 'Employer 2', 'Employer 3', 'Employer 4', 'Employer 5',
                               'Employer 6', 'Employer 7', 'Employer 8', 'Employer 9', 'Employer 10', 'Total'])
    wage_leisure_track = pd.DataFrame(columns=['Employer 1', 'Employer 2', 'Employer 3', 'Employer 4', 'Employer 5',
                                               'Employer 6', 'Employer 7', 'Employer 8', 'Employer 9', 'Employer 10'])
    df2 = pd.DataFrame(columns=['Employer 1', 'Employer 2', 'Employer 3', 'Employer 4', 'Employer 5',
                                'Employer 6', 'Employer 7', 'Employer 8', 'Employer 9', 'Employer 10', 'Total'])
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        initial_demand.append(demand_model.schedule.agents[i].get_need())
    initial_demand.append(sum(initial_demand))
    print("Initial Demand of Employers:" + str(initial_demand))
    df.loc[0] = initial_demand
    # This part finds out the initial wage and leisure for all the employers
    all_members = demand_model.schedule.agents
    # initial case when model is not saved.
    if choice == 1:
        wage = list()
        leisure = list()
        for i in range(0, 10):
            wage.append(all_members[i].get_wage_offered())
            leisure.append(all_members[i].get_leisure())
        print("Wages:" + str(wage))
        print("Leisure" + str(leisure))
        return demand_model
        wage_leisure_track.loc[0] = wage
        wage_leisure_track.loc[1] = leisure
        consumer_surplus = list()

        for i in range(0, 10):
            demand_model.step()
            profit = list()
            for pro in range(0, 10):
                profit.append(all_members[pro].calculate_profit())
            profit.append(sum(profit) / 10)
            df2.loc[i] = profit
            print(profit)
            model_features.analise(demand_model)
            unemployment.append(global_vars.unemployment_rate)
            needs = list()
            for j in range(0, 10):
                needs.append(demand_model.schedule.agents[j].get_need())
            needs.append(sum(needs))
            df.loc[i + 1] = needs
            for k in range(0, 10):
                demand_model.schedule.agents[k].increase_wage_and_leisure()
                demand_model.step6()
            consumer_surplus.append(demand_model.consumer_surplus())
            print(consumer_surplus)

        wage = list()
        leisure = list()
        for i in range(0, 10):
            wage.append(all_members[i].get_wage_offered())
            leisure.append(all_members[i].get_leisure())
        print(wage)
        print(leisure)
        wage_leisure_track.loc[2] = wage
        wage_leisure_track.loc[3] = leisure
        print(consumer_surplus)
        with open('demand.pkl', 'wb') as output:
            pickle.dump(demand_model, output, pickle.HIGHEST_PROTOCOL)
        df.to_csv('demand_results3.csv', index=False)
        df2.to_csv('profit3.csv', index=False)
        wage_leisure_track.to_csv('wages_and_leisure3.csv', index=False)
        df.to_csv('demand_results4.csv', index=False)
        df2.to_csv('profit4.csv', index=False)
        wage_leisure_track.to_csv('wages_and_leisure4.csv', index=False)


def print_demand(demand_model):
    initial_demand = list()
    for i in range(0, global_vars.N):
        initial_demand.append(demand_model.schedule.agents[i].get_need())
    initial_demand.append(sum(initial_demand))
    return initial_demand


def dumb_model(demand_model):
    print("Initial Demand : ")
    initial_demand = print_demand(demand_model)
    print(str(initial_demand))

    demand_model.step()
    model_features.analise(demand_model)
    print("Final Demand : ")
    final_demand = print_demand(demand_model)
    print(str(final_demand))

    # Calculating Profit
    all_agents = demand_model.schedule.agents
    profit = list()
    for pro in range(0, 10):
        profit.append(all_agents[pro].calculate_profit())
    profit.append(sum(profit) / 10)
    print(profit)

    x = ['Emp 1', 'Emp 2', 'Emp 3', 'Emp 4', 'Emp 5',
         'Emp 6', 'Emp 7', 'Emp 8', 'Emp 9', 'Emp 10', 'Total']
    x_axis = np.arange(len(x))

    plt.bar(x_axis - 0.2, initial_demand, 0.4, label='Initial Demand')
    plt.bar(x_axis + 0.2, final_demand, 0.4, label='Final Demand')

    plt.xticks(x_axis, x)
    plt.xlabel("Employers")
    plt.ylabel("Demand")
    plt.title("Demand before and after")
    plt.legend()
    plt.show()
    return demand_model


def self_regulating_worker( model):
    print()
    agent_index = [i for i in range(10, 5010)]
    demand = print_demand(model)
    count = 0
    all_agents = model.schedule.agents
    while demand[-1] > 0 and count < 10:

        random.shuffle(agent_index)
        for i in agent_index[0:3000]:
            all_agents[i].decrease_reservation_wage_leisure(10)
            all_agents[i].step()
        count = count + 1
        demand = print_demand(model)
        print(demand)