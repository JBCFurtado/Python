L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
l0 = [2009, 2001, 2003, 1986, 1990, 1983, 1980, 1979, 1950, 2005]
l1 = ['Paulão', 'Pablo Vitar', 'Jojo Todinho', 'Surfistinha', 'Mia Khalifa',\
      'Just Bieber', 'Lula', 'Jatene', 'Dilma', 'Annita']
l4 = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre',\
      'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']

def zodiaco ():
    return(l0[i] % 12 == L[j])
for i in range(10):
        for j in range(12):
            if zodiaco():
                print('{0} = {1}'. format(l1[i], l4[j]))