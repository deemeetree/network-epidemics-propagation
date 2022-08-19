from epidemix.equations import SI, SIS, SIR, SIRV

import numpy as np
import networkx as nx

from epidemix.epidemic import EpiModel
from plot import draw_probs

days = np.arange(0, 10, 0.1)

num_node = 50
# G = nx.watts_strogatz_graph(num_node, 5, 0.4)     # Small world
# G = nx.powerlaw_cluster_graph(num_node, 5, 0.4)   # Power law
G = nx.gnp_random_graph(num_node, 0.08)             # Random

epi = EpiModel(G, SIR, num_state=3, params=[4, 2, 0.4, 0.2])

s, i, r = epi.simulate(days)

epi.set_propagate(0, 1, neighbor=1, update_state=False)
epi.set_propagate(1, 2, neighbor=None, update_state=False)
status, _ = epi.propagation()

epi.visualize(status, np.arange(16), figsize=(15, 15), n_row=4, n_col=4)
