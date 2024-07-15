from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from curso_app.models import Curso, Estudiante, Profesor, Direccion


def crear_curso(request):
    if request.method == 'GET':
        return render(request, 'crear_curso.html')
    else:
        Curso.objects.create(
            codigo = request.POST['codigo'],
            nombre = request.POST['nombre'],
            version = request.POST['version'],
        )
        return HttpResponse('Curso creado correctamente')


def crear_profesor(request):
    if request.method == 'GET':
        return render(request, 'crear_profesor.html')
    else:
        Profesor.objects.create(
            rut = request.POST['rut'],
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            activo = request.POST['activo'],
            creado_por = request.POST['creado_por'],
        )
        return HttpResponse('Profesor creado correctamente')


def crear_estudiante(request):
    if request.method == 'GET':
        return render(request, 'crear_estudiante.html')
    else:
        Estudiante.objects.create(
            rut = request.POST['rut'],
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            fecha_nac = request.POST['fecha_nac'],
            activo = request.POST['activo'],
            creado_por = request.POST['creado_por'],            
        )
        return HttpResponse('El estudiante ha sido creado exitósamente')


def crear_direccion(request):
    if request.method == 'GET':
        return render(request, 'crear_direccion.html')
    elif request.method == 'POST':
        # Obtener el rut del estudiante desde el formulario
        rut_estudiante = request.POST['rut_estudiante']
        
        # Obtener la instancia del estudiante por su rut
        estudiante = get_object_or_404(Estudiante, rut=rut_estudiante)
        
        # Crear la dirección asociada al estudiante
        direccion = Direccion.objects.create(
            calle=request.POST['calle'],
            numero=request.POST['numero'],
            dpto=request.POST.get('dpto', ''),
            comuna=request.POST['comuna'],
            ciudad=request.POST['ciudad'],
            region=request.POST['region'],
            estudiante_id=estudiante  # Asignar el estudiante a la dirección
        )
        
        return HttpResponse('La dirección fue creada exitósamente')


def obtener_curso(request):
    codigo = request.POST['codigo']
    curso = Curso.objects.filter(curso = curso).first()
    return render(request,'plantilla.html', {'curso':curso})


def obtener_profesor(request):
    rut = request.POST['rut']
    profesor = Profesor.objects.filter(rut = rut).first()
    return render(request,'plantilla.html', {'profesor':profesor})


def obtener_estudiante(request):
    rut = request.POST['rut']
    estudiante = Estudiante.objects.filter(rut = rut).first()
    return render(request,'plantilla.html', {'estudiante':estudiante})



def asignar_profesor_a_curso(request):
    if request.method == 'GET':
        # Obtener todos los profesores y cursos para mostrarlos en un formulario
        profesores = Profesor.objects.all()
        cursos = Curso.objects.all()
        return render(request, 'asignar_profesor_a_curso.html', {'profesores': profesores, 'cursos': cursos})
    else:
        # Obtener el profesor y el curso desde el formulario
        profesor_rut = request.POST['profesor_rut']
        curso_codigo = request.POST['curso_codigo']
        
        # Obtener las instancias de los objetos
        profesor = get_object_or_404(Profesor, rut=profesor_rut)
        curso = get_object_or_404(Curso, codigo=curso_codigo)
        
        # Asignar el profesor al curso
        curso.profesor_id.add(profesor)
        
        return HttpResponse(f'Profesor {profesor.nombre} {profesor.apellido} asignado al curso {curso.nombre}.')




def asignar_estudiante_a_curso(request):
    if request.method == 'POST':
        # Obtener el código del curso y el RUT del estudiante desde el formulario
        curso_codigo = request.POST['curso_codigo']
        estudiante_rut = request.POST['estudiante_rut']
        
        # Obtener la instancia del curso
        curso = get_object_or_404(Curso, codigo=curso_codigo)
        
        # Obtener la instancia del estudiante
        estudiante = get_object_or_404(Estudiante, rut=estudiante_rut)
        
        # Asignar el curso al estudiante
        estudiante.curso_id = curso
        estudiante.save()
        
        return HttpResponse('Estudiante agregado al curso.')
    else:
        return render(request, 'agregar_estudiante_a_curso.html')



def imprimir_estudiantes_curso(request):
    # Obtener el código del curso
    curso_codigo = request.POST['curso_codigo']

    # Obtener la instancia del curso con el código
    curso = get_object_or_404(Curso, codigo=curso_codigo)

    # Obtener los estudiantes asignados al curso
    estudiantes = Estudiante.objects.filter(curso_id=curso)

    # Imprimir los estudiantes
    for estudiante in estudiantes:
        print(f"RUT: {estudiante.rut}")
        print(f"Nombre: {estudiante.nombre}")
        print(f"Apellido: {estudiante.apellido}")
        print("-" * 20)

    return HttpResponse('Estudiantes listados.')




