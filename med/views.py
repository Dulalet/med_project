from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from  rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from med.models import Appointment
from med.serializers import AppointmentSerializer
from users.models import MedicalWorker, Department
from users.serializers import CustomUserSerializer, MedicalWorkerSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def profile(request):
    serializeduser = CustomUserSerializer(request.user)
    response = {'user': serializeduser.data}
    if request.user.category == 'med_worker':
        med_worker = MedicalWorker.objects.get(user=request.user)
        med_worker_data = MedicalWorkerSerializer(med_worker)
        response['med_worker'] = med_worker_data.data
    return Response(response, HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def doctors_by_department(request, department_name):
    if department_name not in dict(Department.departmentChoices):
        return Response('page not found', HTTP_404_NOT_FOUND)
    med_workers = MedicalWorker.objects.filter(department__name=department_name)
    response = []
    for med_worker in med_workers:
        user = CustomUserSerializer(med_worker.user).data
        med_workers_data = MedicalWorkerSerializer(med_worker).data
        response.append({**user, **med_workers_data})
    return Response(response, HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def appointments(request):
    if request.user.is_authenticated:
        if request.user.category == 'med_worker':
            appointment_data = Appointment.objects.filter(doctor=request.user)
        else:
            appointment_data = Appointment.objects.filter(patient=request.user)
    else:
        appointment_data = Appointment.objects.all()
    serialized = AppointmentSerializer(appointment_data, many=True)
    return Response(serialized.data, HTTP_200_OK)
