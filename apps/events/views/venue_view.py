# New file created 
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, FormView, ListView

class VenueCreateView(CreateView):
	queryset = Venue.objects.all()
	template_name = 'templates/venue_create.html'
	model = Venue


class VenueDetailView(UpdateView):
	queryset = Venue.objects.all()
	template_name = 'templates/venue_detail.html'
	model = Venue


class VenueListView(ListView):
	queryset = Venue.objects.all()
	template_name = 'templates/venue_list.html'
	model = Venue


class VenueDeleteView(DeleteView):
	queryset = Venue.objects.all()
	template_name = 'templates/venue_delete.html'
	model = Venue


