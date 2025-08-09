from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Daily_amounts, Employee, Styles
from django.contrib import messages
import json

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




# @login_required can be added if you have a user authentication system
# @csrf_exempt is used here to allow POST requests without a CSRF token.
# You should use this with caution. For authenticated users, using a
# proper CSRF token is highly recommended.

@csrf_exempt
def handle_daily_amounts(request):
    """
    Handles POST requests to add a new Daily_amounts record and GET requests
    to retrieve paginated daily amounts.
    """
    if request.method == 'POST':
        # Handles adding a new daily amount record from a POST request
        try:
            employee_id = request.POST.get('employee')
            style_id = request.POST.get('style')
            output = request.POST.get('output')

            # Ensure all required fields are present
            if not all([employee_id, style_id, output]):
                return JsonResponse({"error": "Missing one or more required fields: employee, style, output."}, status=400)
            
            # Retrieve the employee and style instances
            employee = Employee.objects.get(id=employee_id)
            style = Styles.objects.get(id=style_id)

            # Create and save the new Daily_amounts record
            daily_amount = Daily_amounts(
                employee=employee,
                style=style,
                output=output
            )
            daily_amount.save()
            messages.success(request, "Daily amount added successfully! 🎉")
            # return JsonResponse({"message": "Daily amount added successfully"}, status=201)
            return redirect('handle_daily_amounts')

        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee with the given ID does not exist."}, status=404)
        except Styles.DoesNotExist:
            return JsonResponse({"error": "Style with the given ID does not exist."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == 'GET':
        # Handles retrieving a paginated list of all daily amounts
        daily_amounts_list = Daily_amounts.objects.all().order_by('-date')
        
        paginator = Paginator(daily_amounts_list, 10) # 10 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Retrieve all employees and styles to populate the form's dropdowns
        employees = Employee.objects.all()
        styles = Styles.objects.all()

        return render(request, 'daily_amounts.html', {
            'page_obj': page_obj,
            'employees': employees,
            'styles': styles,
        })

    return JsonResponse({"error": "Only POST and GET requests are supported."}, status=405)



@csrf_exempt
def handle_employees(request):
    """
    Handles POST requests to add a new Employee and GET requests
    to retrieve paginated employees.
    """
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            address = request.POST.get('address')
            employee_code = request.POST.get('employee_code')
            mobile_number = request.POST.get('mobile_number')
            efp_number = request.POST.get('efp_number')

            if not all([name, address, employee_code]):
                return JsonResponse({"error": "Missing one or more required fields."}, status=400)
            
            employee = Employee(
                name=name,
                address=address,
                employee_code=employee_code,
                mobile_number=mobile_number,
                efp_number=efp_number
            )
            employee.save()
            messages.success(request, "Employee added successfully! 👷")
            return redirect('handle_employees')
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == 'GET':
        employees_list = Employee.objects.all().order_by('name')
        
        paginator = Paginator(employees_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'employees.html', {
            'page_obj': page_obj,
        })
    
    return JsonResponse({"error": "Only POST and GET requests are supported."}, status=405)


@csrf_exempt
def handle_styles(request):
    """
    Handles POST requests to add a new Style and GET requests
    to retrieve paginated styles.
    """
    if request.method == 'POST':
        try:
            style_code = request.POST.get('style_code')
            operation = request.POST.get('operation')
            mach = request.POST.get('mach')
            smv = request.POST.get('smv')
            target = request.POST.get('target')

            if not all([style_code, operation, mach, smv, target]):
                return JsonResponse({"error": "Missing one or more required fields."}, status=400)
            
            style = Styles(
                style_code=style_code,
                operation=operation,
                mach=mach,
                smv=smv,
                target=target
            )
            style.save()
            messages.success(request, "Style added successfully! 🧵")
            return redirect('handle_styles')
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == 'GET':
        styles_list = Styles.objects.all().order_by('style_code')
        
        paginator = Paginator(styles_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'styles.html', {
            'page_obj': page_obj,
        })
    
    return JsonResponse({"error": "Only POST and GET requests are supported."}, status=405)
