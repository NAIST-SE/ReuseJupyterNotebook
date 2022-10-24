# Check dept counts
sales_ca1.groupby(sales_ca1.index.str[:-6]).size()
