#Initialize cache and requests lists
cache=[]
requests=[]


#FIFO function
def fifo():
    for i in requests:                          #Iterate over items in requests list
        if i in cache:                          #If the number in request list in cache, its a hit
            print("hit")                        

        elif i not in cache:                    #If element in request list is not in cache, its a miss
            print("miss")

            if len (cache)<8:                   #If the length of cache is less than 8 (max limit), the item is appended to cache
                cache.append(i)

            elif len(cache)>=8:                 #If length of cache is over max limit, cache at index [0] is deleted
                del cache[0]                    #and the item in request list is appended to cache
                cache.append(i)

               

    print(cache)
    cache.clear()
    requests.clear()

   
#LFU function
def lfu():

    req_dict={}                                 #Declare empty requests dictionary

    for i in requests:                          #Iterate over the items in request list

        if i in cache:                          #if the items in request list is in cache, its a hit
            print("hit")

        else:
            print('miss')                       #if not, its a miss.

            if len(cache) > 7:                 #Check if length of cache is greater than 7 (maxmimum is 8)

                cache_dict = {}

                cache_dict = {key:value for key,value in req_dict.items() if key in cache}

                minocc = min(cache_dict.values())

                cache_dict = [key for key in cache_dict if cache_dict[key] == minocc]

                cache.remove(min(cache_dict))

            cache.append(i)

        if i in req_dict:

            req_dict[i]+=1

        else:

            req_dict[i]=1

    print(cache)

    cache.clear()

    requests.clear()

 

   
#User input code block
while True:
    
    try:
        user_inp = int(input()) #User input

        if user_inp != 0:                       #if user enters value other than zero, append input to requests list.

            requests.append(user_inp)

   

        elif user_inp == 0:                     #0 signifies end of user input, user is asked to choose eviction algo.

            algo = input() #Evicition algo

            if algo == '1':                     #1 for FIFO

                fifo()

            elif algo == '2':                   #2 for LFU

                lfu()

            elif algo == "Q":                   #Q to quit the program

                exit()

    except ValueError:
        exit()