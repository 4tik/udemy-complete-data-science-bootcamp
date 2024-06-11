import pandas as pd

values = [1,2,3,4]
pandas_values = pd.Series(values)
print(pandas_values)

indexing = {
    "one": 1,
    "second": 2,
    "third": 3
}

pandas_values = pd.Series(indexing)
print(pandas_values)