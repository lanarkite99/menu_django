from django.shortcuts import render
from django.views import generic
from .models import Menu,MEAL_TYPE

class MenuList(generic.ListView):
    queryset = Menu.objects.order_by()
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["meals"]= MEAL_TYPE
        return context


class MenuSubList(generic.DetailView):
    model=Menu
    template_name = "menusublist.html"
