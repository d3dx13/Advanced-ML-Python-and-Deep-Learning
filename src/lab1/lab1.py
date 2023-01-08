import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rosstat_salaty: pd.DataFrame = pd.read_csv(
    'ROSSTAT_SALARY_RU_2019_normalized.csv',
    delimiter=',',
    decimal='.',
    index_col='REGION_NAME'
)
rosstat_salaty = rosstat_salaty.drop(["Алтайский край",
                                      "Ростовская область",
                                      "Еврейская АО",
                                      "Ямало-Ненецкий АО",
                                      "Амурская область"])
rosstat_salaty = rosstat_salaty.sort_values(by='SALARY')
rosstat_salaty['index'] = list(range(1, len(rosstat_salaty.index) + 1))

print(rosstat_salaty)

for interest_index in [54, 67, 69]:
    print(interest_index, " - ", rosstat_salaty[rosstat_salaty["index"] == interest_index]["SALARY"].values)

print(rosstat_salaty["SALARY"].mean())

print(rosstat_salaty["SALARY"].median())
