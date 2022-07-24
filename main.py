from apriori import apriori
from PCY import pcy

list_of_candidates_dict, stats = apriori(r"data\baskets.txt",support =0.0025)
print("**********"*10)
list_of_candidates_dict, stats = pcy(r"data\baskets.txt",support =0.0025)