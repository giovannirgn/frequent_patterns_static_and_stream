from apriori import apriori
from PCY import pcy
from load_function import load_for_stream
from stream_exponential_decay import stream_exponential_decay
from stream_multiple_apriori import multiple_apriori


#list_of_candidates_dict, stats = apriori(r"data\baskets.txt",support =0.0025,verbose = True)

#list_of_candidates_dict, stats = pcy(r"data\baskets.txt",support =0.0025, verbose = True)

#stream_exponential_decay(load_for_stream(r"data\baskets.txt"),decay=0.005, drop_threshold=0.5, verbose = True)

#multiple_apriori(load_for_stream(r"data\baskets.txt"),len_batch=,support=.0025)