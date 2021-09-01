from django.shortcuts import redirect
from django.shortcuts import render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('store:store_page')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_groups(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'store/not_authorized.html')
        return wrapper_func
    return decorator

