# %% Import
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import sys
# %%
## Custom Files:
ABS_PATH = "/home/jx/JXProject/Github/covidx-clubhouse" # Define ur absolute path here
def abspath(relative_path):
    return os.path.join(ABS_PATH, relative_path)

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(abspath("src_code"))

# %%
data_paths = [
    "output/CUSTOM-MODEL/v6/y_pred[best].txt",
    "output/CUSTOM-MODEL/v6/y_pred[final].txt",
    "output/CUSTOM-MODEL/v6-custom-3/y_pred[best[36:50]].txt",
    "output/CUSTOM-MODEL/v6-custom-3/y_pred[best[37:50]].txt",
    "output/CUSTOM-MODEL/v6-custom-3/y_pred[best].txt",
    "output/CUSTOM-MODEL/v6-custom-3/y_pred[final].txt"
]
data_list = [ pd.read_csv(abspath(path), sep=" ", header=None) for path in data_paths ]
# %%
from icecream import ic
ic(np.sum(np.abs(data_list[2]-data_list[3])))
ic(np.sum(np.abs(data_list[4]-data_list[3])))
ic(np.sum(np.abs(data_list[5]-data_list[3])))

ic(np.sum(np.abs(data_list[4]-data_list[2])))
ic(np.sum(np.abs(data_list[5]-data_list[2])))


# %%
