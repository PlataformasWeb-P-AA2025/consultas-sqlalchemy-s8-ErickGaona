from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from clases import Departamento, Inscripcion, Curso, Estudiante,Instructor,Tarea,Entrega
from config import cadena_base_datos

# Crear conexión con la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 5.1 obtener todos los cursos
cursos = session.query(Curso).all()

# 5.2 Iterar sobre cada curso para obtener el promedio de calificaciones de sus entregas
for curso in cursos:
    # obtener el promedio de calificaciones de las entregas del curso actual
    promedio = session.query(func.avg(Entrega.calificacion))\
        .join(Entrega.tarea)\
        .filter(Tarea.curso_id == curso.id)\
        .scalar()  # scalar() devuelve un solo valor

    # Mostrar el resultado
    print(f"Curso: {curso.titulo}, Promedio de calificaciones: {promedio}")
