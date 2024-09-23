from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib import messages
from category.models import Category
from category.forms import CategoryModelForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ["category.view_category"]
    login_url = "/authen/"
    def get(self, request: HttpRequest):
        category_qs = Category.objects.all()
        
        form_category_list = [
            CategoryModelForm(instance=category)
            for category in category_qs
        ]
        context = {
            "forms": form_category_list,
            "category_qs": category_qs
        }
        
        return render(request, "list_category.html", context)
    

class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ["category.add_category"]
    
    def post(self, request: HttpRequest):
        form = CategoryModelForm(request.POST)
        
        if form.is_valid():
            form.save()
        else:
            non_field_errors_mes = str(form.non_field_errors())
            messages.error(request, "create error {error}".format( error=non_field_errors_mes ))
            
        return redirect('category-list')
        

class CategoryEditView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ["category.change_category"]
    
    def post(self, request: HttpRequest, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryModelForm(request.POST, instance=category)
        
        if form.is_valid():
            form.save()
            
        return redirect('category-list')


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ["category.delete_category"]
    
    def get(self, request: HttpRequest, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect('category-list')
        