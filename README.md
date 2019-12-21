# Assignment 3

The goal of assignment 3 was to use the map reduce algorithm to count the number of flights by each carrier. The data set used had 120 million records starting in October 1987 and ending in April 2008. 

The first step before starting the map reduce algorithm was to use multiprocessing to load the 120 million records of data. It took 5 min 30s to load the data into the notebook, which is much faster than the serial code. 

Once the data was loaded the next task was to count the number of flights by carrier using map reduce. There are three steps in the map reduce algorithm, starting with the mapping step, then the shuffling step, and finally the reducing step. All steps in the map reduce algorithm come from the “mapreduce “class in the “mapreduce1.py” file.  

In the mapping step a list of all the carriers taken from the “UniqueCarrier” column in each data set when loaded in to the notebook are mapped by adding a 1 next to the carrier when the carrier had a flight. Next is the shuffling step where the list from the mapping step is sorted by carrier. For example, all the records with carrier ‘AA’ are now grouped together. The last step is the reduce step which is where all the sorted values from the shuffling step are counted for each carrier. The final count for each carrier is done in the step and shown in the conclusion. 
