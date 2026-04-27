from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from services.models import ServiceRequest
from accounts.models import Profile

@staff_member_required
def admin_dashboard(request):
    all_requests = ServiceRequest.objects.select_related('user', 'worker').all()
    users = Profile.objects.filter(role='user').select_related('user')
    workers = Profile.objects.filter(role='worker').select_related('user')
    stats = {
        'total': all_requests.count(),
        'pending': all_requests.filter(status='Pending').count(),
        'accepted': all_requests.filter(status='Accepted').count(),
        'completed': all_requests.filter(status='Completed').count(),
        'rejected': all_requests.filter(status='Rejected').count(),
        'users': users.count(),
        'workers': workers.count(),
    }
    return render(request, 'adminpanel/dashboard.html', {
        'all_requests': all_requests,
        'users': users,
        'workers': workers,
        'stats': stats,
    })

@staff_member_required
def delete_request(request, pk):
    req = get_object_or_404(ServiceRequest, pk=pk)
    req.delete()
    return redirect('admin_dashboard')
