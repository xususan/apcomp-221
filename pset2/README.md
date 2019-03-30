# APComp 221

## General

We are using Python 3 (any version should work). We also use PyTest for testing purposes. 

## Run tests

First install pytest:

    pip3 install pytest
    pytest

To run an individual test:


    pytest -k clean_csv


## 1. Removing duplicates


count_columns helps us understand the distribution of corrupt lines by counting how many columns are found in the csv.

Example usage: 

```
python3 src/count_columns.py datasets/dirty_sample_small.csv
```

## 1. Distribution of quasi-identifiers in the US

To run our script, make sure you have R (3.5.2 or above verified) installed. Open up R or Rstudio, and run `source "problem_1.R`. It will take a little bit of time, but it will then print desired values to Terminal.


## 2. quasi-identifier CSV

`quasi_reduce.py` is used to output a CSV that only has the quasi-identifiers for a given dataset. 

Arguments: 
1. The path to the full dataset. 
2. The desired path to the output dataset. 
3. Config file that, at minimum, lists the quasi-identifiers and identifiers in the dataset. 

```
python3 src/quasi_reduce.py datasets/mid_sample_set.csv output/quasi.csv config/quasi.config
```

## 3. k-anonymous suppression

`k_suppress.py` is used to output a CSV that is made k-anonymous for a given value of k. This script will suppress any row that does not have k copies of its quasi-identifiers in the dataset.

Arguments: 
1. The path to the dataset to make k-anonymous. 
2. Config file that, at minimum, lists the quasi-identifiers and identifiers in the dataset. 
3. The desired path to the output dataset. 
4. Value of k.

```
python3 src/k_suppress.py output/quasi.csv config/quasi.config output/k3.csv 3
python3 src/k_suppress.py output/quasi.csv config/quasi.config output/k4.csv 4
python3 src/k_suppress.py output/quasi.csv config/quasi.config output/k5.csv 5
```

```

