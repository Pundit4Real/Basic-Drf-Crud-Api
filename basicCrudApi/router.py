from person.viewsets import PersonViewset
from rest_framework import routers

# setting up the router function

app_name = 'person'

router = routers.DefaultRouter()
router.register('person',PersonViewset,basename='PersonViewset')

