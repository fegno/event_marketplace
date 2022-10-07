# New file created 
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, FormView, ListView


class DestinationCreateView(CreateView):
	queryset = Destination.objects.all()
	template_name = 'templates/destination_create.html'
	model = Destination


class DestinationDetailView(UpdateView):
	queryset = Destination.objects.all()
	template_name = 'templates/destination_detail.html'
	model = Destination


class DestinationListView(ListView):
	queryset = Destination.objects.all()
	template_name = 'templates/destination_list.html'
	model = Destination


class DestinationDeleteView(DeleteView):
	queryset = Destination.objects.all()
	template_name = 'templates/destination_delete.html'
	model = Destination


