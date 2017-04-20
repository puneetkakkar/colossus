from django.shortcuts import render
from django.db.models import Max
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.models import User
from django.contrib import messages
from home_and_login.models import user_details
from project.models import project, file_model
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.defaultfilters import slugify
# import project from models
from .models import project, file_modal_form


@login_required(login_url='../../')
def add_project_page(request):
    if request.method == 'POST':
        form = file_modal_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            args = file_model.objects.all().aggregate(Max('id'))
            file_link = file_model.objects.filter(id=args['id__max']).values_list('file_project_link' ,flat=True)
            return HttpResponse(file_link)
        else:
            print('NO')
    user_profile_link = user_details.objects.filter(
        user_id=request.user.id).values_list('profile_link')[0][0]
    form = file_modal_form()
    return render(request, 'project/add.html', {'profile_link': user_profile_link, 'form':form})


@login_required(login_url='../../')
def add_project(request):
    project_title = request.POST['project_title']
    project_type = request.POST['project_type']
    project_desc = request.POST['project_desc']
    user_profile_link = user_details.objects.filter(
        user_id=request.user.id).values_list('profile_link')[0][0]
    slugged_link = user_profile_link + '/' + slugify(project_title)
    user_id_in_action = request.user.id
    project_save = project.objects.create(
        user_id=user_id_in_action, title=project_title, project_type=project_type, description=project_desc, project_link=slugged_link)
    return HttpResponse("Done")


def show_project(request, requested_user, requested_profile_link):
    print(requested_user)
    print(requested_profile_link)
    requested_user_id = user_details.objects.filter(
        profile_link=requested_user).values_list('user_id')[0][0]
    requested_project_link = requested_user+'/'+requested_profile_link
    print(requested_project_link)
    if requested_user_id:
        project_details = project.objects.filter(user_id=requested_user_id, project_link=requested_project_link).values_list(
            'likes_total', 'comments_total', 'shares_total', 'title', 'description')
        if project_details:
            temp_dict = {}
            temp_dict['likes_total'] = project_details[0][1]
            temp_dict['comments_total'] = project_details[0][1]
            temp_dict['shares_total'] = project_details[0][2]
            temp_dict['title'] = project_details[0][3]
            temp_dict['description'] = project_details[0][4]
            one = user_details.objects.filter(user_id=requested_user_id).values_list(
                'full_name', 'profile_link', 'photo_link')
            temp_dict['full_name'] = one[0][0]
            temp_dict['profile_link'] = one[0][1]
            temp_dict['photo_link'] = one[0][2]
            temp_dict['liked'] = 0
            return render(request, 'user_profile/project_page.html',  {'project': temp_dict})
        else:
            return HttpResponse('No project')

def start_new(request):
    return render(request, 'project/start_new.html')

def view_project(request):
    return render(request, 'project/view.html')

def view_project_stream(request, requested_stream):
    print ("this" + requested_stream)
    
    return render(request, 'project/stream_view.html', {'stream' : requested_stream,})

def generate_stream_projects(request):
    feed_posts = {}
    # all_projects = project.objects.filter(project_type=requested_stream).values_list('title', 'description', 'likes_total')
    from project.models import project
    user_project_list = project.objects.filter(project_type=request.POST['stream'])
    for project_one in user_project_list:
        temp_dict = {}
        temp_dict['likes_total'] = project_one.likes_total
        temp_dict['title'] = project_one.title
        temp_dict['comments_total'] = project_one.comments_total
        temp_dict['shares_total'] = project_one.shares_total
        temp_dict['description'] = project_one.description
        temp_dict['project_id'] = project_one.id
        one = user_details.objects.filter(user_id=project_one.user_id).values_list(
            'full_name', 'profile_link', 'photo_link')
        temp_dict['full_name'] = one[0][0]
        temp_dict['profile_link'] = one[0][1]
        temp_dict['photo_link'] = one[0][2]
        feed_posts['post: ' + str(project_one.id)] = temp_dict
    return JsonResponse(feed_posts)