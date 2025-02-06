Caso de Estudio: Registro de Estudiantes en un Curso en Línea
Eres el encargado de desarrollar un sistema para gestionar la inscripción de estudiantes en un curso en línea. Para ello, debes construir un diccionario que almacene información sobre los estudiantes inscritos.

Requisitos:
Estructura del Diccionario:

Cada estudiante debe estar identificado por un ID único (puede ser un número de matrícula o un UUID).
Los datos de cada estudiante deben incluir:
Nombre completo
Correo electrónico
Edad
País de residencia
Progreso en el curso (porcentaje del 0 al 100)
Calificación final (de 0 a 10, inicialmente en None hasta que termine el curso)
Estado de inscripción ("activo" o "finalizado")
Módulos completados (lista con los nombres de los módulos terminados)
Requisitos Específicos:

El diccionario debe permitir agregar nuevos estudiantes sin afectar los existentes.
El progreso debe actualizarse a medida que el estudiante avanza en el curso.
Una vez que el progreso llegue al 100%, el estado debe cambiar a "finalizado".
La calificación final solo puede asignarse si el curso está finalizado.
