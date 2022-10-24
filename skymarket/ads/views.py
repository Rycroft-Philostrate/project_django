from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets

from ads.models import Ad, Comment
from ads.permissions import AdOwner, AdAdmin
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer
from ads.filters import AdFilter
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_classes = {
        'list': AdSerializer,
        'create': AdDetailSerializer,
        'retrieve': AdDetailSerializer,
        'update': AdDetailSerializer,
        'partial_update': AdDetailSerializer,
        'destroy': AdDetailSerializer,
    }
    default_serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_permission(self):
        permission_classes = (AllowAny,)
        if self.action == "retrieve":
            permission_classes = (AllowAny,)
        elif self.action in ("create", "update", "partial_update", "destroy", "me"):
            permission_classes = (AdOwner | AdAdmin,)
        return (permission() for permission in permission_classes)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        return ad_instance.comments.all()

    def get_permission(self):
        permission_classes = (IsAuthenticated,)
        if self.action in ("list", "retrieve"):
            permission_classes = (IsAuthenticated,)
        elif self.action in ("create", "update", "partial_update", "destroy"):
            permission_classes = (AdOwner | AdAdmin,)
        return (permission() for permission in permission_classes)

