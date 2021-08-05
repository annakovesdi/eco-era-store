from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


# display user profile
def user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succesfully updated profile')

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': user_profile,
        'on_profile_page': True
    }

    return render(request, template, context)
