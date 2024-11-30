import os
import numpy as np
from sklearn import svm
import pickle
import tempfile
import sys

def train_model():
    # Crear una carpeta temporal en lugar de usar la estructura empaquetada
    with tempfile.TemporaryDirectory() as temp_dir:
        dataPath = os.path.join(temp_dir, 'Data')
        os.makedirs(dataPath, exist_ok=True)
        
        # Crear y usar la carpeta 'Data' temporal
        # Copia o genera los archivos necesarios aquí
        # Ejemplo de estructura simulada:
        # os.makedirs(os.path.join(dataPath, 'persona1'))
        # ...cargar o copiar datos necesarios...
        
        peopleList = os.listdir(dataPath)
        labels = []
        facesData = []
        label = 0

        for nameDir in peopleList:
            personPath = os.path.join(dataPath, nameDir)
            for fileName in os.listdir(personPath):
                labels.append(label)
                vec = np.load(os.path.join(personPath, fileName))
                facesData.append(vec.flatten())
            label += 1

        clf = svm.SVC(gamma='scale', probability=True)
        clf.fit(facesData, np.array(labels))

        # Guardar el modelo en la misma carpeta que el ejecutable
        base_dir = os.path.dirname(os.path.realpath(sys.executable if getattr(sys, 'frozen', False) else __file__))
        modelPath = os.path.join(base_dir, 'Models', 'ModeloFaceFrontalData2024.pkl')
        
        os.makedirs(os.path.dirname(modelPath), exist_ok=True)
        with open(modelPath, 'wb') as f:
            pickle.dump(clf, f)
