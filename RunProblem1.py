import problem1 as Model

import scr.SamplePathClass as SamplePathSupport

import scr.FigureSupport as Fig

headProb = 0.5

timeSteps = 20

cohortNumber = 1000







myCohort = Model.Cohort(id = 2, cohort_number = cohortNumber, head_prob = headProb)

myCohort.simulate(timeSteps)


print("The probablity of flipping a head is 0.5, we flip 20 times as one game and we undergo the game 1000 times")
print('Average expected reward (dollors):', myCohort.get_ave_value())

print('The maximum reward is:', max(myCohort.get_exp_value()), "dollars", "and the minimum reward is:", min(myCohort.get_exp_value()), 'dollars.')







# plot the histogram

Fig.graph_histogram(

    observations=myCohort.get_exp_value(),

    title='Histogram of Rewards',

    x_label='Reward',

    y_label='Count')



#estimate the prob of losing money in this game

probLoss = myCohort.get_loss_number()

print('The probability of losing money in this game is:', probLoss)