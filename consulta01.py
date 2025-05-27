from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

from clases import Departamento, Inscripcion, Curso, Estudiante,Instructor,Tarea,Entrega

from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()



#Consulta 01

# 1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. 
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, calificación, 
# nombre de instructor y nombre del departamento

#clase = session.query(Departamento).join(Estudiante).\
#        filter(Departamento.nombre.like("%Arte%")).all()

entregas = session.query(Entrega)\
  .join(Tarea.curso)\
  .join(Curso.departamento)\
  .filter(Departamento.nombre.like("%Arte%")).all()
#aplique un filtro para obtener solo las entregas de cursos del departamento "Arte"

for entrega in entregas:
    print(f"Estudiante: {entrega.estudiante.nombre}, "
          f"Calificación: {entrega.calificacion}, Instructor: {entrega.tarea.curso.instructor.nombre}, "
          f"Departamento: {entrega.tarea.curso.departamento.nombre}")


# Recorremos todas las entregas obtenidas
#for entrega in entregas:
    # el nombre del estudiante que la entregó
    # la calificación recibida
    # el nombre del instructor del curso
    # y el nombre del departamento al que pertenece el curso
