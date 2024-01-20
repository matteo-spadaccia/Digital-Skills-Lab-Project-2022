from django.shortcuts import render, get_object_or_404
from .models import Department,Course,Event
import datetime

# Create your views here.

def main(request):
    departments = Department.objects.all()

    context = {
        'departments': departments,
    }

    return render(request, 'app/main.html', context)

def department(request, pk):
    department = Department.objects.get(pk=pk)
    courses = Course.objects.filter(department=department)
    events = Event.objects.filter(department=department)

    context = {
        'department': department,
        'courses': courses,
        'events': events,
    }

    return render(request, 'app/department.html', context)

def course(request, pk):
    course = Course.objects.get(pk=pk)
    department = course.department
    
    context = {
        'course': course,
        'department': department,
    }

    return render(request, 'app/course.html', context)

def event(request, pk):
    event = Event.objects.get(pk=pk)
    department = event.department
    
    context = {
        'event': event,
        'department': department,
    }

    return render(request, 'app/event.html', context)

def courses(request):
    courses = Course.objects.all()
    departments = Department.objects.all()

    context = {
        'courses': courses,
        'departments': departments,
    }

    return render(request, 'app/courses.html', context)

def events(request):
    events = Event.objects.order_by('datetime')
    today = datetime.date.today()
    flag = False
    for event in events:
        if event.datetime.year == today.year and event.datetime.month == today.month and event.datetime.day == today.day:
            flag = True

    context = {
        'events': events,
        'today': today,
        'flag': flag
    }

    return render(request, 'app/events.html', context)