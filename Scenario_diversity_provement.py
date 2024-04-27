class Scenarios:
    def __init__(self):
        self.num_scenarios = 1000
        self.avatar_features = 30
        self.SF_threshold = 15
        self.SA_threshold = 0.5
        self.evi_features = 10
        self.ev_choice = 3
        self.SE_threshold = 0.25

    def factorial(self, start, end):
        if start == end:
            return end
        return start * self.factorial(start - 1, end)

    def combination(self, m, n):
        return self.factorial(m, m - n + 1) / self.factorial(n, 1)

    def check(self):
        # probability of 2 similar Avatar features
        p_SAF = self.SF_threshold / 100

        # probability of similar 2 Avatars
        num_SAF = int(self.avatar_features * self.SA_threshold)
        p_SA = self.combination(self.avatar_features, num_SAF) * p_SAF ** num_SAF

        # probability of 2 similar environments
        p_SEF = self.ev_choice **(-2)
        num_SEF = int(self.evi_features * self.SE_threshold)
        p_SE = self.combination(self.evi_features, num_SEF) * p_SEF**num_SEF

        # probability of 2 similar scenarios
        p_SS = p_SE * p_SA
        print(f"similar Avatar prob = {p_SA}")
        print(f"similar Enviro prob = {p_SE}")
        print(f"similar Scenar prob = {p_SS}")
        print(f"Probability of 2 similar scenarios among {S1.num_scenarios} is ", self.combination(self.num_scenarios, 2) * p_SS**2)


if __name__ == '__main__':
    S1 = Scenarios()
    S1.check()



