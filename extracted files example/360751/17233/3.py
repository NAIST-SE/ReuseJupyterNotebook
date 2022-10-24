fixed_costs = [500, 0, 50, 50, 100, 200, 200, 300, 300, 400, 500]
variable_costs = [434, 0, 0, 9, 9, 9, 18, 18, 36, 36, 235]

cost_matrix = np.zeros((5000, 101))
for i in range(5000):
    for j in range(101):
        choice = pref_matrix[i, j]
        cost = fixed_costs[choice] + variable_costs[choice]*fam_sizes[i]
        cost_matrix[i,j] = cost
        
