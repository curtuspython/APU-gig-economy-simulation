import copy
import math
import random

import numpy as np

import model_outside
from employer import Employer
from worker import Worker
from model import MarketModel
import pandas as pd
import global_vars
import matplotlib.pyplot as plt
import model_features
import pickle


def model_with_demand_constraint(choice=1):
    unemployment = list()
    demand_model = MarketModel(global_vars.N, global_vars.M, 3, True)
    initial_demand = list()
    df = pd.DataFrame(columns=['Emp 1', 'Emp 2', 'Emp 3', 'Emp 4', 'Emp 5',
                               'Emp 6', 'Emp 7', 'Emp 8', 'Emp 9', 'Emp 10', 'Total'])
    wage_leisure_track = pd.DataFrame(columns=['Employer 1', 'Employer 2', 'Employer 3', 'Employer 4', 'Employer 5',
                                               'Employer 6', 'Employer 7', 'Employer 8', 'Employer 9', 'Employer 10'])
    df2 = pd.DataFrame(columns=['Employer 1', 'Employer 2', 'Employer 3', 'Employer 4', 'Employer 5',
                                'Employer 6', 'Employer 7', 'Employer 8', 'Employer 9', 'Employer 10', 'Total'])
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        initial_demand.append(demand_model.schedule.agents[i].get_need())
    initial_demand.append(sum(initial_demand))
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
        wage.append(0)
        leisure.append(0)
        print("Wages:" + str(wage))
        print("Leisure" + str(leisure))
        df.loc[1] = wage
        df.loc[2] = leisure
        df.to_csv('Models/initial.csv', index=False)
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


def self_regulating_worker(model, choice, iterations, modes_count):
    wage = list()
    leisure = list()
    gig_list = list()
    ngig_list = list()
    skill_list = list()
    unemp_rates = list()
    profit_list = list()

    nums = np.ones(5000)
    nums[:5000] = 0
    np.random.shuffle(nums)
    agent_index = [i for i in range(10, 5010)]
    demand = print_demand(model)
    count = 0
    all_agents = model.schedule.agents
    '''
    for agent in all_agents:
        if isinstance(agent, Worker):
            agent.pref_modes = nums[count]
            count = count + 1
    '''
    count = 0
    while demand[-1] > 0 and count < 1:
        print("\n")
        print("Iteration" + str(count))
        print("--------------------------------")
        print("--------------------------------")
        avg_wage = model.average_wages()
        avg_leisure = model.average_leisure()
        wage.append(avg_wage)
        leisure.append(avg_leisure)
        if model.average_wages() < global_vars.regulatory_threshold_wage:
            print("Minimum wage introduced at " + str(count))
            #model.update_min_wages(global_vars.regulatory_threshold_wage)
            #model_outside.leave_job(model)
            # model_outside.fire_from_job(model)
        if model.average_leisure() < global_vars.regulatory_threshold_leisure:
            print("Minimum leisure introduced at " + str(count))
            #model.update_min_leisure(global_vars.regulatory_threshold_leisure)
            #model_outside.leave_job(model)
            # model_outside.fire_from_job(model)
        random.shuffle(agent_index)
        skill = 0
        for i in agent_index[0:5000]:
            if choice == 1:
                all_agents[i].decrease_reservation_wage_leisure(10)
            else:
                skill = all_agents[i].skill + skill
                all_agents[i].decrease_reservation_wage_leisure(11)
        skill_list.append(skill / 5000)
        demand = print_demand(model)
        model.step()

        profit = model_outside.profit_find(model);
        profit_list.append(sum(profit) / 10)
        count = count + 1
        print("Profit per firm:" + str(profit))
        print("Consumer Surplus :" + str(model.consumer_surplus()))
        model_features.analise(model)
        unemp_rates.append(global_vars.unemployment_rate)
        gig_non_gig = model_outside.get_urates(model)
        gig_list.append(gig_non_gig[0])
        ngig_list.append(gig_non_gig[2])
    print("Profit:" + str(profit_list))
    print("Wage" + str(wage))
    print("Leisure" + str(leisure))
    print("Unemployement Rates:" + str(unemp_rates))
    print("Skill :" +str(skill_list))
    print(str(gig_list))
    print(str(ngig_list))

    if choice == 1:
        with open('Models/demand_after15rounds10.pkl', 'wb') as output:
            pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)
    if choice == 2:
        with open('Models/demand_after15rounds11.pkl', 'wb') as output:
            pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)
    # increase the demands
    for i in range(0, 10):
        all_agents[i].demand = math.ceil(0.1 * all_agents[i].demand) + all_agents[i].demand
        all_agents[i].need = math.ceil(0.1 * all_agents[i].demand) + all_agents[i].need

    print("wage::::::::::" + str(wage))
    print("Leisure:::::::" + str(leisure))


def self_regulating_employer(demand_model, updatefor):
    print("Printing the employer work")
    unemployment = list()
    initial_demand = list()
    wage_avg = list()
    leisure_avg = list()
    for i in updatefor:
        initial_demand.append(demand_model.schedule.agents[i].get_need())
    initial_demand.append(sum(initial_demand))
    print(initial_demand)
    # This part finds out the initial wage and leisure for all the employers
    all_members = demand_model.schedule.agents
    wage = list()
    leisure = list()
    for i in updatefor:
        wage.append(all_members[i].get_wage_offered())
        leisure.append(all_members[i].get_leisure())
    print("Wage: " + str(wage))
    print("Leisure: " + str(leisure))

    for i in updatefor:
        model_features.analise(demand_model)
        unemployment.append(global_vars.unemployment_rate)

        for k in updatefor:
            demand_model.schedule.agents[k].increase_wage_and_leisure()
        # model_outside.fire_from_job(demand_model)
        demand_model.step()
        profit = list()
        for pro in updatefor:
            profit.append(all_members[pro].calculate_profit())
        profit.append(sum(profit) / 10)
        print("Profit: " + str(profit))
        print("Consumer Surplus : " + str(demand_model.consumer_surplus()))
        demand = print_demand(demand_model)
        print(demand)
        print("-----------------------------------------------------------------------")
        print(".......................................................................")
        wage = list()
        leisurex = list()
        for avg in updatefor:
            wage.append(all_members[avg].get_wage_offered())
            leisurex.append(all_members[avg].get_leisure())
        wage_avg.append(sum(wage) / 10)
        leisure_avg.append(sum(leisurex) / 10)
        print(str(wage_avg))
        print(str(leisure_avg))
    wage = list()
    leisure = list()
    for i in updatefor:
        wage.append(all_members[i].get_wage_offered())
        leisure.append(all_members[i].get_leisure())
    print("Wage: " + str(wage))
    print("Leisure: " + str(leisure))
    print("Wage avg: " + str(wage_avg))
    print("Leisure avg: " + str(leisure_avg))


def combined_model(demand_model):
    mask = [0 for i in range(0, 10)]
    nums = np.ones(5000)
    nums[:4000] = 0
    print(nums)
    np.random.shuffle(nums)
    agent_index = [i for i in range(10, 5010)]
    count = 0
    all_agents = demand_model.schedule.agents
    for agent in all_agents:
        if isinstance(agent, Worker):
            agent.pref_modes = nums[count]
            count = count + 1
    for i in range(0, 7):
        initial = print_demand(demand_model)
        self_regulating_worker(demand_model, 2, 1, 4000)
        final = print_demand(demand_model)
        mask = model_outside.updateornot(initial, final, mask)
        updatedfor = list()
        for j in range(len(mask)):
            if mask[j] == 4:
                updatedfor.append(j)
                mask[j] = 0
        print(updatedfor)
        if len(updatedfor) != 0:
            self_regulating_employer(demand_model, updatedfor)
        all_members = demand_model.schedule.agents
        wage = 0
        leisure = 0
        for agent in all_agents:
            if isinstance(agent, Employer):
               wage = wage + agent.get_wage_offered()
               leisure = leisure + agent.get_leisure()
        print("Avergeeeee Wage" + str(wage/10))
        print("Averageeee Leisure" + str(leisure/10))
    wage = list()
    leisure = list()
    for i in range(0, 10):
        wage.append(all_members[i].get_wage_offered())
        leisure.append(all_members[i].get_leisure())
    print("Wage: " + str(wage))
    print("Leisure: " + str(leisure))
