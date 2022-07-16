from utils import *

def second_iteration(BASKETS,list_of_candidates_dict,treshold,verbose):

    t0 = start_time()

    C2 = {}

    for basket in BASKETS:

        filtered_baskets = filter_baskets(basket,list(list_of_candidates_dict[0].keys()))

        combinations = combinations_k_elements(filtered_baskets,2)

        for comb in combinations:

            C2 = check_if_is_in_dict_and_count(comb,C2)

    C2 = filter_infrequent_items(C2,treshold)

    second_pass_time = time_needed(t0)

    C2_size = get_size_in_MB(C2)

    list_of_candidates_dict.append(C2)

    if verbose == True:

        print("The second pass took {} minutes".format(second_pass_time))
        print("The size of the candidate for the third pass is {} MB".format(C2_size))

    return list_of_candidates_dict, second_pass_time,C2_size


def n_th_iteration(BASKET,list_of_candidate_dict,threshold,k,verbose):

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

    new_candidate_dict = filter_infrequent_items(new_candidate_dict,threshold)

    list_of_candidate_dict.append(new_candidate_dict)

    n_th_iterations_time = time_needed(t0)

    new_candidate_dict_nth_iteration_size = get_size_in_MB(new_candidate_dict)

    if verbose == True:

        print("The {}th pass took {} minutes".format(k,n_th_iterations_time))
        print("The size of the candidate for the third pass is {} MB".format(new_candidate_dict_nth_iteration_size))

    return list_of_candidate_dict, n_th_iterations_time, new_candidate_dict_nth_iteration_size





























