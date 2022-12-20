from django.shortcuts import render,redirect,reverse
#from django.views.generic import TemplateView
from django.views import generic
from .models import Supplier
from .forms import SupplierModelForm,CustomUserCreationForm

# Create your views here.
class SignupView(generic.CreateView):
    template_name="registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"  
 

class SuppliersListView(generic.ListView):
    template_name="suppliers/suppliers_list.html"
    context_object_name='suppliers'
    queryset=Supplier.objects.all()

class SuppliersDetailView(generic.DetailView):
    template_name="suppliers/suppliers_detail.html"
    queryset=Supplier.objects.all()
    context_object_name='suppliers'

class SuppliersCreateView(generic.CreateView):
    template_name="suppliers/suppliers_create.html"
    form_class = SupplierModelForm

    def get_success_url(self):
        return reverse("suppliers:suppliers-list")

class SuppliersUpdateView(generic.UpdateView):
    template_name="suppliers/suppliers_update.html"
    queryset=Supplier.objects.all()
    form_class = SupplierModelForm

    def get_success_url(self):
        return reverse("suppliers:suppliers-list")


class SuppliersDeleteView(generic.DeleteView):
    template_name="suppliers/suppliers_delete.html"
    queryset=Supplier.objects.all()

    def get_success_url(self):
        return reverse("suppliers:suppliers-list") 