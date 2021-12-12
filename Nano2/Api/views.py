from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework.views import APIView
from . import bot
# Create your views here.

class apiView(APIView):

    def post(self,request):
        if request.method == 'POST':

            obj = json.load(request)
            text = obj['query']
            p= bot.query(text)
            pred = {'response':str(p)}
            return JsonResponse(pred)