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

    threshold = round(support * len(BASKETS), 0)

    C1 = filter_infrequent_items(C1, threshold)
    items_dict = reverse_dict(items_dict)

    load_time = time_needed(t0)

    basket_size = get_size_in_MB(BASKETS)
    C1_size = get_size_in_MB(C1)
    items_dict_size = get_size_in_MB(items_dict)

    if verbose == True:

        print("Loading the basket from the file, encoding the item and finding the candidate for the second pass of the Apriori took {} minutes".format(load_time))

        print("The size of the list of baskets is {} MB".format(basket_size))

        print("The size of the list of the items dict is {} MB".format(items_dict_size))

        print("The size of the list of the candidate for the second iteration is {} MB".format(C1_size))


    return BASKETS, items_dict, [C1], basket_size, items_dict_size, C1_size,load_time, threshold















