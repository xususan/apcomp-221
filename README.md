# APComp 221

## General

We are using Python 3 (any version should work). We also use PyTest for testing purposes. 

## Run tests

First install pytest:

    pip3 install pytest
    pytest

To run an individual test:

    pytest -k k_suppress

## Config File
An example config file (which contains the quasi-identifiers and identifiers specified on Canvas) can be found in quasi.config. The config file is a JSON, with the following entries:
- `delete_columns`: a list of column names that are identifiers and should be removed from the dataset altogether.
- `quasi_identifiers`: a list of column names that are quasi-identifiers, and will need to be made k-anonymous.
- `generalize_columns`: used in `k_blur.py`, a list of columns to generalize (i.e, replace city with state and so on)
- `blur_columns`: used in `k_blur.py`, a list of (continuous) columns to group into larger bin sizes.
- `sensitive_columns`: used in `l_diversity.py`, a list of columns that may be considered sensitive to members of the dataset.

## Data Analysis

count_column_uniques helps us understand the distribution of our quasi-identifiers, by printing out what the unique values are for each quasi-identifier column, and the number of times each value appears in the dataset.

Example usage: 

    python3 src/count_column_uniques.py datasets/mid_sample_set.csv config/quasi.config

## 1. Distribution of quasi-identifiers in the US

To run our script, make sure you have R (3.5.2 or above verified) installed. Open up R or Rstudio, and run `source "problem_1.R`. It will take a little bit of time, but it will then print desired values to Terminal.


## 2. quasi-identifier CSV

`quasi_reduce.py` is used to output a CSV that only has the quasi-identifiers for a given dataset. 

Arguments: 
1. The path to the full dataset. 
2. The desired path to the output dataset. 
3. Config file that, at minimum, lists the quasi-identifiers and identifiers in the dataset. 

    python3 src/quasi_reduce.py datasets/mid_sample_set.csv output/quasi.csv config/quasi.config

## 3. k-anonymous suppression

`k_suppress.py` is used to output a CSV that is made k-anonymous for a given value of k. This script will suppress any row that does not have k copies of its quasi-identifiers in the dataset.

Arguments: 
1. The path to the dataset to make k-anonymous. 
2. Config file that, at minimum, lists the quasi-identifiers and identifiers in the dataset. 
3. The desired path to the output dataset. 
4. Value of k.

    python3 src/k_suppress.py output/quasi.csv config/quasi.config output/k3.csv 3
    python3 src/k_suppress.py output/quasi.csv config/quasi.config output/k4.csv 4
    python3 src/k_suppress.py output/quasi.csv config/quasi.config output/k5.csv 5

## 4. k-anonymous synthetic

`k_synthetic.py` is used to output a CSV that is made k-anonymous for a given value of k. This script will add synthetic records until there are at least k records with a given set of a quasi-identifiers.

Arguments: 
1. The path to the dataset to make k-anonymous. 
2. Config file that, at minimum, lists the quasi-identifiers and identifiers in the dataset. 
3. The desired path to the output dataset. 
4. Value of k.

    python3 src/k_synthetic.py output/quasi.csv config/quasi.config output/k_synthetic_3.csv 3
    python3 src/k_synthetic.py output/quasi.csv config/quasi.config output/k_synthetic_4.csv 4
    python3 src/k_synthetic.py output/quasi.csv config/quasi.config output/k_synthetic_5.csv 5

## 5. k-anonymous generalization, blurring, and suppression

For this problem, we ran generalization and blurring using `k_blur.py`, and fed the resulting CSV through `k_suppress.py` to make the resulting CSV k-anonymous.

Step 1:
Run `k_blur.py`, with arguments as follows:

Arguments:
1. The path to the dataset to make k-anonymous. 
2. Config file that lists the quasi-identifiers, identifiers, list of columns to generalize, and list of columns to blur in the dataset. 
3. The desired path to the output dataset. 
4. Minimum number of values in each bin for blurring. For example, passing a value of 100 means that for each column to blur, we will bin it such that there are at least 100 records in a given bin.

Step 2:
Run `k_suppress.py` with the output from the previous step.

    python3 src/k_blur.py output/quasi.csv config/quasi.config output/k_blur_10.csv 10
    python3 src/k_blur.py output/quasi.csv config/quasi.config output/k_blur_100.csv 100
    python3 src/k_blur.py output/quasi.csv config/quasi.config output/k_blur_1000.csv 1000
    python3 src/k_blur.py output/quasi.csv config/quasi.config output/k_blur_10000.csv 10000
    python3 src/k_suppress.py output/k_blur_10.csv config/quasi.config output/k_blur_10_suppress_3.csv 3
    python3 src/k_suppress.py output/k_blur_100.csv config/quasi.config output/k_blur_100_suppress_3.csv 3
    python3 src/k_suppress.py output/k_blur_1000.csv config/quasi.config output/k_blur_1000_suppress_3.csv 3
    python3 src/k_suppress.py output/k_blur_10000.csv config/quasi.config output/k_blur_10000_suppress_3.csv 3
    python3 src/k_suppress.py output/k_blur_10.csv config/quasi.config output/k_blur_10_suppress_4.csv 4
    python3 src/k_suppress.py output/k_blur_100.csv config/quasi.config output/k_blur_100_suppress_4.csv 4
    python3 src/k_suppress.py output/k_blur_1000.csv config/quasi.config output/k_blur_1000_suppress_4.csv 4
    python3 src/k_suppress.py output/k_blur_10000.csv config/quasi.config output/k_blur_10000_suppress_4.csv 4
    python3 src/k_suppress.py output/k_blur_10.csv config/quasi.config output/k_blur_10_suppress_5.csv 5
    python3 src/k_suppress.py output/k_blur_100.csv config/quasi.config output/k_blur_100_suppress_5.csv 5
    python3 src/k_suppress.py output/k_blur_1000.csv config/quasi.config output/k_blur_1000_suppress_5.csv 5
    python3 src/k_suppress.py output/k_blur_10000.csv config/quasi.config output/k_blur_10000_suppress_5.csv 5

## 6. l-diversity

`l_diversity.py` counts, for each sensitive feature, how many values the feature takes on for each possible combination of the quasi-identifiers. For example, a row in the output that says "1   153" indicates that there are 153 quasi-identifiers that have only one corresponding feature value. The overall `l-diversity` with respect to a given sensitive feature is therefore the minimum of these frequency counts, but for visualization's sake we output all frequency counts.

Arguments:
1. Path to dataset to analyze.
2. Config file, that lists at minimum a set of quasi-identifier columns, identifier columns, and columns considered sensitive. 

    python3 src/l_diversity.py datasets/mid_sample_set.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_10_suppress_3.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_100_suppress_3.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_1000_suppress_3.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_10000_suppress_3.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_10_suppress_4.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_100_suppress_4.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_1000_suppress_4.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_10000_suppress_4.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_10_suppress_5.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_100_suppress_5.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_1000_suppress_5.csv config/quasi.config
    python3 src/l_diversity.py output/k_blur_10000_suppress_5.csv config/quasi.config

