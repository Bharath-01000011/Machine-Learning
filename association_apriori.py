import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules

groceries = []

with open("E:\\bokey\\Excelr Data\\Python Codes\\association rules\\groceries.csv") as f:
    groceries = f.read()

groceries = groceries.split("\n")
groceries_list = []
for i in groceries:
    groceries_list.append(i.split(","))

all_groceries_list = [i for item in groceries_list for i in item]
from collections import Counter

item_frequencies = Counter(all_groceries_list)

item_frequencies = sorted(item_frequencies.items(),key = lambda x:x[1])
frequencies = list(reversed([i[1] for i in item_frequencies]))
items = list(reversed([i[0] for i in item_frequencies]))


import matplotlib.pyplot as plt

plt.bar(height = frequencies[0:11],left = list(range(0,11)),color='rgbkymc');plt.xticks(list(range(0,11),),items[0:11]);plt.xlabel("items")
plt.ylabel("Count")

groceries_series  = pd.DataFrame(pd.Series(groceries_list))
groceries_series = groceries_series.iloc[:9835,:] # removing the last empty transaction

groceries_series.columns = ["transactions"]
X = groceries_series['transactions'].str.join(sep='*').str.get_dummies(sep='*')

frequent_itemsets = apriori(X, min_support=0.005, max_len=3,use_colnames = True)
frequent_itemsets.sort_values('support',ascending = False,inplace=True)
plt.bar(left = list(range(1,11)),height = frequent_itemsets.support[1:11],color='rgmyk');plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item-sets');plt.ylabel('support')
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head(20)
rules.sort_values('lift',ascending = False,inplace=True)

 
def to_list(i):
    return (sorted(list(i)))


ma_X = rules.antecedants.apply(to_list)+rules.consequents.apply(to_list)


ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]
index_rules = []
for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))

rules_no_redudancy  = rules.iloc[index_rules,:]
rules_no_redudancy.sort_values('lift',ascending=False).head(10)


