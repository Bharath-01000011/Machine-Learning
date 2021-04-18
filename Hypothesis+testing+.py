import pandas as pd
import numpy as np
import scipy 
from scipy import stats
import statsmodels.api as sm
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

data=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/with and without additive.csv")

withoutAdditive_data=stats.shapiro(data.Without_additive)
withoutAdditive_pValue=withoutAdditive_data[1]
print("p-value is: "+str(withoutAdditive_pValue))

Additive=stats.shapiro(data.With_Additive)
Additive_pValue=Additive[1]
print("p-value is: "+str(Additive_pValue))

from scipy.stats import mannwhitneyu
mannwhitneyu(data.Without_additive, data.With_Additive)

promotion=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/Promotion.csv")

Promotion=stats.shapiro(promotion.InterestRateWaiver)
Promotion_pValue=Promotion[1]
print("p-value is: "+str(Promotion_pValue))

SDPromotion=stats.shapiro(promotion.StandardPromotion)
SDPromotion_pValue=Promotion[1]
print("p-value is: "+str(SDPromotion_pValue))

scipy.stats.levene(promotion.InterestRateWaiver, promotion.StandardPromotion)

scipy.stats.ttest_ind(promotion.InterestRateWaiver,promotion.StandardPromotion)

scipy.stats.ttest_ind(promotion.InterestRateWaiver,promotion.StandardPromotion,equal_var = True)

from statsmodels.formula.api import ols
cof=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/ContractRenewal_Data(unstacked).csv")
cof.columns="SupplierA","SupplierB","SupplierC"

SupA=stats.shapiro(cof.SupplierA)
SupA_pValue=SupA[1]
print("p-value is: "+str(SupA_pValue))

SupB=stats.shapiro(cof.SupplierB)
SupB_pValue=SupB[1]
print("p-value is: "+str(SupB_pValue))

SupC=stats.shapiro(cof.SupplierC)
SupC_pValue=SupC[1]
print("p-value is: "+str(SupC_pValue))

scipy.stats.levene(cof.SupplierA, cof.SupplierB)
scipy.stats.levene(cof.SupplierB, cof.SupplierC)
scipy.stats.levene(cof.SupplierC, cof.SupplierA)

mod=ols('SupplierA~SupplierB+SupplierC',data=cof).fit()
aov_table=sm.stats.anova_lm(mod,type=2)
print(aov_table)


Bahaman=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/Bahaman.csv")
count=pd.crosstab(Bahaman["Defective"],Bahaman["Country"])
count

Chisquares_results=scipy.stats.chi2_contingency(count)
Chi_pValue=Chisquares_results[1]
print("p-value is: "+str(Chi_pValue))

import statsmodels.stats.descriptivestats as sd
data=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/Signtest.csv")

data_socres=stats.shapiro(data.Scores)
data_pValue=data_socres[1]
print("p-value is: "+str(data_pValue))

sd.sign_test(data.Scores,mu0=0)

two_prop_test=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/JohnyTalkers.csv")

from statsmodels.stats.proportion import proportions_ztest

tab = two_prop_test.groupby(['Person', 'Icecream']).size()
count = np.array([58, 152]) 
nobs = np.array([480, 740]) 

stat, pval = proportions_ztest(count, nobs,alternative='two-sided') 
print('{0:0.3f}'.format(pval))

stat, pval = proportions_ztest(count, nobs,alternative='larger')
print('{0:0.3f}'.format(pval))
