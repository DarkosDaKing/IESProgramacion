curso = {'alumnos': ['Juan', 'Franco', 'Javier'], 
         'materias': ['matematica', 'fisica', 'quimica', 'historia', 'lengua']}

listaDeMaterias = curso['materias'].copy()
listaDeMateriasNoAprobadas = []

for m in listaDeMaterias:
    nota = int(input('Que nota te sacaste en ' + m + ' ?'))
    if nota > 6:
        listaDeMateriasNoAprobadas.append(m)
    
print(listaDeMateriasNoAprobadas)  