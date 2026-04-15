# -------- DataFrame example --------




import pandas as pd

mydataset = {
    "Name": ["Manish", "Yash", "Atul"],
    "System_ID": [2025066457453, 202564545, 6569544]
}

myvar = pd.DataFrame(mydataset)

print(myvar)



# -------- Series example --------



import pandas as pd

data = ["Manish", "Yash", "Atul"]

myvar = pd.Series(data)

print(myvar)



# -------- DataFrame from list --------



import pandas as pd

data = ["Manish", "Yash", "Atul"]

myvar = pd.DataFrame(data)

print(myvar)


import numpy as np
import pandas as pd

data = {
    "num_legs": [2, 4, 8, 0],
    "num_wings": [2, 0, 0, 0],
    "num_specimens": [8, 2, 5, 6]
}

index_names = ["sparrow", "fox", "spider", "snake"]

myvar = pd.DataFrame(data, index=index_names)

print(myvar)
