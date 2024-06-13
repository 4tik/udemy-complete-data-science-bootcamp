

import numpy as np
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values= np.nan, strategy='mean')

data = [
    [12, np.nan, 34],
    [10, 32, np.nan],
    [np.nan, 11, 20]
]

print(f"Orginal data : {data}")
imputer = imputer.fit(data)
data = imputer.transform(data)

print(f"after impute : {data}")