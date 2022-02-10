import pandas as pd
from sqlalchemy import create_engine

# Read data from txt file in datasets folder
df = pd.read_csv('./datasets/The_Joy_Of_Painting-Episode_Dates.txt', sep="\t")
df2 = pd.read_csv('./datasets/The_Joy_Of_Painting-Subject_Matter.txt', sep="\t")
df3 = pd.read_csv('./datasets/The_Joy_Of_Painting-Colors_Used.txt', sep="\t")

engine = create_engine('postgresql://postgres:hank@localhost:5432/postgres')

df.to_sql('episode_dates', engine, if_exists='replace')
df2.to_sql('subject_matter', engine, if_exists='replace')
df3.to_sql('colors_used', engine, if_exists='replace')