# Identify the batches with drift
drift_batches = tt.query('drift')['sbatch'].unique()
print(drift_batches)
