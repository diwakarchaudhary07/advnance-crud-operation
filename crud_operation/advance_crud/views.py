from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.core.paginator import Paginator


# CREATE + READ + SEARCH + FILTER + DATE FILTER + PAGINATION

def student_list(request):

    # Search Input
    search = request.GET.get('search')

    # City Filter
    city_filter = request.GET.get('city')

    # Date Filter
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    # All Students
    students = Student.objects.all().order_by('-id')

    # Search Logic
    if search:

        students = students.filter(

            Q(name__icontains=search) |
            Q(age__icontains=search) |
            Q(email__icontains=search) |
            Q(city__icontains=search)

        )

    # City Filter
    if city_filter:

        students = students.filter(
            city__iexact=city_filter
        )

    # Date Filter
    if from_date and to_date:

        students = students.filter(
            created_at__date__range=[from_date, to_date]
        )

    # Pagination
    paginator = Paginator(students, 5)

    page_number = request.GET.get('page')

    students = paginator.get_page(page_number)

    return render(request, 'student_list.html', {
        'students': students
    })


# CREATE

def student_create(request):

    form = StudentForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('student_list')

    return render(request, 'student_form.html', {
        'form': form
    })


# UPDATE

def student_update(request, id):

    student = get_object_or_404(Student, id=id)

    form = StudentForm(
        request.POST or None,
        instance=student
    )

    if form.is_valid():

        form.save()

        return redirect('student_list')

    return render(request, 'student_form.html', {
        'form': form
    })


# DELETE

def student_delete(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('student_list')