from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Sneaker
from .serializers import SneakerSerializer
from .permissions import IsOwnerOrReadOnly

class SneakerList(ListCreateAPIView):
    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    queryset = Sneaker.objects.all()

    #serializing
    serializer_class = SneakerSerializer

# The SneakerDetail needs the same things
class SneakerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Sneaker.objects.all()
    serializer_class = SneakerSerializer
    permission_classes = (IsOwnerOrReadOnly,)
