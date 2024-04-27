from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import json

getcontext().prec = 30
class Scenarios:
    def __init__(self, N=1000):
        self.num_scenarios = N
        self.avatar_features = 23
        self.SF_threshold = 20
        self.SA_threshold = 0.5
        self.evi_features = 16
        self.ev_choice = 4
        self.SE_threshold = 0.5

    def factorial(self, start, end):
        if start == end:
            return end
        return start * self.factorial(start - 1, end)

    def combination(self, m, n):
        return self.factorial(m, m - n + 1) / self.factorial(n, 1)

    def check(self, N=None):
        if N:
            self.num_scenarios = N
        # probability of 2 similar Avatar features
        p_SAF = self.SF_threshold / 100

        # probability of similar 2 Avatars
        num_SAF = int(self.avatar_features * self.SA_threshold)

        p_SA = 1 - Decimal(1-Decimal(p_SAF)**num_SAF)**int(self.combination(self.avatar_features, num_SAF))
        # p_SA = self.combination(self.avatar_features, num_SAF) * p_SAF ** num_SAF

        # probability of 2 similar environments
        p_SEF = self.ev_choice **(-2)
        num_SEF = int(self.evi_features * self.SE_threshold)
        p_SE = 1 - Decimal(1 - Decimal(p_SEF)**num_SEF)** int(self.combination(self.evi_features, num_SEF))
        # p_SE = self.combination(self.evi_features, num_SEF) * p_SEF**num_SEF

        # probability of 2 similar scenarios
        p_SS = p_SE * p_SA
        print(f"similar Avatar prob = {p_SA}")
        print(f"similar Enviro prob = {p_SE}")
        print(f"similar Scenar prob = {p_SS}")
        result = 1 - Decimal(1 - p_SS)**int(self.combination(self.num_scenarios, 2))
        print(f"Probability of 2 similar scenarios among {S1.num_scenarios} is ", result)
        return result


if __name__ == '__main__':
    S1 = Scenarios()
    X = range(500,1500,10)
    Y = []
    for x in X:
        Y.append(S1.check(x))
    plt.plot(X,Y)
    plt.show()

    # v = Decimal(0.000001)
    # print(v)
    # print(v**10)