import math

from mesa import Agent, Model
import numpy as np
import random
import global_vars


class Employer(Agent):
    """ An agent with fixed initial wealth."""
    work_count = 0

    def __init__(self, unique_id, model, N, n, prob, t, total, service_demand, flexibility):
        super().__init__(unique_id, model)
        self.prob = prob
        self.n = n
        self.increment_number = 0
        self.total = total
        self.demand = math.ceil((5000 / 1000) * service_demand)
        self.need = self.demand
        self.type = t + 1
        self.wage_offered = np.random.binomial(self.n, self.prob, 1)[0]
        self.leisure = np.random.binomial(total, self.prob, 1)[0] - self.wage_offered
        self.flexibility = flexibility
        self.workers = list()
        self.workers_potential = list()
        if Employer.work_count == 0:
            Employer.work_count = N
        self.profit = -1
        self.workers_reservation_wages = list()

    def acquire_worker(self, worker_id, worker_potential, wage):
        self.workers.append(worker_id)
        self.workers_potential.append(worker_potential)
        self.workers_reservation_wages.append(wage)
        self.need = self.need - 1

    def get_uniqueid(self):
        return self.unique_id

    def get_workCount(self):
        return len(self.workers)

    def get_wage_offered(self):
        return self.wage_offered

    def get_type(self):
        return self.type

    def get_leisure(self):
        return self.leisure

    def get_profit(self):
        return self.profit

    def get_emp_id(self):
        return self.unique_id

    def get_workers(self):
        return self.workers

    def get_flexibility(self):
        return self.flexibility

    def reset(self):
        self.workers = list()
        self.workers_potential = list()
        self.profit = -1

    def step(self):
        self.type = self.type

    def calculate_profit(self):
        profit = 0
        for i in range(len(self.workers)):
            profit = profit + self.workers_potential[i] - self.wage_offered
        self.profit = profit
        return profit

    def set_minimum_wage(self, minimum_wage):
        if self.wage_offered < minimum_wage:
            self.wage_offered = minimum_wage

    def set_minimum_leisure(self, minimum_leisure):
        if self.leisure < minimum_leisure:
            self.leisure = minimum_leisure

    def increase_wage_and_leisure(self):
        self.increment_number += 1
        if self.need == 0:
            return
        if self.increment_number == 1:
            if self.type == 2:
                x = self.leisure + self.leisure * 0.1
                if x >= 80:
                    self.leisure = 80
                else:
                    self.leisure = x
            else:

                x = self.wage_offered + self.wage_offered * 0.1
                if x >= 80:
                    self.wage_offered = 80
                else:
                    self.wage_offered = x

        else:
            if self.type == 1:
                x = self.leisure + self.leisure * 0.1
                if x >= 80:
                    self.leisure = 80
                else:
                    self.leisure = x
                self.wage_offered = self.wage_offered + self.wage_offered * 0.1
                if self.wage_offered > 80:
                    self.wage_offered = 80
            else:
                self.leisure = self.leisure + self.leisure * 0.1
                x = self.wage_offered + self.wage_offered * 0.1
                if x >= 80:
                    self.wage_offered = 80
                else:
                    self.wage_offered = x
                if self.leisure >= 80:
                    self.leisure = 80

    def get_need(self):
        return self.need

    def consumer_surplus_for_employer(self):
        c_surplus = 0
        for i in range(len(self.workers)):
            c_surplus = c_surplus + self.wage_offered - self.workers_reservation_wages[i]
        self.profit = c_surplus
        return c_surplus
