from utils import start_time, time_needed, encode_products, reverse_dict, filter_infrequent_items,get_size_in_MB



def load_data_apriori(txtfile, support,verbose = False):

    # import data stored in a text file
    # the data structure will be a listt of lists ex [[item1,item2,.....],[item1,....],[],...]:
    # the function will return the list of baskets, the item dictionary, the candidate for the second pass of the apriori
    # and the size of the three elements in megabites

    t0 = start_time()

    BASKETS = []

    items_dict = {}

    C1 = {}

    item_id = 1

    raw_lines = open(txtfile, 'r', encoding="utf-8").read().splitlines()

    for line in raw_lines:

        basket,items_dict, item_id, C1= encode_products(line, items_dict,item_id,C1)  # see comments in encode_products function

        BASKETS.append(basket)

    C1_before_size = get_size_in_MB(C1)

    len_before_C1 = len(C1)

    threshold = round(support * len(BASKETS), 0)

    C1 = filter_infrequent_items(C1, threshold)

    len_after_C1 = len(C1)

    items_dict = reverse_dict(items_dict)

    load_time = time_needed(t0)

    basket_size = get_size_in_MB(BASKETS)

    items_dict_size = get_size_in_MB(items_dict)

    stats = {}

    stats["time"] = {}

    stats["time"]["load_and_1st_pass"] = load_time

    stats["sizes"] = {}

    stats["sizes"]["C1"] = C1_before_size

    stats["len"] = {}

    stats["len"]["C1"] = {"before":len_before_C1,"after":len_after_C1}

    if verbose == True:

        print("Loading the basket from the file, encoding the item and finding the candidate for the second pass of the Apriori took {} minutes".format(load_time))

        print("The size of the list of baskets is {} MB".format(basket_size))

        print("The size of the list of the items dict is {} MB".format(items_dict_size))

        print("The size of the list of the candidate for the second iteration before filtering the infrequent items is {} MB".format(C1_before_size))

        print("C1 contains {} elements, before dropping the infrequent ones".format(len_before_C1))

        print("C1 contains {} elements, after dropping the infrequent ones".format(len_after_C1))

        print("_--_" * 10)

    return BASKETS, items_dict, [C1], stats, threshold















