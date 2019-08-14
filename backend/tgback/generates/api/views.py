from rest_framework import viewsets
from generates.models import Generate
from .serializers import GenerateSerializer


class GenerateViewSet(viewsets.ModelViewSet):
    serializer_class = GenerateSerializer
    queryset = Generate.objects.all()


# from rest_framework.generics import (
#     ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)


# class GenerateListView(ListAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer


# class GenerateDetailView(RetrieveAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer


# class GenerateCreateView(CreateAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer


# class GenerateUpdateView(UpdateAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer


# class GenerateDeleteView(DestroyAPIView):
#     queryset = Generate.objects.all()
#     serializer_class = GenerateSerializer
