# APComp 221

## General

    python3 count_columns_uniques.py mid_sample_set.csv quasi.config

## Run tests

First install pytest:

    pip3 install pytest
    pytest

To run an individual test:

    pytest -k k_suppress

## 2. quasi-identifier CSV

    python3 quasi_reduce.py mid_sample_set.csv quasi.csv quasi.config

## 3. k-anonymous suppression

    python3 k_suppress.py quasi.csv quasi.config k3.csv 3
    python3 k_suppress.py quasi.csv quasi.config k4.csv 4
    python3 k_suppress.py quasi.csv quasi.config k5.csv 5

## 4. k-anonymous synthetic

    python3 k_synthetic.py quasi.csv quasi.config k_synthetic_3.csv 3
    python3 k_synthetic.py quasi.csv quasi.config k_synthetic_4.csv 4
    python3 k_synthetic.py quasi.csv quasi.config k_synthetic_5.csv 5

## 5. k-anonymous generalization, blurring, and suppression

    python3 k_blur.py quasi.csv quasi.config k_blur_10.csv 10
    python3 k_blur.py quasi.csv quasi.config k_blur_100.csv 100
    python3 k_blur.py quasi.csv quasi.config k_blur_1000.csv 1000
    python3 k_blur.py quasi.csv quasi.config k_blur_10000.csv 10000
    python3 k_suppress.py k_blur_10.csv quasi.config k_blur_10_suppress_3.csv 3
    python3 k_suppress.py k_blur_100.csv quasi.config k_blur_100_suppress_3.csv 3
    python3 k_suppress.py k_blur_1000.csv quasi.config k_blur_1000_suppress_3.csv 3
    python3 k_suppress.py k_blur_10000.csv quasi.config k_blur_10000_suppress_3.csv 3
    python3 k_suppress.py k_blur_10.csv quasi.config k_blur_10_suppress_4.csv 4
    python3 k_suppress.py k_blur_100.csv quasi.config k_blur_100_suppress_4.csv 4
    python3 k_suppress.py k_blur_1000.csv quasi.config k_blur_1000_suppress_4.csv 4
    python3 k_suppress.py k_blur_10000.csv quasi.config k_blur_10000_suppress_4.csv 4
    python3 k_suppress.py k_blur_10.csv quasi.config k_blur_10_suppress_5.csv 5
    python3 k_suppress.py k_blur_100.csv quasi.config k_blur_100_suppress_5.csv 5
    python3 k_suppress.py k_blur_1000.csv quasi.config k_blur_1000_suppress_5.csv 5
    python3 k_suppress.py k_blur_10000.csv quasi.config k_blur_10000_suppress_5.csv 5

## 6. l-diversity

    python3 l_diversity.py k_blur_10_suppress_3.csv quasi.config
    python3 l_diversity.py k_blur_100_suppress_3.csv quasi.config
    python3 l_diversity.py k_blur_1000_suppress_3.csv quasi.config
    python3 l_diversity.py k_blur_10000_suppress_3.csv quasi.config
    python3 l_diversity.py k_blur_10_suppress_4.csv quasi.config
    python3 l_diversity.py k_blur_100_suppress_4.csv quasi.config
    python3 l_diversity.py k_blur_1000_suppress_4.csv quasi.config
    python3 l_diversity.py k_blur_10000_suppress_4.csv quasi.config
    python3 l_diversity.py k_blur_10_suppress_5.csv quasi.config
    python3 l_diversity.py k_blur_100_suppress_5.csv quasi.config
    python3 l_diversity.py k_blur_1000_suppress_5.csv quasi.config
    python3 l_diversity.py k_blur_10000_suppress_5.csv quasi.config

