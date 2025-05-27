from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from clases import Departamento, Inscripcion, Curso, Estudiante,Instructor,Tarea,Entrega

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
#Consulta 03

#   Obtener todas las tareas asignadas a los siguientes estudiantes 

#    Jennifer Bolton 
#    Elaine Perez
#    Heather Henderson
#    Charles Harris

#    En función de cada tarea, presentar el número de entregas que tiene

from sqlalchemy import func

# Consulta: Obtener tareas asignadas a ciertos estudiantes y cuántas entregas tiene cada una
tareas = session.query(Tarea)\
    .join(Entrega.estudiante)\
    .filter(Estudiante.nombre.in_([             
         "Jennifer Bolton", 
        "Elaine Perez", 
        "Heather Henderson", 
        "Charles Harris"
 ])).group_by(Tarea.id).all()
#agrupamos las tareas por id 

for tarea in tareas:
    num_entregas = len(tarea.entregas)  # Contamos cuántas entregas tiene esa tarea
    print(f"Tarea: {tarea.titulo}, Número de entregas: {num_entregas}")

