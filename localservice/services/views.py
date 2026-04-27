from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ServiceRequest
from .forms import ServiceRequestForm
from accounts.models import Profile

def get_profile(user):
    try:
        return user.profile
    except Profile.DoesNotExist:
        return None

@login_required
def dashboard(request):
    profile = get_profile(request.user)
    if not profile:
        messages.error(request, "Profile not found. Please contact support.")
        return redirect('/accounts/logout/')
    if profile.role == 'worker':
        return redirect('worker_dashboard')
    return redirect('user_dashboard')

@login_required
def user_dashboard(request):
    profile = get_profile(request.user)
    if not profile or profile.role != 'user':
        return redirect('worker_dashboard')
    status_filter = request.GET.get('status', '')
    requests_qs = ServiceRequest.objects.filter(user=request.user)
    if status_filter:
        requests_qs = requests_qs.filter(status=status_filter)
    form = ServiceRequestForm()
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.save()
            messages.success(request, "Service request submitted!")
            return redirect('user_dashboard')
    return render(request, 'services/user_dashboard.html', {
        'form': form,
        'requests': requests_qs,
        'status_filter': status_filter,
        'profile': profile,
    })

@login_required
def worker_dashboard(request):
    profile = get_profile(request.user)
    if not profile or profile.role != 'worker':
        return redirect('user_dashboard')
    pending = ServiceRequest.objects.filter(status='Pending')
    my_jobs = ServiceRequest.objects.filter(worker=request.user, status='Accepted')
    completed = ServiceRequest.objects.filter(worker=request.user, status='Completed')
    return render(request, 'services/worker_dashboard.html', {
        'pending': pending,
        'my_jobs': my_jobs,
        'completed': completed,
        'profile': profile,
    })

@login_required
def accept_request(request, pk):
    profile = get_profile(request.user)
    if not profile or profile.role != 'worker':
        return redirect('/')
    req = get_object_or_404(ServiceRequest, pk=pk, status='Pending')
    req.status = 'Accepted'
    req.worker = request.user
    req.save()
    messages.success(request, "Request accepted!")
    return redirect('worker_dashboard')

@login_required
def reject_request(request, pk):
    profile = get_profile(request.user)
    if not profile or profile.role != 'worker':
        return redirect('/')
    req = get_object_or_404(ServiceRequest, pk=pk, status='Pending')
    req.status = 'Rejected'
    req.save()
    messages.info(request, "Request rejected.")
    return redirect('worker_dashboard')

@login_required
def complete_request(request, pk):
    profile = get_profile(request.user)
    if not profile or profile.role != 'worker':
        return redirect('/')
    req = get_object_or_404(ServiceRequest, pk=pk, worker=request.user, status='Accepted')
    req.status = 'Completed'
    req.save()
    messages.success(request, "Job marked as completed!")
    return redirect('worker_dashboard')
