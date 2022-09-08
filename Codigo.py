# Proyecto-1
# Proyecto Diseño Logico
# Hola

from fpdf import FPDF

class PDF(FPDF): #crea la clase PDF, donde el archivo s.txt para transformarse en PDF
    def texts(self,name):
        with open(name,"rb") as xy:
            txt = xy.read().decode("latin-1")
        self.set_xy(10.0,20.0)
        self.set_text_color(00.0, 00.0, 00.0)
        self.set_font("Arial", "", 12)
        self.multi_cell(0,5,txt)
        
documento = open("s.txt","w") #Se abre el archivo txt, donde se guardan las soluciones
def mul(x,y): #Toma los elementos de los arrays para multiplicar los minterminos
    res = []
    for i in x:
        if i+"'" in y or (len(i)==2 and i[0] in y):
            return []
        else:
            res.append(i)
    for i in y:
        if i not in res:
            res.append(i)
    return res

def multiplicar(x,y): #Toma los arrays y los multiplica término por termino
    res = []
    for i in x:
        for j in y:
            tmp = mul(i,j)
            res.append(tmp) if len(tmp) != 0 else None
    return res

def buscarIPE(x): #Realiza la busqueda de los Implicantes primos 
    res = []
    for i in x:
        if len(x[i]) == 1:
            res.append(x[i][0]) if x[i][0] not in res else None
    return res

def buscar_variable(x): #Busqueda de los bits 
    var_list = []
    for i in range(len(x)):
        if x[i] == '0':
            var_list.append(chr(i+65)+"'")
        elif x[i] == '1':
            var_list.append(chr(i+65))
    return var_list

def remover(_chart,terms): #Se elimina el bit que se repita
    for i in terms:
        for j in buscar(i):
            try:
                del _chart[j]
            except KeyError:
                pass
            
def buscar(a): #Permite la busqueda de los binarios de minterminos con su comparación de bits
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

def comparar(a,b): #Comparación de bit en binarios de los minterminos
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            indice = i
            c += 1
            if c>1:
                return (False,None)
    return (True,indice)

def aplanar_lista(x): #Permite la reducción de la lista
    elementos_aplanados = []
    for i in x:
        elementos_aplanados.extend(x[i])
    return elementos_aplanados


with open("problema.txt") as archivo: #Permite la apertura del archivo txt, además de leer su contenido respectivo
    contenido = archivo.read()
    
mt = [int(i) for i in contenido.strip().split(",")]#Ingreso de los minterminos y agregado (lee la separación por comas)
mt.sort()
largo = len(bin(mt[-1]))-2
groups,todos_p = {},set()
for mintermino in mt:
    try:
        groups[bin(mintermino).count('1')].append(bin(mintermino)[2:].zfill(largo))#Permite que los minterminos agregados, sean cambiados a su forma binaria
    except KeyError:
        groups[bin(mintermino).count('1')] = [bin(mintermino)[2:].zfill(largo)]

documento.write("Group No.\tMinterminos\tBinarios\n%s"%('='*30))#Permite el desarrollo de la selección de los binarios de los minterminos en grupos a según los 1's que tengan
for i in sorted(groups.keys()):#Ordenamiento de la matriz de los grupos de los binarios actuales
    documento.write("\n%5d:\n"%i)
    for j in groups[i]:
        documento.write("\t\t    %-20d%s\n"%(int(j,2),j)) 
    documento.write('-'*50)

while True:
    tmp = groups.copy()#Se realiza una copia de los grupo para manejarlos al antojo
    groups,m,marcado,parar = {},0,set(),True #Realización de declaraciones de sentencias para el recorrido, comparación y condiciones de parada de las sentencias
    l = sorted(list(tmp.keys()))
    for i in range(len(l)-1):
        for j in tmp[l[i]]:
            for k in tmp[l[i+1]]:
                res = comparar(j,k) #Inicio de la comparación de los bits de los binarios para setear su cambio 
                if res[0]:
                    try:
                        groups[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None 
                    except KeyError:
                        groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]] 
                    parar = False
                    marcado.add(j) 
                    marcado.add(k) 
        m += 1
    no_marcados = set(aplanar_lista(tmp)).difference(marcado) #Aquellos elementos que no tienen comparativa de bits con otro binario en la matriz
    todos_p = todos_p.union(no_marcados) #Implicantes primos
    documento.write("\nElementos no marcados de la tabla:")
    if len(no_marcados)==0:
        documento.write("None\n")
    else:
        documento.write(', '.join(no_marcados))
    if parar: #Cuando los minterminos no logran tener una comparación
        documento.write("\n\nTodos los implicantes principales: ")
        if len(todos_p)==0:
             documento.write("None\n")
        else:
            documento.write(', '.join(todos_p))
        break 
    documento.write("\n\n\n\nGroup No.\tMinterminos\tBinarios\n%s"%('='*30))
    for i in sorted(groups.keys()): #Se agrupan los pares y sus repectivos binarios con cambios de bit
        documento.write("\n%5d:\n"%i) 
        for j in groups[i]:
            documento.write("\t\t%-24s%s\n"%(','.join(buscar(j)),j)) #Se imprime los minterminos en terminos binarios
        documento.write('-'*50)
        
sz = len(str(mt[-1])) #Contador para poder imprimir los implicantes principales
chart = {}
documento.write('\n\n\nCuadro de implicantes principales:\n\nMinterminos |%s\n%s'%('  '.join(('  '*(sz-len(str(i))))+str(i) for i in mt),'='*(len(mt)*(sz+1)+10)))
for i in todos_p:
    merged_minterms,y = buscar(i),0
    documento.write("\n%-16s|"%','.join(merged_minterms))
    cd= str(mt[0])
    for j in merged_minterms:
        x = mt.index(int(j))*(sz+1)
        documento.write('  '*abs(x-y)+'  '*(sz-1)+'X')
        y = x+sz
        try:
            chart[j].append(i) if i not in chart[j] else None 
        except KeyError:
            chart[j] = [i]
    documento.write('\n'+'-'*(len(mt)*(sz+1)+28))

IPE = buscarIPE(chart) #Busqueda de los implicantes principales esenciales
documento.write("\nImplicantes principales esenciales: "+', '.join(str(i) for i in IPE))
remover(chart,IPE)

if(len(chart) == 0): #Nos permite dar la resolución por una ecuación booleana
    final_result = [buscar_variable(i) for i in IPE] 
else: 
    P = [[buscar_variable(j) for j in chart[i]] for i in chart]
    while len(P)>1:
        P[1] = multiplicar(P[0],P[1])
        P.pop(0)
    final_result = [min(P[0],key=len)] 
    final_result.extend(buscar_variable(i) for i in IPE) 
documento.write('\n\nSolucion: F = '+' + '.join(''.join(i) for i in final_result))

documento.close() #Se cierra el archivo 
pdf = PDF()
pdf.add_page()
pdf.texts("s.txt") #Se tanscribe el archivo s.txt a un PDF
pdf.output("solucion.pdf", "f") #Crea el archivo PDF final



