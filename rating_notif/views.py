from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import F
from project.models import project
from .models import project_like

# Create your views here.
def like_post(request):
    beta = request.POST['element_beta']
    project_like.objects.create(project_id=beta,user_id=request.user.id)
    project.objects.filter(id=beta).update(
        likes_total=F('likes_total') + 1)
    return HttpResponse('hello')

def unlike_post(request):
    beta = request.POST['element_beta']
    project_like.objects.filter(project_id=beta, user_id=request.user.id).delete()
    project.objects.filter(id=beta).update(
        likes_total=F('likes_total') - 1)
    return HttpResponse('hello')