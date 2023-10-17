
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import seaborn as sns

data_path1 = 'D:\\2 Code\\1FPT\ADY201m\\Project\\Project ADY\\Project ADY0.csv'
data_path2 = 'D:\\2 Code\\1FPT\ADY201m\\Project\\Project ADY\\Project ADY1.csv'
data_path3 = 'D:\\2 Code\\1FPT\ADY201m\\Project\\Project ADY\\Project ADY2.csv' 
data_path4 = 'D:\\2 Code\\1FPT\ADY201m\\Project\\Project ADY\\Project ADY3.csv' 
data_path5 = 'D:\\2 Code\\1FPT\ADY201m\\Project\\Project ADY\\Project ADY4.csv'
data_path6 = 'D:\\2 Code\\1FPT\ADY201m\\Project\\Project ADY\\Project ADY5.csv'
data_path7 = 'D:\\2 Code\\1FPT\ADY201m\\Project\\Project ADY\\Project ADY6.csv'
data_path8 = 'D:\\2 Code\\1FPT\ADY201m\\Project\\Project ADY\\Project ADY7.csv'
data_path9 = 'D:\\2 Code\\1FPT\ADY201m\\Project\\Project ADY\\Project ADY8 copy.csv'

data1 = pd.read_csv(data_path1)
data2 = pd.read_csv(data_path2)
data3 = pd.read_csv(data_path3)
data4 = pd.read_csv(data_path4)
data5 = pd.read_csv(data_path5)
data6 = pd.read_csv(data_path6)
data7 = pd.read_csv(data_path7)
data8 = pd.read_csv(data_path8)
data9 = pd.read_csv(data_path9)

data1_numeric = data1.drop('Unnamed: 0', axis=1)
data2_numeric = data2.drop('Unnamed: 0', axis=1)
data3_numeric = data3.drop('Unnamed: 0', axis=1)
data4_numeric = data4.drop('Unnamed: 0', axis=1)
data5_numeric = data5.drop('Unnamed: 0', axis=1)
data6_numeric = data6.drop('Unnamed: 0', axis=1)
data7_numeric = data7.drop('Unnamed: 0', axis=1)
data8_numeric = data8.drop('Unnamed: 0', axis=1)
data9_numeric = data9.drop('Unnamed: 0', axis=1)

data1_numeric = data1_numeric.iloc[0]
data2_numeric = data2_numeric.iloc[0] 
data3_numeric = data3_numeric.iloc[0]
data4_numeric = data4_numeric.iloc[0]
data5_numeric = data5_numeric.iloc[0]
data6_numeric = data6_numeric.loc[0]
data7_1_numeric = data7_numeric.loc[0]
data7_2_numeric = data7_numeric.loc[1]
data7_3_numeric = data7_numeric.loc[2]
data7_4_numeric = data7_numeric.loc[3]
data7_5_numeric = data7_numeric.loc[4]
data8_1_numeric = data8_numeric.loc[0]
data8_2_numeric = data8_numeric.loc[1]
data8_3_numeric = data8_numeric.loc[2]
data8_4_numeric = data8_numeric.loc[3]
data9_numeric = data9_numeric.loc[0]

data_frame = pd.concat([data1_numeric, data2_numeric, data3_numeric, data4_numeric, data5_numeric, data6_numeric,
                        data7_1_numeric, data7_2_numeric, data7_3_numeric, data7_4_numeric, data7_5_numeric,
                         data8_1_numeric, data8_2_numeric, data8_3_numeric, data8_4_numeric, data9_numeric
                         ], axis=1)
correlation_data = data_frame.corr()
fig,ax1= plt.subplots(figsize=(15,15))

sns.heatmap(correlation_data,cmap=sns.diverging_palette(50, 500, n=500),fmt='.2f',square=True, vmax=1,vmin=-1,center=0,annot=True, ax=ax1,
            xticklabels=[1,2,3,4,5,6,"GDP",7.2,7.3,7.4,7.5,8.1,8.2,8.3,8.4,9],
             yticklabels=[1,2,3,4,5,6,"GDP",7.2,7.3,7.4,7.5,8.1,8.2,8.3,8.4,9]
             )

# x = np.array([data2_numeric])
# y = np.array([data7_1_numeric])[:,2:]
# plt.scatter(x,y)
# plt.xlabel("Chỉ số giá sản xuất dịch vụ")
# plt.ylabel("GDP")
# x = np.array([data6_numeric])
# y = np.array([data7_1_numeric])
# plt.scatter(x,y)
# plt.xlabel("Lực lượng lao động")
# plt.ylabel("GDP")
plt.show()
# plt.close('q')
