from utils import *
import pickle

def exponential_decay(dict_,penality):

    max_len = 1

    for k in dict_:

        dict_[k] *= (1-penality)

        if len(k) > max_len:

            max_len = len(k)

    return dict_, max_len


def drop_from_count(dict_, list_):

    del_items = [item for item in dict_ if dict_[item] < 0.5]

    for item in del_items:

        del dict_[item]

        if len(item) == 1:

            list_.remove(item[0])

    return dict_, list_


def stream(BASKETS,decay = 0.03):

    count = 1

    frequent_items = {} # initialize emtpy dictionary for frequent items

    singletons = []  # initialize list of singletons

    for basket in BASKETS:

        #print("BASKET",basket)

        frequent_items,max_length = exponential_decay(frequent_items,decay)  # moltiply all frequent items by (1-c) and taking
                                                                             # the lenght of the biggest itemset

        #print("MAX LEN",max_length)

        frequent_items, singletons = drop_from_count(frequent_items,singletons) # remov itemset that drop under score 0.5
                                                                                # from the dictionary and also from the list
                                                                                # of singletons

        filtered_basket = filter_baskets(basket,singletons)  # filter the basket from singletons not present in the list of
                                                             # singletons
        #print("FILTERED BASKET",filtered_basket)

        all_combinations = possible_combinations(filtered_basket,max_length) # all possible combination from 1 to the lenght of
                                                                             # the biggest itemset
        #print("ALL COMBINATIONS",all_combinations)
        for combination in all_combinations:

            #print("COMBINATION",combination)

            len_comb = len(combination)

            if len_comb > 1:

                subsets = possible_combinations(combination,len_comb-2) # calculating all subsets of a specific combiantion
                #print("SUBSETS",subsets)
                #print("**")

                if all(x in frequent_items for x in subsets):  # if all the subsets are frequent

                    frequent_items = check_if_is_in_dict_and_count(combination,frequent_items) # add the combination to frequent items

        for singletone in basket:

            singletons.append(singletone)

            frequent_items  = check_if_is_in_dict_and_count((singletone,),frequent_items)

        singletons = list(set(singletons))  # remove duplicates from singletons list

        count += 1

        if count % 10000 == 0:

            print(f"There are {len(singletons)} singletons")
            print(f"There are {len(frequent_items)} itemset in the frequent items dictionary")
            print(f"The lenght of the biggest itemset is {max_length}")
            print(f"Basket processed {count}")

            print("_----_"*10)

        #print("SINGLETONS",singletons)
        #print("FREQUENT ITEMS",frequent_items)
        #print("___________-")

    pickle.dump(frequent_items, open(r"results\stream_dacay.p", "wb"))





