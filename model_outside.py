from random import random

from pickle5 import pickle

import global_vars
from employer import Employer
from worker import Worker


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
                # if agents.wage_preferred < global_vars.regulatory_threshold_wage or agents.leisure_preferred <
                # global_vars.regulatory_threshold_leisure:
                if agents.more_tolerances <=0:
                    agents.reset(all_agents[agents.get_works_under()])
                    count = count + 1
    print("Workers leaving job:" + str(count))


def fire_from_job(model):
    all_agents = model.schedule.agents
    count = 0;
    for agents in model.schedule.agents:
        if isinstance(agents, Employer):
            for i in agents.get_workers():
                if all_agents[i].revenue_potential * all_agents[i].skill > agents.get_wage_offered() * (
                        1 - agents.get_flexibility()):
                    all_agents[i].reset(agents)
                    count = count + 1
    print("Fired form job:" + str(count))


def give_incentive(agent, typee, model):
    all_agents = model.schedule.agents
    if agent.works_under != -1:
        flag = False
        if agent.skill >= 0.5 and agent.type == 1:

            agent.agreed_wage = (1 + 0.06 * agent.skill) * agent.agreed_wage
            agent.agreed_leisure = (1 + 0.05 * agent.skill) * agent.agreed_leisure
            agent.revenue_potential = (1 + 0.1 * agent.skill) * agent.revenue_potential
            if typee == 1:
                flag = True
                agent.u_temp = agent.wage_coef * agent.agreed_wage + agent.lei_coef * agent.agreed_leisure
            if not flag:
                    agent.more_tolerances -= 1

        return agent.u_temp
    return agent.u_temp


def profit_find(model, typee):
    all_agents = model.schedule.agents
    profit = 0
    count1 = 0
    count2 = 0
    profit_list = list()
    for agents in model.schedule.agents:
        if isinstance(agents, Employer) and agents.type == 1:
            profit = 0
            for i in agents.get_workers():
                if typee == 1 :# not cheating
                    profit = profit + (all_agents[i].revenue_potential - all_agents[i].agreed_wage)
                if typee == 2: # cheating
                    profit = profit + (all_agents[i].revenue_potential - all_agents[i].wage_preferred)
            profit_list.append(profit)
    return profit_list


def get_urates(model):
    gig_count = 0
    ngig_count = 0
    gig_emp = 0
    ngig_emp = 0
    freelancer_emp = 0
    freelancer_count = 0
    all_agents = model.schedule.agents
    for agent in all_agents:
        if isinstance(agent, Worker):
            if agent.type == 1 and agent.beauty == 0:
                gig_count += 1
                if agent.works_under != -1:
                    gig_emp += 1
            elif agent.type == 2 and agent.beauty == 0:
                ngig_count += 1
                if agent.works_under != -1:
                    ngig_emp += 1
            else:
                freelancer_count += 1
                if agent.works_under != -1:
                    freelancer_emp += 1
    print(gig_emp)
    print(gig_count)
    print(ngig_emp)
    print(ngig_count)
    print(freelancer_emp)
    print(freelancer_count)
    return [gig_emp, gig_count, ngig_emp, ngig_count, freelancer_emp, freelancer_count]


def job_tenure_end(model):
    all_agents = model.schedule.agents
    for i in model.schedule.agents:
        if isinstance(i, Worker):
            if i.duration == 500:
                continue
            elif 500 > i.duration > 0:
                i.duration = i.duration - 1
            elif i.get_works_under() != -1:
                i.reset(all_agents[i.get_works_under()])


def avg_wage_job(model):
    all_agents = model.schedule.agents
    avg_offline = 0
    avg_online = 0
    avg_freelancer = 0
    count_online = 0
    count_offline = 0
    count_freelancer = 0
    for i in all_agents:
        if isinstance(i, Worker):
            if i.beauty == 1:
                avg_freelancer = avg_freelancer + i.wage_preferred
                count_freelancer += 1
            elif i.type == 2:
                avg_offline = avg_offline + i.wage_preferred
                count_offline += 1
            else:
                avg_online = avg_online + i.wage_preferred
                count_online += 1
    return [avg_online / count_online, avg_offline / count_offline, avg_freelancer / count_freelancer]


def revenue_potential(model):
    rev = 0
    count = 0
    for agents in model.schedule.agents:
        if isinstance(agents, Worker) and agents.type == 1:
            count += 1
            rev += agents.revenue_potential
    return rev / count


def leisure_average(model):
    lei = 0
    count = 0
    lei2 = 0
    for agents in model.schedule.agents:
        if isinstance(agents, Worker):
            if agents.works_under != -1 and agents.type == 1:
                lei += agents.get_leisure_preferred()
                lei2 += agents.agreed_leisure
                count += 1

    return [lei / count, lei2 / count]


def wage_average(model):
    lei = 0
    count = 0
    lei2 = 0
    for agents in model.schedule.agents:
        if isinstance(agents, Worker):
            if agents.works_under != -1 and agents.type == 1:
                lei += agents.get_wage_preferred()
                lei2 += agents.agreed_wage
                count += 1

    return [lei / count, lei2 / count]


