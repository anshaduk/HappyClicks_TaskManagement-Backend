from django.shortcuts import render
from rest_framework import viewsets,permissions,status,filters
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from . models import Task
from . serializers import TaskSerializer,UserSerializer



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title','description']
    ordering_fields = ['due_date','priority','status']


    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        priority = self.request.query_params.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_stats(request):
    total = Task.objects.filter(user=request.user).count()
    stats = Task.objects.filter(user=request.user).values('status').annotate(count=Count('status'))

    result = {
        'total': total,
        'by_status': {item['status']:item['count'] for item in stats}
    }

    all_statuses = dict(Task.STATUS_CHOICES)
    for status_code in  all_statuses.keys():
        if status_code not in result['by_status']:
            result['by_status'][status_code] = 0

    return Response(result)
    
