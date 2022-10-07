# New file created 
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, FormView, ListView


class EventCreateView(CreateView):
	queryset = Event.objects.all()
	template_name = 'templates/event_create.html'
	model = Event


class EventDetailView(UpdateView):
	queryset = Event.objects.all()
	template_name = 'templates/event_detail.html'
	model = Event


class EventListView(ListView):
	queryset = Event.objects.all()
	template_name = 'templates/event_list.html'
	model = Event


class EventDeleteView(DeleteView):
	queryset = Event.objects.all()
	template_name = 'templates/event_delete.html'
	model = Event


