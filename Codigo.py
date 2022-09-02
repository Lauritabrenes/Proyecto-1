# Proyecto-1
# Proyecto Diseño Logico
#Hola a todos

def buscar(a):#Permite la busqueda de los binarios de minterminos con su comparación de bits
    gaps = a.count('-')
    if gaps == 0:
        return [str(int(a,2))]
    x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
    temp = []
    for i in range(pow(2,gaps)):
        temp2,ind = a[:],-1
        for j in x[0]:
            if ind != -1:
                ind = ind+temp2[ind+1:].find('-')+1
            else:
                ind = temp2[ind+1:].find('-')
            temp2 = temp2[:ind]+j+temp2[ind+1:]
        temp.append(str(int(temp2,2)))
        x.pop(0)
    return temp

def comparar(a,b):#Comparación de bit en binarios de los minterminos
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            indice = i
            c += 1
            if c>1:
                return (False,None)
    return (True,indice)

def aplanar_lista(x):#Permite la reducción de la lista
    elementos_aplanados = []
    for i in x:
        elementos_aplanados.extend(x[i])
    return elementos_aplanados
  
mt = [int(i) for i in input("Ingrese los minterminos: ").strip().split()] #Ingreso de los minterminos y agregado
mt.sort()
largo = len(bin(mt[-1]))-2
groups,todos_p = {},set()
for min in mt:
    try:
        groups[bin(min).count('1')].append(bin(min)[2:].zfill(largo))#Permite que los minterminos agregados, sean cambiados a su forma binaria
    except KeyError:
        groups[bin(min).count('1')] = [bin(min)[2:].zfill(largo)]

print("\n\n\n\nGrupos\tMinterminos\tBinarios\n%s"%('='*50))#Permite el desarrollo de la selección de los binarios de los minterminos en grupos a según los 1's que tengan
#Ordenamiento de la matriz de los grupos de los binarios actuales
for i in sorted(groups.keys()):
    print("%5d:"%i)
    for j in groups[i]:
        print("\t\t%-20d%s"%(int(j,2),j)) 
    print('-'*50)

while True:
    tmp = groups.copy()#Se realiza una copia de los grupo para manejarlos al antojo
    groups,m,marcado,parar = {},0,set(),True#Realización de declaraciones de sentencias para el recorrido, comparación y condiciones de parada de las sentencias
    l = sorted(list(tmp.keys()))
    for i in range(len(l)-1):
        for j in tmp[l[i]]:
            for k in tmp[l[i+1]]:
                res = comparar(j,k)#Inicio de la comparación de los bits de los binarios para setear su cambio
                if res[0]:
                    try:
                        groups[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None 
                    except KeyError:
                        groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]] 
                    parar = False
                    marcado.add(j) 
                    marcado.add(k) 
        m += 1
    no_marcados = set(aplanar_lista(tmp)).difference(marcado)#Aquellos elementos que no tienen comparativa de bits con otro binario en la matriz
    todos = todos_p.union(no_marcados)#Implicantes primos
    print("Elementos no marcados de la tabla:",None if len(no_marcados)==0 else ', '.join(no_marcados)) 
    if parar:#Cuando los minterminos no logran tener una comparación
        print("\n\nTodos los implicantes primos: ",None if len(todos_p)==0 else ', '.join(todos_p))
        break
    print("\n\n\n\nGrupo\tMinterminos\tBinarios\n%s"%('='*50))
    for i in sorted(groups.keys()):#Se agrupan los pares y sus repectivos binarios con cambios de bit 
        print("%5d:"%i) 
        for j in groups[i]:
            print("\t\t%-24s%s"%(','.join(buscar(j)),j)) 
        print('-'*50)
