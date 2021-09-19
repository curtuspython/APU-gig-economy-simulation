from mesa import Agent
import numpy as np
import random
import global_vars


class Worker(Agent):
    """ A worker agent."""
    emp_count = 0

    def __init__(self, unique_id, model, M, n, prob, total, t_o_w, flexibility, tolerance, revenue_potential, skill, pref_modes):
        super().__init__(unique_id, model)
        self.prob = prob
        self.u_temp = 0
        self.more_tolerances = 4
        self.reduce_wage = False
        self.pref_modes = pref_modes
        self.n = n
        self.agreed_wage = 0
        self.agreed_leisure = 0
        self.beauty = 0
        self.duration = 500
        self.wage_preferred = np.random.binomial(self.n, self.prob, 1)[0]
        self.type = random.randint(1, 2)
        self.leisure_preferred = np.random.binomial(total, self.prob, 1)[0] - self.wage_preferred
        if self.type == 1:
            self.wage_coef = np.random.binomial(50, self.prob, 1)[0] / 100
            self.lei_coef = np.random.binomial(total, self.prob, 1)[0] / 100 - self.wage_coef
            self.reduce_wage = False
        else:
            self.wage_coef = np.random.binomial(150, self.prob, 1)[0] / 100
            self.lei_coef = np.random.binomial(total, self.prob, 1)[0] / 100 - self.wage_coef
            self.reduce_wage = True
        self.loyalty = random.randint(1, 10)
        self.utility = 0
        self.flexibility = flexibility
        self.tolerance = 10 * tolerance
        self.revenue_potential = 100 * revenue_potential
        self.skill = skill
        self.works_under = -1
        self.mode = 0
        self.unemployed_duration = np.floor(np.random.normal(global_vars.mu, global_vars.sigma, 1))
        self.employed_duration = 0
        if self.unemployed_duration > 60:
            self.unemployed_duration = 60
        if self.unemployed_duration < 0:
            self.unemployed_duration = 0
        if Worker.emp_count == 0:
            Worker.emp_count = M

        self.leisure_preferred_threshold = self.leisure_preferred - 0.3 * self.leisure_preferred
        self.wage_preferred_threshold = self.wage_preferred - 0.3 * self.wage_preferred

        self.operating_quadrant = 0
        if self.wage_preferred >= 50 and self.leisure_preferred >= 50:
            self.operating_quadrant = 1
        elif self.wage_preferred < 50 and self.leisure_preferred >= 50:
            self.operating_quadrant = 2
        elif self.wage_preferred >= 50 and self.leisure_preferred < 50:
            self.operating_quadrant = 4
        else:
            self.operating_quadrant = 3

    def get_wage_preferred_threshold(self):
        return self.wage_preferred_threshold

    def get_leisure_preferred_threshold(self):
        return self.leisure_preferred_threshold

    def get_works_under(self):
        return self.works_under

    def get_wage_preferred(self):
        return self.wage_preferred

    def get_leisure_preferred(self):
        return self.leisure_preferred

    def get_uniqueid(self):
        return self.unique_id

    def get_wage_coef(self):
        return self.wage_coef

    def get_leisure_coef(self):
        return self.lei_coef

    def get_emp_count(self):
        return Worker.emp_count

    def get_id(self):
        return self.unique_id

    def get_type(self):
        return self.type

    def get_utility(self):
        return self.utility

    def get_loyalty(self):
        return self.loyalty

    def get_tolerance(self):
        return self.tolerance

    def change_type(self):
        if self.type == 1:
            self.type = 2
        else:
            self.type = 1

    def reset(self, agent):
        self.utility = 0
        self.works_under = -1
        self.more_tolerances = 0
        index = agent.workers.index(self.unique_id)
        agent.workers.remove(self.unique_id)
        agent.workers_potential.pop(index)

    def step(self):
        if self.works_under == -1:
            emp = self.model.schedule.agents[0]
            flag = -1
            employers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(employers)
            for i in employers:
                obj = self.model.schedule.agents[i]
                u = self.wage_coef * obj.get_wage_offered() + self.lei_coef * obj.get_leisure()
                if self.u_temp < u:
                    self.u_temp = u
                if self.type == obj.get_type():
                    # hiring of worker j by Employer i
                    if self.utility < u and self.wage_preferred <= obj.get_wage_offered() and self.leisure_preferred <= obj.get_leisure() and obj.get_need() > 0:
                        if self.revenue_potential * self.skill > obj.get_wage_offered() * (1 - obj.get_flexibility()):
                            self.utility = u
                            self.works_under = obj.get_emp_id()
                            emp = obj
                            flag = 1
                            self.agreed_wage = obj.get_wage_offered()
                            self.agreed_leisure = obj.get_leisure()
            if flag == 1:
                emp.acquire_worker(self.unique_id, self.revenue_potential, self.wage_preferred)
                self.unemployed_duration = 0
                self.more_tolerances =4

    def decrease_reservation_wage_leisure(self, choice):
        self.update_unemployed_time()
        if self.unemployed_duration >= 24 and choice == 11:
            self.improve_skill()
            self.unemployed_duration = self.unemployed_duration - 12

        if self.beauty == 1:
            return

        if self.type == 1:
            if self.reduce_wage:
                x = self.wage_preferred - 0.1 * self.wage_preferred
                if x >= self.wage_preferred_threshold:
                    self.wage_preferred = x
                else:
                    self.flip_reduction()
            else:
                x = self.leisure_preferred - 0.1 * self.leisure_preferred
                if x >= self.leisure_preferred_threshold:
                    self.leisure_preferred = x
        else:
            if not self.reduce_wage:
                x = self.leisure_preferred - 0.1 * self.leisure_preferred
                if x >= self.leisure_preferred_threshold:
                    self.leisure_preferred = x
                else:
                    self.flip_reduction()
            else:
                x = self.wage_preferred - 0.1 * self.wage_preferred
                if x >= self.wage_preferred_threshold:
                    self.wage_preferred = x

    def update_unemployed_time(self):
        self.unemployed_duration = self.unemployed_duration + 6

    def update_quadrants(self):
        self.operating_quadrant = 0
        if self.wage_preferred >= 50 and self.leisure_preferred >= 50:
            self.operating_quadrant = 1
        elif self.wage_preferred < 50 and self.leisure_preferred >= 50:
            self.operating_quadrant = 2
        elif self.wage_preferred >= 50 and self.leisure_preferred < 50:
            self.operating_quadrant = 4
        else:
            self.operating_quadrant = 3

    def improve_skill(self):
        x = self.skill + self.skill * 0.1
        if x <= 1:
            self.skill = x

    def flip_reduction(self):
        if self.reduce_wage:
            self.reduce_wage = False
        else:
            self.reduce_wage = True
