import numpy as np
import pandas as pd
from  pandas import Series,DataFrame

pd.set_option('display.width',200)

dates=pd.date_range('20170129',periods=5)
print(dates)

df=pd.DataFrame(np.random.randn(5,5),index=dates,columns=list('ABCDE'))

print(df)