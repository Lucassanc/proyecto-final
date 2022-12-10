from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Pacientes, Operarios
from ejemplo.forms import Buscar, FamiliarForm, PacientesForm, OperariosForm
from django.views import View

def index(request):
    return render(request, "ejemplo/saludar.html")


def saludar_a(request, nombre):
    return render(request, 
    'ejemplo/saludar_a.html',
    {"nombre": nombre}
    )


def sumar(request, a, b):
    return render (request,
    'ejemplo/sumar.html', 
    {"a": a,
     "b": b,
     "resultado": a + b
    }
    )


def buscar(request):
    lista_de_nombre = ["German", "Daniel", "Romero", "Alvaro"]
    query = request.GET['q']
    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_de_resultado]
    else:
        resultado = "no hay match"
    return render(request, 'ejemplo/buscar.html', {"resultado": resultado})

def mostrar_pacientes(request):
    lista_pacientes = Pacientes.objects.all()
    return render(request, "ejemplo/pacientes.html", {"lista_pacientes": lista_pacientes})

class BuscarPaciente(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_paciente.html'
    initial = {"nombre":""}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_pacientes = Pacientes.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'lista_pacientes':lista_pacientes})
        return render(request, self.template_name, {"form": form})

class AltaPaciente(View):
    form_class = PacientesForm
    template_name = 'ejemplo/alta_pacientes.html'
    initial = {"nombre":"", "tipo":"", "edad":"", "observaciones":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el paciente {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'msg_exito': msg_exito})
        return render(request, self.template_name, {"form": form})

def mostrar_operarios(request):
    lista_operarios = Operarios.objects.all()
    return render(request, "ejemplo/operarios.html", {"lista_operarios": lista_operarios})

class BuscarOperario(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_operario.html'
    initial = {"nombre":""}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_operarios = Operarios.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'lista_operarios':lista_operarios})
        return render(request, self.template_name, {"form": form})

class AltaOperario(View):
    form_class = OperariosForm
    template_name = 'ejemplo/alta_operario.html'
    initial = {"nombre":"", "legajo":"", "categoria":"", "observaciones":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el operario {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'msg_exito': msg_exito})
        return render(request, self.template_name, {"form": form})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})