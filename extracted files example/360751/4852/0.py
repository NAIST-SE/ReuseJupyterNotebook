import numpy as np
np.set_printoptions(precision=2, suppress=True)
import pandas as pd
pd.options.display.max_columns = 2000

id_cols = ['store_id', 'item_id']
sales_cols = ['d_'+str(i) for i in range(1,1914)]

sales = pd.read_csv('../input/m5-forecasting-accuracy/sales_train_validation.csv',
                    usecols=id_cols+sales_cols, index_col=id_cols) \
            .astype(np.uint16).sort_index()
sales
