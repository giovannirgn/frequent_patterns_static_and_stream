from utils import *
import pickle

def decaying_window(dict_,penality):

    for k in dict_:

        dict_[k] *= (1-penality)

    return dict_


def drop_from_count(dict_,drop_threshold):

    del_items = [item for item in dict_ if dict_[item] < drop_threshold]

    for item in del_items:

        del dict_[item]

    return dict_

def combinations_with_conditions(goodsubset, remainingels, condition):

    answers = []

    for j in range(len(remainingels)):

        nextsubset = goodsubset + remainingels[j:j + 1]

        if condition(nextsubset):

            answers.append(tuple(nextsubset))

            answers += combinations_with_conditions(nextsubset, remainingels[j + 1:], condition)

    return answers


def stream_decaying_window(BASKET,decay = 0.005,drop_threshold = 0.5,verbose = True):

    freq_items = {}

    t0 = start_time()

    count = 0

    for basket in BASKET:

        freq_items = decaying_window(freq_items,decay)

        freq_items = drop_from_count(freq_items,drop_threshold)

        to_add = combinations_with_conditions([], basket,
            lambda l: all(x in freq_items for x in combinations_k_elements(list(l), len(l) - 1)) or (len(l) == 1))

        for item in to_add:

            freq_items = check_if_is_in_dict_and_count(item,freq_items)

        if verbose == True:

            if count % 10000 == 0:

                print(f"{count} basket processed")

        count += 1

    print("Run edecaying window on the stream took {}".format(time_needed(t0)))

    pickle.dump(freq_items, open(r"results\stream_exponential_decay_apriori.p", "wb"))





