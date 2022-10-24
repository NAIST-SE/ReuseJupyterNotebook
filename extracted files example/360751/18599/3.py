import missingno as msno
msno.dendrogram(sales_ca1.replace(0, np.nan).T, method='ward')
