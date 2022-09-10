from apriori import *
import pickle

def first_pass(batch,treshold):

    C1 = {}

    for basket in batch:

        for item in basket:

            C1 = check_if_is_in_dict_and_count(item,C1)

    C1 = filter_infrequent_items(C1,treshold)

    stats = {}

    stats["time"] = {}

    stats["time"]["load_and_1st_pass"] = 0

    stats["sizes"] = {}

    stats["sizes"]["C1"] = 0

    stats["sizes"]["Bitmap"] = 0

    stats["len"] = {}

    stats["len"]["C1"] = {"before":0,"after":0}

    return [C1], stats


def apriori_stream(batch,threshold):

    list_of_candidates_dict, stats = first_pass(batch, threshold)

    k = 2

    next_pass = False

    if len(list_of_candidates_dict[-1]) != 0:

        next_pass = True

    while next_pass:

        if k == 2:

            list_of_candidates_dict, stats = second_iteration(batch, list_of_candidates_dict, threshold, stats,
                                                              verbose=False)

            k += 1

            if len(list_of_candidates_dict[-1]) == 0:
                next_pass = False

        else:

            list_of_candidates_dict, n_th_iterations_time, new_candidate_dict_nth_iteration_size = n_th_iteration(
                batch, list_of_candidates_dict, threshold, k, stats, verbose=False)

            k += 1

            if len(list_of_candidates_dict[-1]) == 0:
                next_pass = False


    return list_of_candidates_dict


def add_to_frequent_items(frequent_items,frequent_items_batch):


    for candidate in frequent_items_batch[:-1]:

        for item in candidate:

            if item in frequent_items:

                frequent_items[item] = frequent_items[item] + candidate[item]

            else:

                frequent_items[item] = candidate[item]

    return frequent_items




def multiple_apriori(BASKETS,len_batch,support,verbose = True):

    t0 = start_time()

    frequent_items = {}

    threshold = round(len_batch * support,0)

    count = 0

    batches = list(batch(BASKETS,n=len_batch))

    n_batches = len(batches)

    for batch_ in batches:

        frequent_items_batch = apriori_stream(batch_, threshold)

        frequent_items = add_to_frequent_items(frequent_items,frequent_items_batch)

        count += 1

        if verbose == True:

            print(f"{round((count/n_batches),2)*100}% of the batches processed")

    if verbose == True:

        print("Run multiple apriori on the stream took {}".format(time_needed(t0)))


    pickle.dump(frequent_items, open(r"results\stream_multiple_apriori.p", "wb"))








