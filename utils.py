import time
import sys
from random import shuffle

def start_time():
    return time.time()

def time_needed(t0):
    return round((time.time()-t0)/60,2)

def get_size_in_MB(var):
    return round(sys.getsizeof(var)/1000000,2)

def encode_products(line, item_dict,item_id,C1):

    basket = set()

    for el in line.split("__")[2:]:

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


def order_dict(dict_):

    return dict(sorted(dict_.items(), key=lambda item: item[1],reverse=True))

def decode_dict(dict_,dict_item):

    new_dict = {}

    for key in dict_:

        list_ = []

        if isinstance(key, int):

            new_dict[(dict_item[key],)] = dict_[key]

        else:

            for el in key:

                list_.append(dict_item[el])

        new_dict[tuple(list_)] = dict_[key]

    return  new_dict

def unify_list_of_dict(list_of_dict):

    new_dict = {}

    for dict_ in list_of_dict:

        for key in dict_:

            new_dict[key] = dict_[key]

    return new_dict

def pipeline_dict(list_of_dict,item_dict):

    return order_dict(decode_dict(unify_list_of_dict(list_of_dict),item_dict))


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


def hash(list_):

    return ((list_[0]*list_[1])+list_[0]) % 100000


def hash_basket(list_,dict_):

    pairs = combinations_k_elements(list_, 2)

    for pair in pairs:

        index = hash(pair)

        dict_ = check_if_is_in_dict_and_count(index, dict_)

    return dict_


def create_bitmap(hash_table, threshold):

    bit_map = [0 for x in range(100000)]

    for key, value in hash_table.items():

        if value < threshold:

            bit_map[key] = 0

        else:

            bit_map[key] = 1

    return bit_map



def shuffle_list_of_list(list_):

    ind = [x for x in range(len(list_))]

    shuffle(ind)

    suffled_basket = []

    for index in ind:
        suffled_basket.append(list_[index])

    return suffled_basket


def batch(iterable, n=1):

    l = len(iterable)

    for ndx in range(0, l, n):

        yield iterable[ndx:min(ndx + n, l)]


def precision(true_dict,stream_dict):

    count = 0

    for key in stream_dict:

        if key in true_dict:

            count += 1

    return round(count/len(true_dict),1)*100


def false_positive(true_dict,stream_dict):

    count = 0

    for key in stream_dict:

        if key not in true_dict:

            count += 1

    return round(count/len(stream_dict),1)*100