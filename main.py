from apriori import apriori

list_of_candidates_dict, stats = apriori(r"data\baskets.txt",support =0.0025)