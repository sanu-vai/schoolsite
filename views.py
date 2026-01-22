from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import AdmissionForm

# ================= PAGES =================
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def news(request):
    return render(request, 'main/news.html')

def admissions(request):
    return render(request, 'main/admissions.html')

def academics(request):
    return render(request, 'main/academics.html')

def student_life(request):
    return render(request, 'main/student_life.html')

def careers(request):
    return render(request, 'main/careers.html')

def contact(request):
    return render(request, 'main/contact.html')

def courses(request):
    return render(request, 'main/courses.html')

def blog(request):
    return render(request, 'main/blog.html')


# ================= APPLY NOW =================
def apply_now(request):
    current_date = timezone.now()  # Get current date and time

    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)  # handle file uploads
        if form.is_valid():
            form.save()
            return redirect('apply_success')
    else:
        form = AdmissionForm()

    return render(request, 'main/apply_now.html', {
        'form': form,
        'current_date': current_date
    })


def apply_success(request):
    """Simple success page after form submission."""
    return render(request, 'main/apply_success.html')
