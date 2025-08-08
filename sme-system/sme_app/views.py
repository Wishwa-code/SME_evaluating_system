from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Daily_amounts, Employee, Styles
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

            return JsonResponse({"message": "Daily amount added successfully"}, status=201)

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