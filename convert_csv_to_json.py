import pandas as pd 

df = pd.read_csv(
    "datasets/ecommerce_data.csv", 
    sep=",", 
    encoding="iso-8859-1",
    on_bad_lines="skip", 
    index_col=False
)
df.to_json("datasets/ecommerce_data.json")