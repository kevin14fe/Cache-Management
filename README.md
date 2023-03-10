# Cache-Management
Cache Management

Background:

 In computers, memory is located in different parts of the computer; memory on disk is far away from the CPU and takes a long time to access, but offers a large amount of storage; cache memory is close to the CPU so it is faster to access, but does not offer a lot of storage space.

 It is therefore wise to use the cache memory in a smart way, so that pages of memory that are more likely to be accessed are already in the cache. This means that there are fewer accesses to disk memory, and the memory transaction is ultimately quicker.

 This code is used to simulate a cache with two management techniques, which are explained below. 

Working:

 The cache memory operates in the following manner:

 Pages from memory are requested. When a page from memory is requested, the cache memory is searched for that page. 

 If the page is found in the cache memory, then this is called a "hit".

 If the page is not found in the cache memory, then this is called a "miss".  When a miss happens, the page must be retrieved from the main memory (the disk memory) and must be placed in the cache memory. If the cache memory is not full, then the page is simply added to the cache memory. If the cache memory is full, then one of the pages that is in the cache memory will have to be replaced. In this case, we say that a new page is added to the cache memory, and the old page is evicted. 

 There are multiple ways in which we can choose which page to evict. Two of those are presented below, the "First in First Out (FIFO)" algorithm, and the "Least Frequently Used (LFU)" algorithm.


First in First Out (FIFO)

 In a First in First Out (FIFO) cache memory, the page that is evicted is the one that has the longest time since it was added.


Least Frequently Used (LFU)

 In a Least Frequently Used (LFU) cache memory, the page that is evicted is the page that has had the fewest requests so far. In case of two pages having the same    amount of requests, the lowest numbered page should be evicted. The number of requests that a page has had is maintained throughout the parsing of the whole set of  requests, and it is not "forgotten" once a page has been removed from the cache memory.

 

Specifics:

 In this code, we will assume that every page is represented by a positive integer and the capacity of the cache memory is 8 pages. 

 In particular, a request for a page will be indicated by a number, e.g., the number 3 means that we request page 3. If the requested page is in the cache memory, then this will be a hit. If the requested page is not in the cache memory, then this will be a miss. In this latter case, the page has to be retrieved from the main memory and placed into the cache memory. If the cache memory is not full (i.e., it has fewer than 8 pages already in it), then we can simply add the requested page to the cache memory. If the cache memory is full (meaning that it has exactly 8 pages in in), then we have to evict one page already in the cache memory, in order to bring the newly requested page in. Which page to evict is decided based on one of the two algorithms above, FIFO or LFU.

 
Program Structure

 The program has the following functions and variables:

    A global scope list called ???cache???

    A global scope list called ???requests???

    A function fifo() which will run the FIFO cache memory algorithm on cache and requests

    A function lfu() which will run the LFU cache memory algorithm on cache and requests


 Clarification: After each method has been used for the given requests, the cache is cleared, meaning that the list ???cache??? does not contain any elements.

Constructing the list of requests: The program asks the user for an integer repeatedly until 0 is entered. As mentioned above, these integers represent requested pages, and 0 signifies the end of the request input. The inputted integers are placed into the list requests.

Choosing the eviction algorithm: The user is then be presented with the following options: press 1 for fifo, or press 2 for lfu, or press Q to quit the program.

    If the user chooses 1, then the function fifo() is called.
    If the user chooses 2, then the function lfu()) is called.
    If the user chooses Q, the program should terminate.

 Whichever of the two functions is chosen, it iterates over the requests in the list requests, and ???request??? each ???page??? (represented simply as an integer) from the cache memory.

    If the ???page??? is already in the cache memory cache, then this is a hit and the word ???hit??? is printed to the screen.
    If the ???page??? is not in the cache memory cache, then this is a miss and the word ???miss??? is printed to screen.

 In the event of a miss, the correct ???page??? is evicted from the cache memory and the newly requested ???page??? is correctly inserted into cache memory, according to the eviction algorithm that has been selected by the user earlier. In reality, this means that the program will remove an integer from cache and insert a new integer into cache.

 At the end of processing all requests, the final state of cache (i.e., the contents of the list cache) is printed and exits back to the main menu, where the user is prompted to enter the requests.
