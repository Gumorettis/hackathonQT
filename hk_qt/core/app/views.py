from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView

from core.app import calculator, forms


@login_required
def index(request):
    return render(request, "pages/index.html")


@login_required
def calculate(request):
    income = request.GET.get("income", request.user.client.income)
    result = calculator.calculate(income)

    return render(request, "pages/calculate.html", {"result": result, "income": income})


class CreateUserView(FormView):
    template_name = "auth/register.html"
    form_class = forms.CreateUserForm
    success_url = reverse_lazy("home")

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
