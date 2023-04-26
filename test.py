# 0.00 
# 100.00 100.00 
# 150.00 300.00 150.00 
# 175.00 425.00 425.00 175.00 
# 187.50 500.00 625.00 500.00 187.50 
# 193.75 543.75 762.50 762.50 543.75 193.75 
# 196.88 568.75 853.12 962.50 853.12 568.75 196.88 

from ChainingHashTable import ChainingHashTable
from LinearProbingHashTable import LinearProbingHashTable
from QuadraticProbingHashTable import QuadraticProbingHashTable
from DoubleHashingHashTable import DoubleHashingHashTable

keys = [
    "Los Angeles", "Houston", "Washington",
    "Chicago", "San Francisco", "Dallas",
    "Tokyo", "New York", "Vancouver"
]
values = [
    "LAX", "IAH", "IAD",
    "ORD", "SFO", "DAL",
    "NRT", "JFK", "YVR"
]
      
initialCapacity = 11

# Initialize the four types of hash tables
tables = [
    ChainingHashTable(initialCapacity),
    LinearProbingHashTable(initialCapacity),
    QuadraticProbingHashTable(1, 1, initialCapacity),
    DoubleHashingHashTable(initialCapacity)
]
      
# Add the same content to each hash table
for i in range(len(keys)):
    # Insert the item into each hash table
    for j in range(len(tables)):
        tables[j].insert(keys[i], values[i])
      
# Print each table's buckets
tableNames = [
    "Chaining",
    "Linear probing",
    "Quadratic probing",
    "Double hashing"
]
for j in range(len(tables)):
    print("%s: initial table:" % tableNames[j])
    print(tables[j])
      
# Remove the 3 oldest keys from each hash table
for i in range(3):
    for j in range(len(tables)):
        tables[j].remove(keys[i])
      
# Print each table's buckets again
print("")
for j in range(len(tables)):
    print("%s after removal:" % tableNames[j])
    print(tables[j])