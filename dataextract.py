        self.employer_flex = 0.5 + 0.12 * np.random.randn(1, 100)
        self.employer_flex = self.employer_flex.tolist()
        self.employer_flex = 10 * self.employer_flex[0]
        self.employer_flex = modify_random_values(self.employer_flex)