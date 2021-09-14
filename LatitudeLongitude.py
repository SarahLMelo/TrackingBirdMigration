import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birdData = pd.read_csv("bird_tracking.csv") #Leia a planilha de dados
birdNames = pd.unique(birdData.bird_name) #Crie uma lista de elementos únicos com os dados da tabela

plt.figure(figsize=(10, 10)) #Cria o espaço que iremos plotar o gráfico
for name in birdNames: #Adiciona os dados dos pássaros ao gráfico, adicionando todos os de cada pássaro de uma vez
    i = birdData.bird_name == name
    x, y = birdData[i].longitude, birdData[i].latitude
    plt.plot(x, y, ".", label=name)

#Cria a legenda de cada eixo
plt.xlabel("Longitude") 
plt.ylabel("Latitude")

#Cria no canto inferior direito, a indicação de qual pássaro é
plt.legend(loc = "lower right") 

#Plota
plt.show()

