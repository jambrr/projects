# -*- coding: utf-8 -*-
# Revised version 23/09/2021

import numpy as np 
import time
import random
import matplotlib.pyplot as plt

MAX_WIN = 10

# compute a reward based on a probability
def get_reward( prob, n = MAX_WIN ):
    reward = 0
    for i in range( n ):
        if random.random() < prob: # random() returns a float < 1.0
            reward += 1
    return reward

# find the best machine based on past rewards
def get_best_arm( pastRewards, actions ):
    bestArm = 0 # just default to arm #0 at the beginning
    bestAvg = 0
    avg = 0

    for action in actions:
    
        #TODO:
        #step1: find in the history the index of all experiments where "action" was performed
        #for rewards in pastRewards[action]:
        #slice the 2 dimensional array
        a = np.where(pastRewards[:,0] == action)
        avg = np.mean(pastRewards[a])
        print(str(action)+" "+str(avg))
        # tmp = ...
        #step2: compute the mean reward over these experiments
        # avg = ...
        if avg > bestAvg:
            bestAvg = avg
            bestArm = action
    #print("bestArm:", bestArm,  " avg:", bestAvg )
    return bestArm


nb_machines = 10
# set fixed seed as machines' probabilities do not change over experiments
np.random.seed(0)
# chance to win for each machine
#   DO NOT access this information to improve your strategy, that would be considered cheating
#   you can use the information to verify whether your algorithm learned the right choice or not though
arms = np.random.rand( nb_machines ) # create a collection of 10 random float between 0 and 1
print( arms )

# reset to the seed to have actual randomness for each pull of an arm
np.random.seed()

# Number of trials in a single experiment
nb_trials = 1000

starting_time=time.time()

# Numpy-Array of 2-dimensional vectors, initialized with zeros
# first dimension: action taken, second dimension: reward
# both dimensions contain integer values
pastRewards = np.zeros( ( nb_trials, 2 ) ) 

plt.xlabel( "Trials" )
plt.ylabel( "Avg Reward" )

best_arm=0

def run_experiment():
    cumulated = 0

    for i in range( nb_trials ):
       # TODO: use the "random.random()" and "get_best_arm(...)" methods to implement the epsilon-greedy strategy
       #best_arm = get_best_arm(...)  # Hint: use portion of pastRewards that has been set already     
       choice = np.random.choice( nb_machines )
       
       
       # pull the arm of machine with id [choice] and collect the wins
       reward = get_reward( arms[ choice ] )
       # print("choice:", choice, "reward:", reward) # for debugging
       # remember what action was taken and the corresponding win
       pastRewards[ i ] = ( choice, reward )
       
       # used simply to monitor the run
       runningMean = np.mean( pastRewards[ :i+1, 1 ] ) # i+1 because the upper limit is not included
       plt.scatter( i, runningMean )
       cumulated += reward

    best_arm = get_best_arm(pastRewards, list(range(nb_machines)))
    print("total reward "+str(cumulated))
    
    plt.axhline( y = np.max( arms ) * MAX_WIN, color="blue" )
    plt.axhline( y = np.average( arms ) * MAX_WIN, color="orange" )
    plt.ylim(ymin=0, ymax=MAX_WIN)
    print("best arm: ", best_arm, "(should:", np.argmax ( arms ),"p_win:", np.max ( arms ) ,"),  Avg winning:", runningMean)
    #plt.show()
    
    elapsed_time = time.time() - starting_time
    print("Experiment took {} seconds".format(elapsed_time))
    return runningMean

mean = []
for i in range(3):
    mean.append(run_experiment()/MAX_WIN)

print(mean)
