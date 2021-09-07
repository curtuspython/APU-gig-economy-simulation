import math
import random
import numpy as np
import model_outside
from employer import Employer
from model import MarketModel
import pandas as pd
import global_vars
import matplotlib.pyplot as plt
import model_features
from worker import Worker


def model_with_demand_constraint(choice=1):
    demand_model = MarketModel(global_vars.N, global_vars.M, 3, True)
    initial_demand = list()
    df = pd.DataFrame(columns=['Emp 1', 'Emp 2', 'Emp 3', 'Emp 4', 'Emp 5',
                               'Emp 6', 'Emp 7', 'Emp 8', 'Emp 9', 'Emp 10', 'Total'])
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        initial_demand.append(demand_model.schedule.agents[i].get_need())
    initial_demand.append(sum(initial_demand))
    df.loc[0] = initial_demand
    # This part finds out the initial wage and leisure for all the employers
    all_members = demand_model.schedule.agents
    if choice == 1:
        wage = list()
        leisure = list()
        for i in range(0, 10):
            wage.append(all_members[i].get_wage_offered())
            leisure.append(all_members[i].get_leisure())
        print("Wages:" + str(wage))
        print("Leisure" + str(leisure))
        wage.append(0)
        leisure.append(0)
        df.loc[1] = wage
        df.loc[2] = leisure
        df.to_csv('Models/initial.csv', index=False)
        return demand_model


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
    offline_wage = list()
    online_wage = list()
    freelancer_wage = list()
    skill_list = list()
    unemp_rates = list()
    profit_list = list()
    nums = np.ones(5000)
    nums[:5000] = 0
    np.random.shuffle(nums)
    agent_index = [i for i in range(10, 5010)]
    free_list = list()
    demand = print_demand(model)
    all_agents = model.schedule.agents
    count = 0
    avgval = 0
    revpot = 0
    avglei = 0
    while demand[-1] > 0 and count < 1:
        print("\n")
        print("Iteration" + str(count))
        print("--------------------------------")
        print("--------------------------------")
        avg_wage = model.average_wages()
        avg_leisure = model.average_leisure()
        wage.append(avg_wage)
        leisure.append(avg_leisure)
        random.shuffle(agent_index)
        skill = 0
        for i in agent_index[0:5000]:
            if choice == 1:
                all_agents[i].decrease_reservation_wage_leisure(10)

            else:
                if all_agents[i].beauty == 0:
                    skill = all_agents[i].skill + skill
                    avgval += model_outside.give_incentive(all_agents[i], 2)
                    all_agents[i].decrease_reservation_wage_leisure(11)
        skill_list.append(skill / 5000)
        demand = print_demand(model)
        model_outside.job_tenure_end(model)
        model.step()
        revpot = model_outside.revenue_potential(model)
        avglei = model_outside.leisure_average(model)
        profit = model_outside.profit_find(model);
        profit_list.append(sum(profit) / 10)
        count = count + 1
        model_features.analise(model)
        unemp_rates.append(global_vars.unemployment_rate)
        gig_non_gig = model_outside.get_urates(model)
        avg_Wages_extract = model_outside.avg_wage_job(model)
        online_wage.append(avg_Wages_extract[0])
        offline_wage.append(avg_Wages_extract[1])
        freelancer_wage.append(avg_Wages_extract[2])
        gig_list.append(gig_non_gig[0])
        ngig_list.append(gig_non_gig[2])
        free_list.append(gig_non_gig[4])
        avgval = avgval / (gig_non_gig[0] + gig_non_gig[2] + gig_non_gig[4])
    print("Aveage Revenue Generating potential: " + str(revpot))
    print("Average Leisure for the workers:" + str(avglei))
    print("Average Valuation: " + str(avgval))
    print("Unemployement Rates:" + str(unemp_rates))
    print("Online Employed " + str(gig_list))
    print("Offline Employed "+ str(ngig_list))
    print("Freelancer Employed" + str(free_list))

    for i in range(0, 10):
        all_agents[i].demand = math.ceil(0.1 * all_agents[i].demand) + all_agents[i].demand
        all_agents[i].need = math.ceil(0.1 * all_agents[i].demand) + all_agents[i].need

    print("Online_WAGE: " + str(online_wage))
    print("Offline_WAGE: " + str(offline_wage))
    print("Freelancer_WAGE: " + str(freelancer_wage))
    print("Skill: "+ str(skill_list))
    return [gig_list,ngig_list,free_list, online_wage,offline_wage,freelancer_wage, revpot, avglei, avgval]


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

    for i in updatefor:
        model_features.analise(demand_model)
        unemployment.append(global_vars.unemployment_rate)

        for k in updatefor:
            demand_model.schedule.agents[k].increase_wage_and_leisure()
        #model_outside.fire_from_job(demand_model)
        demand_model.step()
        profit = list()
        for pro in updatefor:
            profit.append(all_members[pro].calculate_profit())
        profit.append(sum(profit) / 10)
        demand = print_demand(demand_model)
        wage = list()
        leisurex = list()
        for avg in updatefor:
            wage.append(all_members[avg].get_wage_offered())
            leisurex.append(all_members[avg].get_leisure())
        wage_avg.append(sum(wage) / 10)
        leisure_avg.append(sum(leisurex) / 10)


def combined_model(demand_model):
    mask = [0 for i in range(0, 10)]
    nums = np.ones(5000)
    nums[:5000] = 0
    print(nums)
    np.random.shuffle(nums)
    count = 0
    a  = list()
    b = list()
    c = list()
    d = list()
    e = list()
    f = list()
    g = list()
    h = list()
    p = list()
    all_agents = demand_model.schedule.agents
    for agent in all_agents:
        if isinstance(agent, Worker):
            agent.pref_modes = nums[count]
            count = count + 1
    for i in range(0, 10):
        initial = print_demand(demand_model)
        x = self_regulating_worker(demand_model,2,1,5000)
        a.append(x[0])
        b.append(x[1])
        c.append(x[2])
        d.append(x[3])
        e.append(x[4])
        f.append(x[5])
        g.append(x[6])
        h.append(x[7])
        p.append(x[8])
        final = print_demand(demand_model)
        #model_outside.give_incentive(demand_model,1)
        mask = model_outside.updateornot(initial, final, mask)
        updatedfor = list()

        for j in range(len(mask)):
            if mask[j] == 4:
                updatedfor.append(j)
                mask[j] = 0
        print(updatedfor)
        updatedfor = list(filter(lambda x: x > 1, updatedfor))
        # if len(updatedfor) != 0:
            #self_regulating_employer(demand_model, updatedfor)
        all_members = demand_model.schedule.agents
        wage = 0
        leisure = 0
        for agent in all_agents:
            if isinstance(agent, Employer):
               wage = wage + agent.get_wage_offered()
               leisure = leisure + agent.get_leisure()
    wage = list()
    leisure = list()
    for i in range(0, 10):
        wage.append(all_members[i].get_wage_offered())
        leisure.append(all_members[i].get_leisure())
    print("Wage: " + str(wage))
    print("Leisure: " + str(leisure))
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(p)
