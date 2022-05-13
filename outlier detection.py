from collections import Counter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("banknotes.csv")
print(df.head())

sns.boxplot(data=df,x=df["Length"])
plt.title("Boxplot of Swiss Banknote Length ")
df_outlier1 = df[df['Length']> 216].copy()
print(Counter(df_outlier1['conterfeit']))
df_outlier2 = df[df['Length']> 215.5].copy()
print(Counter(df_outlier2['conterfeit']))
def boxplot(column):
    sns.boxplot(data=df,x=df[f"{column}"])
    plt.title(f"Boxplot of Swiss Banknote {column}")
    plt.show()
boxplot('Length')
boxplot('Right')
boxplot('Left')
boxplot('Bottom')
boxplot('Top')
boxplot('Diagonal')
df_outlier3 = df[(df['Length']> 215)&(df['Right']> 130)&(df['Left']> 
130)&(df['Bottom']> 10)].copy()
print(Counter(df_outlier3['conterfeit']))