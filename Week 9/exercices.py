### Problem 1
# def word_lengths(phrase):    
#     words = phrase.split(" ")
#     print(list(map(len,words)))

# word_lengths('How long are the words in this phrase')



### Problem 2
# from functools import reduce

# def digits_to_num(digits): 
#     print(reduce(lambda x,y: str(x)+str(y),digits))
#     print(reduce(lambda x,y: x*10+y,digits))
# digits_to_num([3,4,3,2,1])



### Problem 3
# def filter_words(word_list, letter):
#     return list(filter(lambda x: x[0] == letter, word_list))

# l = ['hello','are','cat','dog','ham','hi','go','to','heart']
# print(filter_words(l,'h'))



### Problem 4
# def concatenate(L1, L2, connector):
    
#     strings = list(zip(L1, connector*len(L1), L2))
#     print(list(map(''.join, strings)))

# concatenate(['A','B'],['a','b'],'-')




### Problem 5
def d_list(L):   
    d = {} 
    for key,value in enumerate(L):
        d[value] = key
    
    print(list(L))
    print(list(enumerate(L)))
    print(list(map(lambda k,v: (v,k), enumerate(L))))


d_list(['a','b','c'])

