import pandas as pd
import scipy 
from scipy import stats
import statsmodels.stats.descriptivestats as sd
data=pd.read_excel("E:/Day Wise/Day 08 Hypothesis Testing/Data/Marks-1sample sign test.xlsx")

print(stats.shapiro(data.Marks))

sd.sign_test(data.Marks,mu0=82)
help(sd.sign_test)

data=pd.read_excel("E:\Excelr Data\RCodes\Hyothesis Testing\Mann_whitney.xlsx")
data
data.columns="Without_additive","With_additive"
print(stats.shapiro(data.Without_additive))
print(stats.shapiro(data.With_additive))

scipy.stats.mannwhitneyu(data.Without_additive, data.With_additive)

promotion=pd.read_excel("E:/Day Wise/Day 08 Hypothesis Testing/Data/Promotion.xlsx")
promotion
promotion.columns = "Credit","Promotion.Type","InterestRateWaiver","StandardPromotion"

print(promotion.columns)
print(scipy.stats.anderson(promotion.InterestRateWaiver,dist = 'norm'))

print(scipy.stats.anderson(promotion.StandardPromotion,dist = 'norm'))
help(stats.shapiro)

scipy.stats.ttest_ind(promotion.InterestRateWaiver,promotion.StandardPromotion,nan_policy='omit')
help(scipy.stats.ttest_ind)


cof=pd.read_excel("E:/Excelr Data/RCodes/Hyothesis Testing/ContractRenewal_Data(unstacked).xlsx")
cof
cof.columns="SupplierA","SupplierB","SupplierC"

scipy.stats.levene(cof.SupplierA, cof.SupplierB,cof.SupplierC)
help(scipy.stats.levene)

stats.f_oneway(cof.SupplierA , cof.SupplierB , cof.SupplierC)

Bahaman=pd.read_excel("E:/Day Wise/Day 08 Hypothesis Testing/Data/Bahaman.xlsx")
Bahaman

count=pd.crosstab(Bahaman["Defective"],Bahaman["Country"])
count
Chisquares_results=scipy.stats.chi2_contingency(count)
help(scipy.stats.chi2_contingency)
Chisquares_results
Chi_square=[['','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]

