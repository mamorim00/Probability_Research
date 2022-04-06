# Inputing the parameters returns the smallest group size needed for the selected probability, where every following subgroup will also have a probability bigger
# than the wanted probability.

from methods import binary_search,binary_search_updated,findSmallest_1,findSmallest_2,printProbability

# our hypergeo is P(k,M,n,N). Our k is our saple_s, M is number_pop, n is populations-s, and N is number_sample

def main():

    #Number_pop: is the population size.
    number_population = int(input("Choose the population size: "))

    #Population_s: is the number of successes in the population.
    population_s = float(input("Choose the probability of votes for A from 0.5 to 1: "))
    while (population_s<.50 or population_s>1):
        print("Please enter a value between 0.5 and 1")
        population_s = float(input("Choose the probability of votes for A from 0.5 to 1: "))
    population_s= int(population_s*number_population)
    # input smallest probability wanted
    wantedProb = float(input("Chosse the minumum probability wanted from 0.5 to 1: "))
    while (wantedProb<.50 or wantedProb>1):
        print("Please enter a value between 0.5 and 1")
        population_s = float(input("Chosse the minumum probability wanted from 0.5 to 1: "))
    print("smallest",findSmallest_2(number_population,population_s,wantedProb))

    printProbability(number_population,population_s)
  

    
main()






