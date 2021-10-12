from django.shortcuts import render

from .apps import SentimentanalyzerConfig
from django.http import JsonResponse
from rest_framework.views import APIView

class implement_model(APIView):
    def get(self,request):
        if request.method =='GET':
            text=request.GET.get('text')

              vector=SentimentanalyzerConfig.cv.transform([text])
            prediction=SentimentanalyzerConfig.mn.predict(vector)[0]
            response={'text_sentiment':prediction}
            return JsonResponse(response)
# Create your views here.
