import pandas as pd

mydataset = {
    "Name": ["Manish", "Yash", "Atul"],
    "System_ID": [20250666283, 202564545, 6569544]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
