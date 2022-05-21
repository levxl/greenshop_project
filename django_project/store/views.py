from django.shortcuts import render, redirect
from .models import Flowers, Category
from django.views.generic.base import View
from django.views.generic import ListView


class CategoryFilter:
    def get_category(self):
        return Category.objects.all()


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

class FlowersView(ListView):
    model = Flowers
    queryset = Flowers.objects.all()

class AddReview(View):
    def post(self, request, pk):
        print(request.POST)
        return redirect("/")




