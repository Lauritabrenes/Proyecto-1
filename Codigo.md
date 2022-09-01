# Proyecto-1
Proyecto Diseño Logico


j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None 
                    except KeyError:
                        groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]] 
                    parar = False
                    marcado.add(j) 
                    marcado.add(k) 
        m += 1
    no_marcados = set(aplanar_lista(tmp)).difference(marcado) 
    todos = todos_p.union(no_marcados) 
    print("Elementos no marcados de la tabla:",None if len(no_marcados)==0 else ', '.join(no_marcados))
    if parar: 
        print("\n\nTodos los implicantes principales: ",None if len(todos_p)==0 else ', '.join(todos_p))
        bre
    print("\n\n\n\nGroup No.\tMinterminos\tBinarios\n%s"%('='*50)) #Rayitas para dividir la tabla
    for i in sorted(groups.keys()):
        print("%5d:"%i) #Se imprime lso nuemros de los grupos
        for j in groups[i]:
            print("\t\t%-24s%s"%(','.join(buscar(j)),j)) #Se imprime los minterminos en terminos binarios
        print('-'*50) #Rayitas para dividir la tabla


