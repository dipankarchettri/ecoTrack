from django.shortcuts import render, redirect
from .forms import UserProfileForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page or another view
    else:
        form = UserProfileForm()
    
    return render(request, 'user_profile.html', {'form': form})

