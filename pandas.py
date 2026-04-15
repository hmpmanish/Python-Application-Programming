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
