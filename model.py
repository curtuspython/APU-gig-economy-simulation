import random
import global_vars
from mesa import Model
from mesa.time import SimultaneousActivation
from employer import Employer
from worker import Worker
import numpy as np


def modify_random_values(attribute):
    for i in range(0, len(attribute)):
        if attribute[i] > 0.9:
            attribute[i] = 0.90
        if attribute[i] < 0.2:
            attribute[i] = 0.20
        attribute[i] = round(attribute[i], 2)

    return attribute


class MarketModel(Model):
    """A model with 10 employers and employees."""

    def __init__(self, employer_count, worker_count, model_type, demand=True):
        self.regulating_wage = 0
        self.regulating_leisure = 0
        self.num_employers = employer_count
        self.num_workers = worker_count
        self.schedule = SimultaneousActivation(self)
        self.service_demand = list()

        # prepare gaussian distributed random values for agents.

        # 1
        self.skills = 0.5 + 0.12 * np.random.randn(1, 5000)
        self.skills = self.skills.tolist()
        self.skills = self.skills[0]
        self.skills = modify_random_values(self.skills)

        # 2
        self.flexibility = 0.5 + 0.12 * np.random.randn(1, 5000)
        self.flexibility = self.flexibility.tolist()
        self.flexibility = self.flexibility[0]
        self.flexibility = modify_random_values(self.flexibility)

        # 3
        self.tolerance = 0.5 + 0.12 * np.random.randn(1, 5000)
        self.tolerance = self.tolerance.tolist()
        self.tolerance = self.tolerance[0]
        self.tolerance = modify_random_values(self.tolerance)

        # 4
        self.revenue_potential = 0.5 + 0.12 * np.random.randn(1, 5000)
        self.revenue_potential = self.revenue_potential.tolist()
        self.revenue_potential = self.revenue_potential[0]
        self.revenue_potential = modify_random_values(self.revenue_potential)

        # 5
        self.employer_flex = 0.5 + 0.12 * np.random.randn(1, 10)
        self.employer_flex = self.employer_flex.tolist()
        self.employer_flex = self.employer_flex[0]
        self.employer_flex = modify_random_values(self.employer_flex)

        # Create agents
        n = 0
        intercept = 185
        diff1 = -20
        diff2 = -30
        if demand:
            for i in range(0, employer_count):
                self.service_demand.append(random.randint(50, 100))
        #  1-5 online employers
        x = 60
        intercept = intercept - diff1
        for i in range(int(self.num_employers / 2)):
            a = Employer(i, self, worker_count, x, 0.5, 1, intercept, self.service_demand[i], self.employer_flex[i])
            self.schedule.add(a)
            x = x + 10
        # 6-10 offline employers
        x = 100
        intercept = intercept + diff1
        for i in range(int(self.num_employers / 2)):
            a = Employer(int(self.num_employers / 2) + i, self, worker_count, x, 0.5, n, intercept,
                         self.service_demand[int(self.num_employers / 2) + i],
                         self.employer_flex[int(self.num_employers / 2) + i])
            self.schedule.add(a)
            x = x + 10

        # Leisure Preferring Model
        if model_type == 'leisure_preferring':
            for i in range(int(self.num_workers / 10) * 2):
                a = Worker(i + employer_count, self, employer_count, 100, 0.5, 200, 1)
                self.schedule.add(a)

            for i in range(int(self.num_workers / 10) * 3):
                a = Worker(int(self.num_workers / 10) * 2 + i + employer_count, self, employer_count, 150, 0.5, 200, 3)
                self.schedule.add(a)

            for i in range(int(self.num_workers / 10) * 5):
                a = Worker(5 * int(self.num_workers / 10) + i + employer_count, self, employer_count, 50, 0.5, 200, 2)
                self.schedule.add(a)

        # Wage Preferring Model
        elif model_type == 'wage_preferring':
            for i in range(int(self.num_workers / 10) * 4):
                a = Worker(i + employer_count, self, employer_count, 150, 0.5, 200, 1)
                self.schedule.add(a)

            for i in range(int(self.num_workers / 10) * 4):
                a = Worker(int(self.num_workers / 10) * 4 + i + employer_count, self, employer_count, 100, 0.5, 200, 3)
                self.schedule.add(a)

            for i in range(int(self.num_workers / 10) * 2):
                a = Worker(8 * int(self.num_workers / 10) + i + employer_count, self, employer_count, 50, 0.5, 200, 2)
                self.schedule.add(a)

        # This model corresponds to general form
        else:
            for i in range(int(self.num_workers / 5)):
                a = Worker(i + employer_count, self, employer_count, 100, 0.5, 200, 1, self.flexibility[i],
                           self.tolerance[i], self.revenue_potential[i], self.skills[i])
                self.schedule.add(a)

            for i in range(int(self.num_workers / 5)):
                a = Worker(int(self.num_workers / 5) + i + employer_count, self, employer_count, 150, 0.5, 200, 1,
                           self.flexibility[int(self.num_workers / 5) + i],
                           self.tolerance[int(self.num_workers / 5) + i],
                           self.revenue_potential[int(self.num_workers / 5) + i],
                           self.skills[int(self.num_workers / 5) + i])
                self.schedule.add(a)

            for i in range(int(self.num_workers / 5)):
                a = Worker(2 * int(self.num_workers / 5) + i + employer_count, self, employer_count, 50, 0.5, 200, 1,
                           self.flexibility[2 * int(self.num_workers / 5) + i],
                           self.tolerance[2 * int(self.num_workers / 5) + i],
                           self.revenue_potential[2 * int(self.num_workers / 5) + i],
                           self.skills[2 * int(self.num_workers / 5) + i])
                self.schedule.add(a)

            for i in range(int(self.num_workers / 5)):
                a = Worker(3 * int(self.num_workers / 5) + i + employer_count, self, employer_count, 75, 0.5, 200, 1,
                           self.flexibility[3 * int(self.num_workers / 5) + i],
                           self.tolerance[3 * int(self.num_workers / 5) + i],
                           self.revenue_potential[3 * int(self.num_workers / 5) + i],
                           self.skills[3 * int(self.num_workers / 5) + i])
                self.schedule.add(a)

            for i in range(int(self.num_workers / 5)):
                a = Worker(4 * int(self.num_workers / 5) + i + employer_count, self, employer_count, 125, 0.5, 200, 1,
                           self.flexibility[4 * int(self.num_workers / 5) + i],
                           self.tolerance[4 * int(self.num_workers / 5) + i],
                           self.revenue_potential[4 * int(self.num_workers / 5) + i],
                           self.skills[4 * int(self.num_workers / 5) + i])
                self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""
        for i in range(2):
            self.schedule.step()

    def unemployed_time_effect_wage(self, choice):
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                if agents.get_works_under() == -1:
                    agents.update_unemployed_time()
                    agents.decrease_reservation_wage_leisure(choice)
                else:
                    agents.mode = 1
        self.step()

    def unemployed_time_effect_leisure(self, choice):
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                if agents.get_works_under() == -1:
                    agents.update_unemployed_time()
                    agents.update_leisure(choice)
        self.step()

    def update_min_wages(self, minimum_wages):
        for agents in self.schedule.agents:
            if isinstance(agents, Employer):
                agents.set_minimum_wage(minimum_wages)
            else:
                if agents.get_works_under() == -1:
                    if agents.wage_preferred < minimum_wages:
                        agents.wage_preferred = minimum_wages

    def update_min_leisure(self, minimum_leisure):
        for agents in self.schedule.agents:
            if isinstance(agents, Employer):
                agents.set_minimum_leisure(minimum_leisure)
            else:
                if agents.get_works_under() == -1:
                    if agents.leisure_preferred < minimum_leisure:
                        agents.leisure_preferred = minimum_leisure

    def average_wages(self):
        """Obtaining average wages for helping the regulator"""
        wage = 0
        count = 0
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                if agents.get_works_under() == -1:
                    wage = wage + agents.get_wage_preferred()
                    count = count + 1
        wage = wage / count
        return wage

    def average_leisure(self):
        """Obtaining average leisure for helping the regulator"""
        leisure = 0
        count = 0
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                if agents.get_works_under() == -1:
                    leisure = leisure + agents.get_leisure_preferred()
                    count = count + 1
        leisure = leisure / count
        return leisure

    def average_wages_2(self):
        """Obtaining average wages for helping the regulator"""
        wage = 0
        count = 0
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                wage = wage + agents.get_wage_preferred()
                count = count + 1
        wage = wage / count
        return wage

    def average_leisure_2(self):
        """Obtaining average leisure for helping the regulator"""
        leisure = 0
        count = 0
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                leisure = leisure + agents.get_leisure_preferred()
                count = count + 1
        leisure = leisure / count
        return leisure

    def quadrant_update(self):
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                agents.update_quadrants()

    def step6(self):
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                if agents.works_under == -1:
                    agents.step()

    def improve_skills(self):
        """Method allowing worker agents to improve skills so as to get job."""
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                if agents.works_under == -1:
                    agents.improve_skill()

    def consumer_surplus(self):
        """Calculate the consumer surplus for all of the firms"""
        cs = 0
        wk = 0
        for agents in self.schedule.agents:
            if isinstance(agents, Employer):
                cs = cs + agents.consumer_surplus_for_employer()
                wk = wk + agents.get_workCount()
        return cs / 5000

    def set_regulating_wage(self):
        reg_wage = 0
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                reg_wage = reg_wage + agents.get_wage_preferred_threshold()

        self.regulating_wage = reg_wage / global_vars.M
        print("Regulating Wage: " + str(self.regulating_wage))

    def set_regulating_leisure(self):
        reg_leisure = 0
        for agents in self.schedule.agents:
            if isinstance(agents, Worker):
                reg_leisure = reg_leisure + agents.get_leisure_preferred_threshold()
        self.regulating_leisure = reg_leisure / global_vars.M
        print("Regulating Leisure: " + str(self.regulating_leisure))
