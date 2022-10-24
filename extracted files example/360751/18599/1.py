# Filter items at one store 
sales_ca1 = sales.loc['CA_1'] \
                 .assign(d_median=lambda x: x.median(axis=1)) \
                 .query('d_median >= 4') \
                 .drop(columns='d_median') \
                 .iloc[:, -28*24:]  # use the last two years

sales_ca1
