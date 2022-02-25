# Inputing the parameters returns the smallest group size needed for the selected probability, where every following subgroup will also have a probability bigger
# than the wanted probability.

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypergeom.html

from math import floor
from scipy import stats
from scipy.stats import hypergeom

# a test function to see if the hypergeometric function is returning the correct values
def test():
    print(1-stats.hypergeom.cdf(1,21,14,2,loc=0))
    
    


# our hypergeo is P(k,M,n,N). Our k is our saple_s, M is number_pop, n is populations-s, and N is number_sample




def main():

    #Number_pop: is the population size.
    number_population = int(input("Choose the population size:"))

    #Population_s: is the number of successes in the population.
    population_s = int(input("Choose the number of successes in the population:"))

    # input smallest probability wanted
    wantedProb = float(input("Chosse the minumum probability wanted"))
    print("smallest",findSmallest_1(number_population,population_s,wantedProb))
    print("smallest:",findSmallest_2(number_population,population_s,wantedProb))
    print("smallest:",binary_search(number_population,population_s,wantedProb))
     
    print("smallest:",binary_search_updated(number_population,population_s,wantedProb))
    #printProbability(number_population,population_s)


            

  

# This method finds the first subgroup where the probability is bigger than the wanted probability
# After that it tests if for any of the following terms there is a probability smaller than the desired and if not returns the smallest sub group.
# Notice we can only lookmt the odd subgroups, since we have already prove that every odd probability 2k-1 is bigger than the following subgroup 2k


def findSmallest_1(M,n,w):
    smallestNum = M
    maxProb = 0
    for N in range (M):
        if N%2==1:

            k = floor(N/2)
            #print("For N",N,"Prob is:",(1-stats.hypergeom.cdf(k,M,n,N,loc=0)))
            # check if the probability of a subgroup of size N is bigger than the wanted probability
            if ((1-stats.hypergeom.cdf(k,M,n,N,loc=0)))> w:
                maxProb = (1-stats.hypergeom.cdf(k,M,n,N,loc=0))
                smallestNum = N
                #print("For N",N,"Prob is:",(1-stats.hypergeom.cdf(k,M,n,N,loc=0)))
                #print(smallestNum)
                #test if all the following subgroups also have a probability bigger than 95% 
                bigger = True
                i=0
                while i in range (N,M) and bigger==True:
                    if ((1-stats.hypergeom.cdf(k,M,n,i,loc=0)<maxProb)):
                        bigger = False
                if bigger==True:
                    return smallestNum

# This method finds the first subgroup where the probability is bigger than the wanted probability

def findSmallest_2(M,n,w):
    smallestNum = M
    for N in range (M):
        if N%2==1:

            k = floor(N/2)
            #print("For N",N,"Prob is:",(1-stats.hypergeom.cdf(k,M,n,N,loc=0)))
        # check if the probability of a subgroup of size N is bigger than the wanted probability
            if ((1-stats.hypergeom.cdf(k,M,n,N,loc=0)))> w:
                smallestNum = N
                #print("For N",N,"Prob is:",(1-stats.hypergeom.cdf(k,M,n,N,loc=0)))
                #print(smallestNum)
                return smallestNum


# This method will perform an adapded version of a binary search to the data
def binary_search(M,n,w):
    search_list= []
    num_list = []
    # Append to our search list all the probabilities under 100%
    # create an empty list with floor(M/2))+1/2 +1 lenght 1,3,5,7
    for N in range((floor(M/2))+1):
        if N%2==1:
            k = floor(N/2)
            search_list.append((1-stats.hypergeom.cdf(k,M,n,N,loc=0)))
            num_list.append(N)
    iterations = 1
    left = 0 # starting index
    right = len(search_list)-1 # Last index
    mid = (right + left)//2 # In Python, // means floored division, 
    done = False
    while not done:
        if (search_list[mid]<w):
            left = mid
        else:
            right = mid+1
        mid = (right+left)//2
        iterations +=1
        if (search_list[mid]>w and search_list[mid-1]<w):
            done=True

    return num_list[mid]

    # This method will perform an adapded version of a binary search to the data
def binary_search_updated(M,n,w):
    num_list = []
    k_list= []

    # Append to our search list all the probabilities under 100%
    # create an empty list with floor(M/2))+1/2 +1 lenght 1,3,5,7
    #for N in range((((floor(M/2))+1)//2)+1):
        #num_list.append(2*N+1)
        #k_list.append(floor((2*N+1)/2))

    for N in range((floor(M/2))+1):
        if N%2==1:
            k_list.append(floor(N/2))
            num_list.append(N)
    
    iterations = 1
    left = 0 # starting index
    right = len(num_list)-1 # Last index
    mid = (right+left)//2
    prob = (1-stats.hypergeom.cdf(k_list[mid],M,n,num_list[mid],loc=0))
    previous_prob = (1-stats.hypergeom.cdf(k_list[mid-1],M,n,num_list[mid-1],loc=0))
    done = False
    while not done:
        
        if (prob<w):
            left = mid
        else:
            right = mid+1

        mid = (right+left)//2
        iterations +=1

        prob = (1-stats.hypergeom.cdf(k_list[mid],M,n,num_list[mid],loc=0))
        previous_prob = (1-stats.hypergeom.cdf(k_list[mid-1],M,n,num_list[mid-1],loc=0))

        if (prob>w and previous_prob<w):
            done=True
            
        
    return num_list[mid]
        

    

            





# Our m is number_popilation and our 
def printProbability(M,n):
    done = False
    M_range= int((2*M*(1-(n/100)))+1)
    while (not done):
        mode = input(" Please choose the subgroups you want to look at (1-All , 2-ODDS, 3-EVENS, 4-NONE) and press enter: ")
        if mode =="4":
            return
        elif mode == "1":
            # We can
            for N in range (M_range):
                k = floor(N/2)
                print("For N",N,"Prob is:",(1-stats.hypergeom.cdf(k,M,n,N,loc=0)))
                #print("For N",N,"Prob binom is:",(stats.binom.cdf(k,n,.7,)))
    
        elif (mode=="2"):
            for N in range (M_range):
                k = floor(N/2)
                if (N%2!=0):
                    print("For N",N,"Prob is:",(1-stats.hypergeom.cdf(k,M,n,N,loc=0)))
        if (mode=="3"):
            for N in range (M_range):
                k = floor(N/2)
                if (N%2==0):
                    print("For N",N,"Prob is:",(1-stats.hypergeom.cdf(k,M,n,N,loc=0)))
        keepgoing = input("Do you want to print anything else? Press y to keep going or any other key to stop")
        if (keepgoing != "y"):
            done = True



     

            

    
main()





