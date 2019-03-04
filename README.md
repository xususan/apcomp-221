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

    python3 src/quasi_reduce.py datasets/mid_sample_set.csv output/quasi.csv config/quasi.config

## 3. k-anonymous suppression

    python3 src/k_suppress.py output/quasi.csv config/quasi.config output/k3.csv 3
    python3 src/k_suppress.py output/quasi.csv config/quasi.config output/k4.csv 4
    python3 src/k_suppress.py output/quasi.csv config/quasi.config output/k5.csv 5

## 4. k-anonymous synthetic

    python3 src/k_synthetic.py output/quasi.csv config/quasi.config output/k_synthetic_3.csv 3
    python3 src/k_synthetic.py output/quasi.csv config/quasi.config output/k_synthetic_4.csv 4
    python3 src/k_synthetic.py output/quasi.csv config/quasi.config output/k_synthetic_5.csv 5

## 5. k-anonymous generalization, blurring, and suppression

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

