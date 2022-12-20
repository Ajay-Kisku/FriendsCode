array = [1,8,9,20]

array = sorted(list(set(array) - {1,0}))  #exclude 0, 1

maxArray = max(array)
goUpTo = 0 # iterate other elements upto this only
lenArray = len(array) #max count to get answer else there is no answer
notDivisibleBy = []

# i will be greatest number by which smallest array element could not be divided
for i in range(2, maxArray):
    if maxArray % i != 0 : goUpTo = i

#for storing the elements that cannot divide the array elements
for i in array:
    for j in range(2, goUpTo+1): # remove the iteration of 1
        if i % j != 0:
            notDivisibleBy.append(j)

#removing the duplicate elements
distinctNotDivisibleBy = list(set(notDivisibleBy) - set(array))

answer = 0

for j in range(len(distinctNotDivisibleBy)):
    if(notDivisibleBy.count(distinctNotDivisibleBy[j]) == lenArray):
        answer = distinctNotDivisibleBy[j]
        break
    else:
        pass
        # break

if(answer != 0 ): print("Answer :", answer)

#for storing the elements that cannot divide the array elements
for i in array:
    print(str(i).ljust(3), end=" : ")
    for j in range(2, goUpTo+1): # remove the iteration of 1
        if(j == answer):
            print(("\033[4;31m "+str(j)+" \033[0m").rjust(3), end=", ")
        elif (i % j != 0 ):
            print(str(j).rjust(3), end=", ")
    print("")
