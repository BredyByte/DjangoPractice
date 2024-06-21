from django.shortcuts import redirect
from django.urls import reverse

def redirect_authenticated_user(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('user:profile'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func
