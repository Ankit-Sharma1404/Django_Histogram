from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import pandas as pd
import os
import seaborn as sb

class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context=None)

class LinksPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'links.html', context=None)

class Population(TemplateView):
    def getDelhiPopu(request):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'DelhiPopulationData.csv')
        df = pd.read_csv(file_path)
        gr = sb.factorplot(x='Year', hue='Population', data=df, col='Growth Rate', kind='count')
        response = HttpResponse(content_type="image/jpeg")
        gr.savefig(response, format="png")
        return response


