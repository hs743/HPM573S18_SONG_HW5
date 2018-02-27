import numpy as np
from enum import Enum
import scr.SamplePathClass as Pathcl
import scr.StatisticalClasses as Stat




class coinstate(Enum):

    """State of coin"""

    HEAD = 1

    TAIL = 0





class Game:

    def __init__(self, id, head_prob):

        self._id = id

        self._headProb = head_prob

        self._rnd = np.random

        self._rnd.seed(self._id)

        self._flipResult = coinstate.HEAD

        self._trails = []

        self._reward = -250



    def simulate(self, n_time_steps):



        t = 0  # simulation time



        while t < n_time_steps:

            if self._rnd.sample() < self._headProb:

                self._flipResult = coinstate.HEAD

                self._trails.append(self._flipResult)



            else:

                self._flipResult = coinstate.TAIL

                self._trails.append(self._flipResult)



            t += 1



    def get_exp_value(self, n_time_steps):

        i = 2



        while i < n_time_steps:

            if self._trails[i] == coinstate.HEAD and self._trails[i-1] == coinstate.TAIL and self._trails[i-2] == coinstate.TAIL:

                self._reward += 100

            i += 1



        return self._reward





class Cohort:

    def __init__(self, id, cohort_number, head_prob):

        self._cohorts = []
        self._expValue = []
        self._cohortNumber = cohort_number

        n = 1

        while n <= cohort_number:

            game = Game(id * cohort_number + n, head_prob)

            self._cohorts.append(game)

            n += 1



    def simulate(self, n_time_steps):

        for game in self._cohorts:

            game.simulate(n_time_steps)

            value = game.get_exp_value(n_time_steps)

            if not (value is None):

                self._expValue.append(value)



        return self._expValue



    def get_loss_number(self):
        loss = 0
        for i in self._expValue:
            if i < 0:
                loss += 1
        return loss/len(self._expValue)

    def get_exp_value(self):
        return self._expValue

    def get_ave_value(self):
        return sum(self._expValue)/len(self._expValue)

    def get_cohort_number(self):
        return self._cohortNumber

