from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import StudentForm
from .models import Student
from django.views.generic import UpdateView,CreateView,DeleteView,DetailView,ListView,View,TemplateView,RedirectView

# Create your views here.
class HomeTemplate(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        form = StudentForm()
        context =  super().get_context_data(**kwargs)
        obj = Student.objects.all()
        context={
            'data':obj,
            'form':form
        }
        return context
    def post(self,request):
        data = StudentForm(request.POST)
        data.save()
        return HttpResponseRedirect("/")

class DeleteTemp(RedirectView):
    url="/"
    def get_redirect_url(self,**kwargs):
        del_id = kwargs['id']
        Student.objects.get(pk=del_id).delete()
        return super().get_redirect_url(self,**kwargs)

class UserupdateView(View):
   
    def get(self,request,id):
        data = Student.objects.get(pk=id)
        fm = StudentForm(instance=data)
        context = {
            'form':fm
        }
        return render(request,'update.html',context)
    def post(self,request,**kwargs):
        update_id = kwargs['id']
        sf  = Student.objects.get(pk=update_id)
        Stuform = StudentForm(request.POST,instance=sf)
        if Stuform.is_valid():
            Stuform.save()
        return HttpResponse("Data updated")
        


