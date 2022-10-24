# Install rapids component, cuDF
# Takes a few minutes...
! conda update --force-reinstall conda -y

!conda install -c nvidia -c rapidsai -c numba -c conda-forge -c defaults \
    cudf=0.7 python=3.6 cudatoolkit=10.0 -y

import cudf

# Convert existing Pandas df since it exists already
gputrain = cudf.DataFrame.from_pandas(train)
