from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse
from django.utils import timezone  
from .models import EBook, Rating, Borrowing
from .forms import RatingForm, CustomUserCreationForm, CustomAuthenticationForm

class EBookListView(ListView):
    model = EBook
    template_name = 'elibrary/ebook_list.html'
    context_object_name = 'ebooks'

class EBookDetailView(DetailView):
    model = EBook
    template_name = 'elibrary/ebook_detail.html'
    context_object_name = 'ebook'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Check if the current user has an active borrowing for this e-book
            borrowing = Borrowing.objects.filter(
                user=self.request.user,
                ebook=self.object,
                return_date__isnull=True
            ).first()
            context['active_borrowing'] = borrowing
        return context

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'elibrary/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'elibrary/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('ebook_list')

@login_required
def dashboard(request):
    borrowings = Borrowing.objects.filter(user=request.user).order_by('-borrow_date')
    return render(request, 'elibrary/dashboard.html', {'borrowings': borrowings})

@login_required
def borrow_ebook(request, pk):
    ebook = get_object_or_404(EBook, pk=pk)
    if ebook.licenses > 0:
        Borrowing.objects.create(user=request.user, ebook=ebook)
        ebook.licenses -= 1
        ebook.save()
        messages.success(request, f"'{ebook.title}' borrowed successfully! You can download it now.")
    else:
        messages.error(request, "No licenses available.")
    return redirect('ebook_detail', pk=pk)

@login_required
def download_ebook(request, pk):
    ebook = get_object_or_404(EBook, pk=pk)
    if Borrowing.objects.filter(user=request.user, ebook=ebook, return_date__isnull=True).exists():
        file_path = ebook.file.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    messages.error(request, "You haven’t borrowed this e-book or it’s been returned.")
    return redirect('ebook_detail', pk=pk)

@login_required
def return_ebook(request, pk):
    ebook = get_object_or_404(EBook, pk=pk)
    borrowing = Borrowing.objects.filter(user=request.user, ebook=ebook, return_date__isnull=True).first()
    if borrowing:
        borrowing.return_date = timezone.now()
        borrowing.save()
        ebook.licenses += 1
        ebook.save()
        messages.success(request, f"'{ebook.title}' returned successfully!")
    else:
        messages.error(request, "No active borrowing found.")
    return redirect('dashboard')

@login_required
def rate_ebook(request, pk):
    ebook = get_object_or_404(EBook, pk=pk)
    rating = Rating.objects.filter(user=request.user, ebook=ebook).first()

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.ebook = ebook
            rating.save()
            messages.success(request, f"Successfully rated '{ebook.title}'!")
            return redirect('ebook_detail', pk=pk)
    else:
        form = RatingForm(instance=rating)
    return render(request, 'elibrary/rate_ebook.html', {'form': form, 'ebook': ebook})