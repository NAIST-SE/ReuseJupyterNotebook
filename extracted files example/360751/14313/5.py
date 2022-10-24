%%timeit
#This block is STRAIGHT UP ACCELERATED

def get_dist(df):
    return np.sqrt((df.x_1-df.x_0)**2 +
                   (df.y_1-df.y_0)**2 +
                   (df.z_1-df.z_0)**2)

gputrain['dist_rapids'] = get_dist(gputrain)
