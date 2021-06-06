import numpy as np
import matplotlib as plt
plotting = []
plt.rcParams['figure.figsize'] = (10, 10)
N = 10
M = 5000
iterations = 1
half_years = 6
unemployment_rate: int = 0
unemployment_rates = list()
iteration = list()
employed_count = 0

off_to_on = list()
on_to_off = list()
off_to_on_count = 0
to_be_modified = list()
already_employed = list()
on_to_off_count = 0
it_count = 0
average_leisure = list()
average_wages = list()
employer = list()
offline_wc = list()
online_wc = list()
u_rates = list()
u_rates_l = list()
u_rates_w = list()
u_rate = 0
min_wages = list()
min_leisure = list()
mu, sigma = 0, 20  # mean and standard deviation for extracting the duration of unemployed
online_worker = 0
offline_worker = 0
average_unemployment_duration = list()

# new incorporation
regulatory_threshold_wage = 0
regulatory_threshold_leisure = 0
discounting_rate_wage = 0.1
discounting_rate_leisure = 0.1