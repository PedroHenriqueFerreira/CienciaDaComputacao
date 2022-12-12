import os
from resource import *
import random

def writeGraph(n, m, edges, f):
	f.write(str(n)+" "+str(n)+" "+str(m)+"\n")
	for v in range(n):
		for u in edges[v]:
			f.write(str(v)+" "+str(u)+"\n")

#lê os alunos
fl = open("grafo.mtx", "w")
n = int(input("Digite numero de vértices:\n"))
den = int(input("Digite densidade:\n"))
m = 0
edges = [[] for i in range(n)]

for v in range(n):
	for u in range(v+1, n):
		if(random.randint(1, 100) < den):
			m = m+1
			edges[v].append(u)
writeGraph(n,m,edges,fl)

fl.close()
