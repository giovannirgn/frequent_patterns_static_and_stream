# frequent_patterns_static_and_stream
This project aims at comparing the performance of two algorithms used in market modeling: the A-priori algorithm and its variant, the Park Chen Yu algorithm.

Both models will be compared in terms of memory requirements and timeliness.
The algorithms extract frequent patterns on the whole dataset (baskets) therefore they will return all the really frequent items (all the items that exceed given support).

If the dataset is continuously evolving (stream) it is no longer possible to run the analysis on the whole dataset. Thus, in this project will be analyzed two solutions to count frequent items in a datastream: using a decay window and a sampling method.
These two approaches will be compared in terms of time requirements, accuracy (the ability to identify the frequent items), and the share of false positives generated.
