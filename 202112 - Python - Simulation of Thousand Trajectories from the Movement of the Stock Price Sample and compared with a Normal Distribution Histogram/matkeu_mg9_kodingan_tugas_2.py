# -*- coding: utf-8 -*-
"""Matkeu-MG9-Kodingan Tugas 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18ctbGMYJD64GLSsxl1Y5zswgI4d0w4gb

# No 1
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import io
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
# %matplotlib inline

print("Dipilih nilai dari: ")
S0 = 915
print("S0 = ", S0)
Miu = 0.045
print("Miu = ", Miu)
Sigma = 0.15
print("Sigma (Tidak boleh diatas 50%) = ", Sigma)
print("Dipilih T = 4 tahun dengan tiap tahun dibagi menjadi 250 unit waktu")
T_1 = 4
n_1 = 250*T_1
delta_T_1 = T_1/n_1
print("delta_T = ", delta_T_1)

data1 = pd.read_csv("No1.csv")
data1 = data1[["Hrg shm pd wkt (masa mendatang)","Hrg"]]
No1 = data1.set_index('Hrg shm pd wkt (masa mendatang)')
No1.head()

No1.tail()

"""## 1b"""

No1.plot(figsize = (12,4))
hrg_shm_thdp_wkt_1 = plt.show()

"""## 1c

### Daily Return
"""

return_daily_1 = No1.pct_change().dropna()
return_daily_1 = return_daily_1.rename({'Hrg':'Daily Return'}, axis=1)
return_daily_1.head()

return_daily_1.plot(figsize = (12,4))
plt.show()

"""### Daily Log Return"""

No1['Log Return'] = np.log(No1['Hrg']).diff()
No1

No1['Log Return'].plot(figsize = (12,4))
daily_log_return_1 = plt.show()

"""## 1e"""

mean_teoritis_1 = (Miu-(((Sigma*Sigma)/2)))*T_1
print("Mean Teoritis:", mean_teoritis_1)

u_1 = return_daily_1.mean()
print("Mean Empirik (daily return):", u_1)

u_log1 = No1['Log Return'].mean()
print("Mean Empirik (daily log return):", u_log1)

var_teoritis_1 = (Sigma*Sigma)*T_1
print("Var Teoritis:", var_teoritis_1)

var_1 = return_daily_1.var()
print("Var Empirik (daily return):", var_1)

var_log1 = No1['Log Return'].var()
print("Var Empirik (daily log return):", var_log1)

drift_1 = u_1 - (0.5 * var_1)
drift_1

drift_log1 = u_log1 - (0.5 * var_log1)
drift_log1

stdev_1 = return_daily_1.std()
stdev_1

stdev_log1 = No1['Log Return'].std()
stdev_log1

"""## 1a"""

iteration_1 = 1

return_daily_1a = np.exp(drift_1.values + stdev_1.values * norm.ppf(np.random.rand(n_1,iteration_1)))
return_daily_1a = np.array(return_daily_1a)
return_daily_1a

S_1 = data1.iloc[-1:,-1]
S_1

price_list_1 = np.zeros_like(return_daily_1a)
price_list_1 = np.array(price_list_1)
price_list_1

price_list_1[0] = S_1
price_list_1

for t_1 in range(1, n_1):
    price_list_1[t_1] = price_list_1[t_1 - 1] * return_daily_1a[t_1]

price_list_1

plt.figure(figsize=(10,6))
plt.plot(price_list_1)
plt.title("1 Kemungkinan Pergerakan Harga Saham", fontsize = 15)
plt.ylabel("Harga Saham", fontsize = 10)
plt.xlabel("Waktu", fontsize = 10)
plt.show()

"""## 1d"""

import seaborn as sns
import pandas as pd
import numpy as np

sns.distplot(No1['Log Return']

hist_1 = plt.hist(No1['Log Return'])

"""# No 2"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import io
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
# %matplotlib inline

print("Dipilih nilai dari: ")
S0 = 915
print("S0 = ", S0)
Miu = 0.045
print("Miu = ", Miu)
Sigma = 0.15
print("Sigma (Tidak boleh diatas 50%) = ", Sigma)
print("Dipilih T = 4 tahun dengan tiap tahun dibagi menjadi 250 unit waktu")
T_2 = 1
n_2 = 250*T_2
delta_T_2 = T_2/n_2
print("delta_T = ", delta_T_2)

data2 = pd.read_csv("No2.csv")
data2 = data2[["Hrg shm pd wkt (masa mendatang)","Hrg"]]
No2 = data2.set_index('Hrg shm pd wkt (masa mendatang)')
No2.head()

No2.tail()

"""## 2b"""

hist_2 = plt.hist(No2['Hrg'])

"""## 2c"""

No2['Log Harga'] = np.log(No2['Hrg']).diff()
No2

import seaborn as sns
import pandas as pd
import numpy as np

sns.distplot(No2['Log Harga'])

"""Daily Return"""

return_daily_2 = No2.pct_change().dropna()
return_daily_2 = return_daily_2.rename({'Hrg':'Daily Return'}, axis=1)
return_daily_2 = return_daily_2[["Daily Return"]]
return_daily_2.head()

mean_teoritis_2 = (Miu-(((Sigma*Sigma)/2)))*T_2
print("Mean Teoritis:", mean_teoritis_2)

u_log2 = No2['Log Harga'].mean()
print("Mean Empirik (log harga saham):", u_log2)

var_teoritis_2 = (Sigma*Sigma)*T_2
print("Var Teoritis:", var_teoritis_2)

var_log2 = No2['Log Harga'].var()
print("Var Empirik (log harga saham):", var_log2)

drift_2 = u_log2 - (0.5 * var_teoritis_2)
drift_2

stdev_2 = return_daily_2.std()
stdev_2

stdev_log2 = No2['Log Harga'].std()
stdev_log2

"""## 2a"""

iteration_2 = 10000

return_daily_2a = np.exp(-0.011014449001207122 + 0.009508 * norm.ppf(np.random.rand(n_2,iteration_2)))
return_daily_2a = np.array(return_daily_2a)
return_daily_2a

S2 = data2.iloc[-1]
S2

price_list_2 = np.zeros_like(return_daily_2a)
price_list_2 = np.array(price_list_2)
price_list_2

price_list_2[0] = S_2
price_list_2

for t_2 in range(1, n_2):
    price_list_2[t_2] = price_list_2[t_2 - 1] * return_daily_2a[t_2]

price_list_2

plt.figure(figsize=(10,6))
plt.plot(price_list_2)
plt.title("10000 Kemungkinan Pergerakan Harga Saham", fontsize = 15)
plt.ylabel("Harga Saham", fontsize = 10)
plt.xlabel("Waktu", fontsize = 10)
plt.show()

"""# No 3"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
# %matplotlib inline

data = pd.read_csv("SIDO.JK.csv")
data = data[["Date","Adj Close"]]
SIDO = data.set_index('Date')
SIDO.head()

SIDO.tail()

"""## 3a"""

SIDO.plot(figsize = (12,4))
hrg_shm_thdp_wkt = plt.show()

"""## 3b

### Daily Return
"""

return_daily = SIDO.pct_change().dropna()
return_daily = return_daily.rename({'Adj Close':'Return Daily'}, axis=1)
return_daily.head()

return_daily.plot(figsize = (12,4))
plt.show()

"""### Daily Log Return"""

SIDO['Log Return'] = np.log(SIDO['Adj Close']).diff()
SIDO

SIDO['Log Return'].plot(figsize = (12,4))
hrg_shm_thdp_wkt_graph = plt.show()

"""## 3c

Gambar Histogram Daily Log Return
"""

import seaborn as sns
import pandas as pd
import numpy as np

sns.distplot(SIDO['Log Return'])

hrg_shm_thdp_wkt_hist = plt.hist(SIDO['Log Return'])