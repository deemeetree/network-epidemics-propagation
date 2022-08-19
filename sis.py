import networkx as nx
import EoN
import matplotlib.pyplot as plt

N = 10**5  # number of individuals
kave = 5  # expected number of partners
print('generating graph G with {} nodes'.format(N))

G = nx.fast_gnp_random_graph(N, kave/(N-1))  # Erdo’’s-Re’nyi graph

rho = 0.005  # initial fraction infected
tau = 0.3  # transmission rate
gamma = 1.0  # recovery rate

print('doing Event-driven SIS simulation')
t1, S1, I1 = EoN.fast_SIS(G, tau, gamma, rho=rho, tmax=30)
print('doing Gillespie simulation')
t2, S2, I2 = EoN.Gillespie_SIS(G, tau, gamma, rho=rho, tmax=30)
print('done with simulations, now plotting')
plt.plot(t1, I1, label='fast_SIS')
plt.plot(t2, I2, label='Gillespie_SIS')
plt.xlabel('$t$')
plt.ylabel('Number infected')
plt.legend()
plt.show()
