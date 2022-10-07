# New file created 
from django.urls import path, include
urlpatterns = [path('Event/', include([
    path('', EventListView.as_view(), name='event-list'),
    path('create/', EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/update/', EventDetailView.as_view(), name='event-update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]))]
# New file created 
from django.urls import path, include
urlpatterns = [path('Destination/', include([
path('', DestinationListView.as_view(), name='destination-list'),
path('create/', DestinationCreateView.as_view(), name='destination-create'),
path('<int:pk>/update/', DestinationDetailView.as_view(), name='destination-update'),
path('<int:pk>/delete/', DestinationDeleteView.as_view(), name='destination-delete'),
]))]
# New file created 
from django.urls import path, include
urlpatterns = [path('Venue/', include([
path('', VenueListView.as_view(), name='venue-list'),
path('create/', VenueCreateView.as_view(), name='venue-create'),
path('<int:pk>/update/', VenueDetailView.as_view(), name='venue-update'),
path('<int:pk>/delete/', VenueDeleteView.as_view(), name='venue-delete'),
]))]
