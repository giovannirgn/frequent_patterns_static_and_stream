import time
import sys

def start_time():
    return time.time()

def time_needed(t0):
    return round((time.time()-t0)/60,2)

def get_size_in_MB(var):
    return round(sys.getsizeof(var)/1000000,2)

def encode_products(line, item_dict,item_id,C1):

    # encode_products function will get a line from the input file, the item dict, the item id and the dictonary of candidate
    # at a given point and return the updated version of the item_dict, the updadet vesìrsion of the candidate and the
    # encoded basket that wil be stored in the list

    basket = set()  # initialize the basket

    for el in line.split("__")[2:]:  # for each element splitted by  two underscores (excluding the first two that
                                     # are the customer_id and the oreder_id

        if el in item_dict:

            basket.add(item_dict[el])
            C1[item_dict[el]] += 1

        else:

            item_dict[el] = item_id
            C1[item_id] = 1
            basket.add(item_dict[el])
            item_id += 1

    return sorted(list(basket)), item_dict, item_id, C1


def reverse_dict(item_dict):

    list_of_keys = [key for key in item_dict]

    for key in list_of_keys:

        value  = item_dict[key]

        del item_dict[key]

        item_dict[value] = key

    return item_dict


def filter_infrequent_items(dict_,threshold):

    # deltete itmes from candidate dict if the count is less than the support

    del_items = [item for item in dict_ if dict_[item] < threshold]

    for item in del_items:

        del dict_[item]

    return dict_


def filter_baskets(basket,list_):

    filtered_basket = []

    for item in basket:

        if item in list_:

            filtered_basket.append(item)

    sorted(filtered_basket)

    return filtered_basket


def combinations_k_elements(list_,k):

    list_of_combinations = []

    def backtrack(start,comb):

        if len(comb) == k:

            list_of_combinations.append(tuple(sorted(comb.copy())))

            return

        for i in range(start,len(list_)):

            comb.append(list_[i])

            backtrack(i+1,comb)

            comb.pop()

    backtrack(0,[])

    return list_of_combinations



def check_if_is_in_dict_and_count(item,dict_):

    if item in dict_:

        dict_[item] += 1

    else:

        dict_[item] = 1

    return dict_

def frequent_item_lists(dict_):

    items_list  = []

    for key in dict_:

        if isinstance(key,int):

            items_list.append(key)

        else:

            for i in key:

                items_list.append(i)

    return list(set(items_list))