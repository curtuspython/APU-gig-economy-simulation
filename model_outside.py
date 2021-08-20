from pickle5 import pickle

import global_vars
from employer import Employer
from worker import Worker

with open('Models/demand.pkl', 'rb') as inputData:
    demand_model = pickle.load(inputData)


def set_regulating_wage(self):
    reg_wage = 0
    for agents in self.schedule.agents:
        if isinstance(agents, Worker):
            reg_wage = reg_wage + agents.get_wage_preferred() * 0.9

    global_vars.regulatory_threshold_wage = reg_wage / global_vars.M
    print("Regulating Wage: " + str(global_vars.regulatory_threshold_wage))


def set_regulating_leisure(self):
    reg_leisure = 0
    for agents in self.schedule.agents:
        if isinstance(agents, Worker):
            reg_leisure = reg_leisure + agents.get_leisure_preferred() * 0.9
    global_vars.regulatory_threshold_leisure = reg_leisure / global_vars.M
    print("Regulating Leisure: " + str(global_vars.regulatory_threshold_leisure))


def updateornot(initial, final, mask):
    list1 = mask
    z = 1
    list2 = list()
    for i in range(0, 10):
        if final == 0:
            continue
        if (initial[i] - final[i]) > 0.1 * initial[i]:
            list2.append(0)
        else:
            list2.append(1)

    zipped_lists = zip(list1, list2)
    sum = [x + y for (x, y) in zipped_lists]
    return sum


def leave_job(model):
    all_agents = model.schedule.agents
    count = 0
    for agents in model.schedule.agents:
        if isinstance(agents, Worker):
            if agents.get_works_under() != -1:
                if agents.wage_preferred < global_vars.regulatory_threshold_wage or agents.leisure_preferred < global_vars.regulatory_threshold_leisure:
                    agents.reset(all_agents[agents.get_works_under()])
                    count = count + 1
    print("Workers leaving job:" + str(count))


def fire_from_job(model):
    all_agents = model.schedule.agents
    count=0;
    for agents in model.schedule.agents:
        if isinstance(agents, Employer):
            for i in agents.get_workers():
                if all_agents[i].revenue_potential * all_agents[i].skill > agents.get_wage_offered() * (1 - agents.get_flexibility()):
                    all_agents[i].reset(agents)
                    count = count + 1
    print("Fired form job:" + str(count))


def give_incentive(model):
    all_agents = model.schedule.agents
    count = 0
    for agent in all_agents:
        if isinstance(agent, Worker):
            if agent.works_under != -1 and agent.type == 1:
                if agent.skill >= 0.5:
                    agent.wage_preferred = (1 + 0.1 * agent.skill)*agent.wage_preferred
                    agent.revenue_potential = (1 + 0.05 * agent.skill) * agent.revenue_potential


def profit_find(model):
    all_agents = model.schedule.agents
    profit = 0
    profit_list = list()
    for agents in model.schedule.agents:
        if isinstance(agents, Employer):
            profit = 0
            for i in agents.get_workers():
                profit = profit + (all_agents[i].revenue_potential - all_agents[i].wage_preferred)
            profit_list.append(profit)
    return profit_list


def get_urates(model):
    gig_count =0
    ngig_count = 0
    gig_emp = 0
    ngig_emp = 0
    all_agents = model.schedule.agents
    for agent in all_agents:
        if isinstance(agent,Worker):
            if agent.type == 1:
                gig_count += 1
                if agent.works_under != -1:
                    gig_emp +=1
            else:
                ngig_count +=1
                if agent.works_under != -1:
                    ngig_emp += 1

    print(gig_emp)
    print(gig_count)
    print(ngig_emp)
    print(ngig_count)
    return [gig_emp, gig_count, ngig_emp, ngig_count]




