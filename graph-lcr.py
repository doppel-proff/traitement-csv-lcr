"""
Created on Dec 23rd 2025
author : URSET Matthias
"""

#Import
from utils import graph_utils as gu
from utils import list_utils as lu
from utils import files_utils as fu
import os

Path=os.getcwd()

#Opening measurement files
L=fu.open_csv("mesures\\GSEM slow sweep 80.CSV")

#Creating vectors for Impedance and phase
M=[]
for i in range(len(L[0])):
    M.append([])
    for j in range(len(L)):
        M[i].append(L[j][i])

Vz = M[1]
Vtheta = M[2]

#Création d'un vecteur step
Vstep = []
for i in range(len(L)):
    Vstep.append(i)

if len(Vstep) != len(Vz):
    print("Vecteurs de cardinaux différents")

if len(Vstep) != len(Vtheta):
    print("Vecteurs de cardinaux différents")

Mg=[[Vstep,Vz],[Vstep,Vtheta]]
Repo = "Impedances graphs"
Fig_name=["Impedance evolution slow sweep 80°C","Phase evolution slow sweep 80°C"]
Y_Axe=["Impedance in Ohms","Phase in rad"]
X_Axe=["step","step"]

gu.multigraph(Mg,Path,Repo,Fig_name,Y_Axe,X_Axe)
print("Programme execute")