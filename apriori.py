from utils import *
from load_function import load_data_apriori
import pickle

def second_iteration(BASKETS,list_of_candidates_dict,treshold,stats,verbose):

    t0 = start_time()

    C2 = {}

    for basket in BASKETS:

        filtered_baskets = filter_baskets(basket,list(list_of_candidates_dict[0].keys()))

        combinations = combinations_k_elements(filtered_baskets,2)

        for comb in combinations:

            C2 = check_if_is_in_dict_and_count(comb,C2)

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


def n_th_iteration(BASKET,list_of_candidate_dict,threshold,k,stats,verbose):

    t0 = start_time()

    new_candidate_dict = {}

    list_frequent_items = frequent_item_lists(list_of_candidate_dict[-1])

    for basket in BASKET:

        filtered_basket = filter_baskets(basket,list_frequent_items)

        combinations = combinations_k_elements(filtered_basket,k)

        for comb in combinations:

            comb_subsets = combinations_k_elements(comb,k-1)

            if all(x in list_of_candidate_dict[-1] for x in comb_subsets):

                new_candidate_dict = check_if_is_in_dict_and_count(comb,new_candidate_dict)

    new_candidate_dict_nth_iteration_size = get_size_in_MB(new_candidate_dict)

    len_new_candidate_dict_nth_iteration_before = len(new_candidate_dict)

    new_candidate_dict = filter_infrequent_items(new_candidate_dict,threshold)

    len_new_candidate_dict_nth_iteration_after = len(new_candidate_dict)

    list_of_candidate_dict.append(new_candidate_dict)

    n_th_iterations_time = time_needed(t0)

    stats["time"][f"{k}_pass"] = n_th_iterations_time

    stats["sizes"][f"C{k}".format(k)] = new_candidate_dict_nth_iteration_size

    stats["len"][f"C{k}".format(k)] = {"before":len_new_candidate_dict_nth_iteration_before,"after":len_new_candidate_dict_nth_iteration_after}

    if verbose == True:

        print("The {}th pass took {} minutes".format(k,n_th_iterations_time))
        print("The size of the candidate for the {}th pass before filtering infrequent items is {} MB".format(k+1,new_candidate_dict_nth_iteration_size))
        print("C{} contains {} elements, before dropping the infrequent ones".format(k,len_new_candidate_dict_nth_iteration_before))
        print("C{} contains {} elements, after dropping the infrequent ones".format(k,len_new_candidate_dict_nth_iteration_after))
        print("_--_"*10)

    return list_of_candidate_dict, n_th_iterations_time, new_candidate_dict_nth_iteration_size



def apriori(textfile, support, verbose= True):

    t0 = start_time()

    BASKETS, items_dict, list_of_candidates_dict, stats, threshold = load_data_apriori(textfile, support=support, verbose=verbose)


    k = 2

    next_pass = False

    if len(list_of_candidates_dict[-1]) != 0:

        next_pass = True

    while next_pass:

        if k == 2:

            list_of_candidates_dict, stats = second_iteration(BASKETS,list_of_candidates_dict,threshold,stats,verbose)

            k += 1

            if len(list_of_candidates_dict[-1]) == 0:

                next_pass = False

        else:

            list_of_candidates_dict, n_th_iterations_time, new_candidate_dict_nth_iteration_size = n_th_iteration(BASKETS, list_of_candidates_dict, threshold, k,stats, verbose=True)

            k += 1

            if len(list_of_candidates_dict[-1]) == 0:

                next_pass = False

    apriori_time = time_needed(t0)

    if verbose == True:

        print("Run apriori alogrithm took {}".format(apriori_time))

    pickle.dump(list_of_candidates_dict, open(r"results\frequent_itemset_apriori.p", "wb"))
    pickle.dump(stats, open(r"results\stat_apriori.p", "wb"))

    return list_of_candidates_dict, stats


























