from utils import *
from load_function import load_data_pcy
from apriori import n_th_iteration
import pickle

def second_iteration_pcy(BASKETS,list_of_candidates_dict,bitmap,treshold,stats,verbose):

    t0 = start_time()

    C2 = {}

    for basket in BASKETS:

        filtered_baskets = filter_baskets(basket,list(list_of_candidates_dict[0].keys()))

        combinations = combinations_k_elements(filtered_baskets,2)

        for combination in combinations:

            control = hash(combination)

            if bitmap[control] == 1:

                C2 = check_if_is_in_dict_and_count(combination, C2)


    C2_before_size = get_size_in_MB(C2)

    len_before_C2 = len(C2)

    C2 = filter_infrequent_items(C2,treshold)

    len_after_C2 = len(C2)

    second_pass_time = time_needed(t0)

    list_of_candidates_dict.append(C2)

    stats["time"]["2nd_pass"] = second_pass_time

    stats["sizes"]["C2"] = C2_before_size

    stats["len"]["C2"] = {"before":len_before_C2,"after":len_after_C2}

    if verbose == True:

        print("The second pass took {} minutes".format(second_pass_time))
        print("The size of the candidate for the third pass before filtering infrequent items is {} MB".format(C2_before_size))
        print("C2 contains {} elements, before dropping the infrequent ones".format(len_before_C2))
        print("C2 contains {} elements, after dropping the infrequent ones".format(len_after_C2))
        print("_--_" * 10)

    return list_of_candidates_dict, stats


def pcy(textfile, support, verbose= True):

    t0 = start_time()

    BASKETS, items_dict, list_of_candidates_dict, bitmap, stats, threshold = load_data_pcy(textfile, support=support, verbose=verbose)

    k = 2

    next_pass = False

    if len(list_of_candidates_dict[-1]) != 0:

        next_pass = True

    while next_pass:

        if k == 2:

            list_of_candidates_dict, stats = second_iteration_pcy(BASKETS,list_of_candidates_dict,bitmap,threshold,stats,verbose)

            k += 1

            if len(list_of_candidates_dict[-1]) == 0:

                next_pass = False

        else:

            list_of_candidates_dict, n_th_iterations_time, new_candidate_dict_nth_iteration_size = n_th_iteration(BASKETS, list_of_candidates_dict, threshold, k,stats, verbose=True)

            k += 1

            if len(list_of_candidates_dict[-1]) == 0:

                next_pass = False

    pcy_time = time_needed(t0)

    if verbose == True:

        print("Run PCY alogrithm took {}".format(pcy_time))

    pickle.dump(list_of_candidates_dict, open(r"results\frequent_itemset_pcy.p", "wb"))
    pickle.dump(stats, open(r"results\stat_pcy.p", "wb"))

    return list_of_candidates_dict, stats
