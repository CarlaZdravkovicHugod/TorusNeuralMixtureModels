import sys
sys.path.insert(0, '.')

from src.toolbox import load_sample_data, TorusGraph, NCE, sample_syndata_torusgraph

import os
import time
import numpy as np
import torch
import matplotlib.pyplot as plt
import concurrent.futures
import os
from tqdm import tqdm
import time


if __name__ == "__main__":

    # os.environ['DISABLE_TQDM'] = 'True'
    start_time = time.time()

    N = 1000 # samples
    nodes = 3
    K = 3 # single model
    cv_runs = 10
    nce_steps = 5000

    data, true_vals = load_sample_data()
    data = torch.from_numpy(data).float()

    estimation_method = NCE(
        nodes = data.shape[1], 
        K = K, 
        lr = 0.1, 
        steps = nce_steps, 
        return_log_prop_data = True)

    torus_graph = TorusGraph(
        nodes = data.shape[1], 
        samples = data.shape[0], 
        data = data, 
        nModels = K, 
        estimationMethod = estimation_method, 
        true_vals = true_vals)

    torus_graph.visualize()