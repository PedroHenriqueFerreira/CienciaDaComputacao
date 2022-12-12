vertices = []
faces = []

def addVertice():
    idV = int(input('Id do vértice: '))
    x = int(input('X: '))
    y = int(input('Y: '))
    z = int(input('Z: '))
    
    vertices.append({ 'idV': idV, 'x': x, 'y': y, 'z': z })
    
def addFace():
    idF = int(input('Id da face: '))
    
    idV1 = int(input('Id do vértice 1: '))
    idV2 = int(input('Id do vértice 2: '))
    idV3 = int(input('Id do vértice 3: '))
    
    faces.append({ 'idF': idF, 'idV1': idV1, 'idV2': idV2, 'idV3': idV3 })
    
def listarVertices(idF):
    for face in faces:
        if face['idF'] == idF:
            for vertice in vertices:
                for i in range(1, 4):
                    if vertice['idV'] == face[f'idV{i}']:
                        print(f'idV{i}: ({vertice["x"]}, {vertice["y"]}, {vertice["z"]})')
            
            break