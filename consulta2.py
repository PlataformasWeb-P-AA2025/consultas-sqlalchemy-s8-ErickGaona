from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from clases import Departamento, Inscripcion, Curso, Estudiante,Instructor,Tarea,Entrega

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


#Consulta 02

# 2. Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 . 
# En función de los departamentos, presentar el nombre del departamento y 
# el número de cursos que tiene cada departamento


departamentos = session.query(Departamento)\
    .join(Departamento.cursos)\
    .join(Curso.tareas)\
    .join(Tarea.entregas)\
    .filter(Entrega.calificacion <= 0.3)\
    .group_by(Departamento.id)\
    .all()
# traigo todos los departamentos que tengan entregas con calificación <= 0.3

# Mostramos los resultados
for dep in departamentos:
    # cuento manualmente cuantos cursos tiene el depa
    num_cursos = len(dep.cursos)
    print(f"Departamento: {dep.nombre}, Número de cursos: {num_cursos}")
