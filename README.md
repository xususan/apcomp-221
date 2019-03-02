# APComp 221

## 2. quasi-identifier CSV

`python3 quasi_reduce.py mid_sample_set.csv quasi.csv quasi.config`

## 3. k-anonymous suppression

`python3 k_suppress.py quasi.csv quasi.config k3.csv 3`
`python3 k_suppress.py quasi.csv quasi.config k4.csv 4`
`python3 k_suppress.py quasi.csv quasi.config k5.csv 5`

## 4. k-anonymous synthetic
`python3 k_synthetic.py quasi.csv k_synthetic_3.csv 3`
`python3 k_synthetic.py quasi.csv k_synthetic_4.csv 4`
`python3 k_synthetic.py quasi.csv k_synthetic_5.csv 5`

## 5. k-anonymous generalization, blurring, and suppression

