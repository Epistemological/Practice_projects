import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table('bpds_full.dat', sep='\t', dtype=object, chunksize=50000)

df1 = pd.DataFrame(df)
FTG = df1.loc[df1['subscriptionOwnerType']] == 'FTG'
null = df1.loc[df1['registrationNumber']] == 'null'

print(FTG)
print(null)
