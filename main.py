from bandit.thompson import ThompsonBandit

NUM_ITER = 99999
prob_array = [0.1, 0.2, 0.3, 0.5]

def ThompsonSim(p_arr):
    
    bandits = [ThompsonBandit(p) for p in p_arr]

    # play each arm
    
    for i in range(NUM_ITER):
        best_bandit = bandits[0]
        best_reward = -1
        reward = -1
        # Compute the best bandit
        for bandit in bandits:
            reward = bandit.sample()
            if reward > best_reward:
                best_bandit = bandit
                best_reward = reward     

        best_bandit = best_bandit.play_update()      

    return bandits

if __name__ == "__main__":
    bandits = ThompsonSim(prob_array)

    for b in bandits:
        print(float( b.a) / float(b.a + b.b) )
    
    for b in bandits:
        print(str(b.num_plays) + " / " + str(b.a) + " / "+ str(b.b))






