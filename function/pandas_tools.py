import numpy as np
import pandas as pd

def cal_magnitude(pd_data):
    names = pd_data.columns
    components = list({name[-2:] for name in names})
    tags = list({int(name[:-3]) for name in names})
    components.sort()
    # create new data frame by components
    new_df_list = []
    for comp in components:
        _tags = [name for name in names if comp in name]
        new_df_list += [pd.DataFrame(pd_data, columns=_tags)]
    # new pd_data for magnitude data
    new_data = {tag: None for tag in tags}
    for tag in tags:
        _value = [pd_data[f'{tag}:{comp}'] for comp in components]
        _value = np.linalg.norm(_value, axis=0)
        new_data[tag] = _value
    new_df_list += [pd.DataFrame(new_data)]
    return new_df_list