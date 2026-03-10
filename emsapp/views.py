from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Employee
from .forms import EmployeeForm


# ---------- simple class-based pages ----------
class HomeView(generic.TemplateView):
    template_name = "emsapp/home.html"


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "emsapp/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["total_employees"] = Employee.objects.count()
        return ctx


# ---------- employee CRUD ----------
class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    template_name = "emsapp/display.html"
    context_object_name = "employees"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset().order_by("e_id")
        q = self.request.GET.get("q", "")
        if q:
            qs = qs.filter(e_name__icontains=q) | qs.filter(
                department__icontains=q
            ) | qs.filter(e_id__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["query"] = self.request.GET.get("q", "")
        return ctx


class EmployeeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "emsapp/insert.html"
    success_url = reverse_lazy("display")

    def form_valid(self, form):
        messages.success(self.request, "Employee added successfully!")
        return super().form_valid(form)


class EmployeeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "emsapp/edit.html"
    pk_url_kwarg = "e_id"
    success_url = reverse_lazy("display")

    def form_valid(self, form):
        messages.success(self.request, "Employee updated successfully!")
        return super().form_valid(form)


class EmployeeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Employee
    context_object_name = "employee"
    template_name = "emsapp/delete.html"
    pk_url_kwarg = "e_id"
    success_url = reverse_lazy("display")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Employee deleted successfully!")
        return super().delete(request, *args, **kwargs)