from employer import Employer
import matplotlib.pyplot as plt
import global_vars

plt.rcParams['figure.figsize'] = (10, 10)


def analise(empty_model):
    profit = list()
    number_of_workers = list()
    counter = 0
    unemployed_preferred_wages = list()
    unemployed_preferred_leisure = list()
    wages_e_on = list()
    lei_e_on = list()
    wages_e_of = list()
    lei_e_of = list()
    types = list()
    wages_e = list()
    lei_e = list()
    count = 0
    color = list()
    util = list()
    global_vars.offline_worker = 0
    global_vars.online_worker = 0
    # for agent in empty_model.schedule.agents:
    #    if isinstance(agent, Employer):
    #        agent.calculate_profit()
    for agent in empty_model.schedule.agents:
        counter += 1
        if isinstance(agent, Employer):
            number_of_workers.append(len(agent.workers))
            profit.append(agent.get_profit())

    all_agents = empty_model.schedule.agents
    # fetch the data for plotting the graphs
    for agent in all_agents:
        if isinstance(agent, Employer):
            wages_e.append(agent.get_wage_offered())
            lei_e.append(agent.get_leisure())
            types.append(agent.get_type())
            util.append(0)
            if agent.get_type() == 1:
                wages_e_on.append(agent.get_wage_offered())
                lei_e_on.append(agent.get_leisure())
            else:
                wages_e_of.append(agent.get_wage_offered())
                lei_e_of.append(agent.get_leisure())
            if len(agent.get_workers()) > 0:
                # adding the list of all the workers of each employee to the color named list.
                color.append(agent.get_workers())
                count = count + 1
            else:
                color.append(None)
        else:
            util.append(agent.get_utility())
            # Here the employed and unemployed agents are counted.
            # if agent.get_works_under() == -1:
            #    unemployed_preferred_wages.append(agent.get_wage_preferred())
            #    unemployed_preferred_leisure.append(agent.get_leisure_preferred())
            if agent.get_type() == 1:
                global_vars.online_worker += 1
            else:
                global_vars.offline_worker += 1
    # Finding the W. The total number of employed workers.
    global_vars.employed_count = 0
    for employee in range(global_vars.N):
        global_vars.employed_count = global_vars.employed_count + len(all_agents[employee].workers)

    # Finding the unemployment rate.
    global_vars.unemployment_rate = 1 - global_vars.employed_count / (len(all_agents) - global_vars.N)
    print("Employed count: " + str(global_vars.employed_count))
    print("Unemployment Rate: " + str(global_vars.unemployment_rate))