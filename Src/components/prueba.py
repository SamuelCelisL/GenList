import os

# Construye la ruta base del proyecto
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base_dir = os.path.join(project_dir, 'src')

# Construye las rutas a los archivos de la base de datos
BasedeDatos = os.path.join(base_dir, 'DataBase', 'BaseDeDatos.db')
BasedeSQL = os.path.join(base_dir, 'DataBase', 'BaseDeDatos.sql')

print('basededatos',BasedeDatos)
print('basedesql',BasedeSQL)
print('base_dir',base_dir)