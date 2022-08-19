import networkx as nx
import EoN
import matplotlib.pyplot as plt

N = 10**2  # number of individuals
kave = 16  # expected number of partners - more realistic - 12 for 100
print('generating graph G with {} nodes'.format(N))

G = nx.fast_gnp_random_graph(N, kave/(N-1))  # Erdo’’s-Re’nyi graph

# G = nx.watts_strogatz_graph(N, 14, 0.5)     # Small world
# G = nx.powerlaw_cluster_graph(N, 10, 0.5)   # Power law
# G = nx.newman_watts_strogatz_graph(N, 8, 1)

plt.figure(1)
nx.draw_kamada_kawai(G)


print('generated a graph with {} edges'.format(G.number_of_edges()))

rho = 0.01  # initial fraction infected
tau = 1  # transmission rate
gamma = 2  # recovery rate

print('doing Event-driven SIS simulation')
t1, S1, I1 = EoN.fast_SIS(G, tau, gamma, rho=rho, tmax=50)
print('doing Gillespie simulation')
t2, S2, I2 = EoN.Gillespie_SIS(G, tau, gamma, rho=rho, tmax=50)
print('done with simulations, now plotting')

plt.figure(2)

# plt.axis([0, 50, 70, 100])

plt.plot(t1, I1, label='fast_SIS')
plt.plot(t2, I2, label='Gillespie_SIS')
plt.xlabel('$t$')
plt.ylabel('Number infected')
plt.legend()
plt.show()
