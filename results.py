from utils import pipeline_dict, precision, false_positive
import pickle

item_dict = pickle.load(open(r"data/item_dict.p", "rb"))

apriori_freq = pipeline_dict(pickle.load(open("results/frequent_itemset_apriori.p", "rb")),item_dict)
apriori_stat = pickle.load(open("results/stat_apriori.p", "rb"))

pcy_freq = pipeline_dict(pickle.load(open("results/frequent_itemset_pcy.p", "rb")),item_dict)
pcy_stat = pickle.load(open("results/stat_pcy.p", "rb"))

stream_decay = pipeline_dict([pickle.load(open("results/stream_exponential_decay_apriori.p", "rb"))],item_dict)
stream_apriori = pipeline_dict([pickle.load(open("results/stream_multiple_apriori.p", "rb"))],item_dict)

#print(f"The percentage of frequent items identified by the decay stream is {precision(apriori_freq,stream_decay)}% of the real frequent itemset")
#print(f"The percentage of frequent items identified by apriori stream is {precision(apriori_freq,stream_apriori)}% of the real frequent itemset")

#print(f"The percentage of false positive of the decay stream is {false_positive(apriori_freq,stream_decay)}%")
#print(f"The percentage of false positive of the apriori stream is {false_positive(apriori_freq,stream_apriori)}%")


pickle.dump(apriori_freq, open(r"results\apriori_decpded.p", "wb"))
pickle.dump(pcy_freq, open(r"results\pcy_decpded.p", "wb"))
pickle.dump(stream_decay, open(r"results\decay_decpded.p", "wb"))
pickle.dump(stream_apriori, open(r"results\stream_apriori_decpded.p", "wb"))