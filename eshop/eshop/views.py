from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
import sys
sys.path.append(".")
from apps.userprofiles.models import OneTimeToken

# def index(request):
#     template = loader.get_template('main.html')
#     auth_form = AuthenticationForm()
#     create_new_user_form = UserCreationForm()
#     context = {
#         'create_new_user_form': create_new_user_form,
#         'auth_form': auth_form,
#     }
#     if request.method == 'GET':
#         return HttpResponse(template.render(context, request))
#     else:
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             request_context = RequestContext(request)
#             return HttpResponse(template.render(request_context.push(context), request))
#         else:
#             return HttpResponse('No such a user exists', request)

def index(request):
    template = loader.get_template('main.html')
    auth_form = AuthenticationForm()
    create_new_user_form = UserCreationForm()
    context = {
        'create_new_user_form': create_new_user_form,
        'auth_form': auth_form,
    }

    return HttpResponse(template.render(context, request))


def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return HttpResponseRedirect('/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def activate(request):
    template = loader.get_template('activate.html')
    token = request.GET.get('token')
    context = {}
    if token:
        try:
            token_item = OneTimeToken.objects.get(pk=token)
        except:
            context['response'] = 'No such an activation token exists! Please sign up again.'
        else:
            user = User.objects.get(pk=token_item.user.id)
            if token_item.date_of_expiry > timezone.now().date():
                user.is_active = True
                user.save()
                token_item.delete()
                context['response'] = 'Your account has been activated successfully!'
            else:
                token.delete()
                user.delete()
                context['response'] = 'This token is expired. Please sign up again.'
    else:
        context['response'] = 'The query string is not valid'

    return HttpResponse(template.render(context, request))
