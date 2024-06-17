from components import conexcionBD

estudiantes = conexcionBD.obtener_estudiantes_de_una_clase(14)

print(estudiantes)