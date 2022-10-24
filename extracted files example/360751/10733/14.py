def score_it(path):
    path_df = cities.reindex(path).reset_index()
    path_df['step'] = np.sqrt((path_df.X - path_df.X.shift())**2 + (path_df.Y - path_df.Y.shift())**2)
    path_df['step_adj'] = np.where((path_df.index) % 10 != 0, path_df.step, path_df.step + 
                            path_df.step*0.1*(~path_df.CityId.shift().isin(pnums)))
    return path_df.step_adj.sum()

display(score_it(path))

sub = pd.read_csv('../input/sample_submission.csv')
sub['Path'] = path
sub.to_csv('submission.csv', index=False)
sub.head()
