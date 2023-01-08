import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pulsar_stars = pd.read_csv(
    'data/trial/asset-v1_ITMOUniversity+DATANFST2035+cifru_2035+type@asset+block@pulsar_stars_new.csv',
    delimiter=',',
    decimal='.'
)
print(pulsar_stars)

pulsar_stars_new = pulsar_stars[
    ((pulsar_stars.TG == 0) & (104.1953125 <= pulsar_stars.MIP) & (pulsar_stars.MIP <= 104.5859375)) |
    ((pulsar_stars.TG == 1) & (5.8125 <= pulsar_stars.MIP) & (pulsar_stars.MIP <= 14.1484375))
]


print(pulsar_stars_new)
print(pulsar_stars_new.MIP.mean())
