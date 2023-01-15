import pandas as pd

"""Age of patient at time of operation (numerical)"""
AGE = 30
"""Patient's year of operation (year - 1900, numerical)"""
OP_YEAR = 64
"""Number of positive axillary nodes detected (numerical)"""
AXIL_NODES = 1
"""Survival status (class attribute) 1 = the patient survived 5 years or longer 2 = the patient died within 5 year"""
SURV_STATUS = 1.1
val_list = [AGE, OP_YEAR, AXIL_NODES, SURV_STATUS]
tag_list = ["AGE", "OP_YEAR", "AXIL_NODES", "SURV_STATUS"]


def dfFromCSV(file_path):
    return pd.read_csv(file_path, header=0,
                       names=tag_list)
