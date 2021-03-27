# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:27:08 2021

@author: LENOVO
"""

import networkx as nx
import matplotlib.pyplot as plt

map_city = nx.Graph()                                                    #C1

import pandas as pd
df = pd.read_csv('vertices.csv', sep=",", keep_default_na=True)          #C2
print(df)                                                                #C3
print(df["ID"])                                                          #C4

df2 = pd.read_csv('arcos.csv', sep=",", keep_default_na=True)            #C5
print(df2)                                                               #C6
print(df2["ID_origen"])                                                  #C7

for i in range(len(df["ID"])):                                           #C8*n , where n is the number of vertices
    map_city.add_node(df['ID'].values[i])                                #C9
    
for j in range(len(df2)):                                                #C10*m , where m is the number of arcos
    map_city.add_edge(df2['ID_origen'].values[j], df2['ID_destino'].values[j])  #C11
    map_city[df2['ID_origen'].values[j]][df2['ID_destino'].values[j]]["weight"] = df2['distancia'].values[j]   #C12


nx.draw_shell(map_city, node_color = "blue", edge_color = "grey", font_size = 10, width = 2, with_labels = True, node_size = 350, arrows = True, arrowsize = 20)
plt.show()
