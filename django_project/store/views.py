from django.shortcuts import render, redirect
from .models import *
from django.views.generic.base import View
from django.views.generic import ListView


def home(request):
    return render(request, 'store/flowers_list.html')

class CategoryFilter:
    def get_category(self):
        return Category.objects.all()

class FlowersView(CategoryFilter, ListView):
    def get(self, request):
        flowers = Flowers.objects.all()
        return render(request, "store/store_doc.html", {"store_doc" : flowers})

class FlowersListView(CategoryFilter, ListView):
    model = Flowers
    queryset = Flowers.objects.all()

class FlowersDetailView(View):
    def get(self, requset, slug):
        flowersget = Flowers.objects.get(url=slug)
        flowersall = Flowers.objects.all()
        return render(requset, "store/store_detail.html", {"flowers": flowersall, 
        "flowersget": flowersget })

class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Flowers.objects.filter(title__icontains=self.request.GET.get("q"))

class AddReview(View):
    def post(self, request, pk):
        print(request.POST)
        return redirect("/")