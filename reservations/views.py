from django.views.generic import FormView, CreateView

from django.http import HttpResponse, HttpResponseRedirect
from .forms import MakeReservationForm, DetailReservationForm, SelectVehicleReservationForm
from reservations.models import Reservation
from vehicle.models import Vehicle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from formtools.wizard.views import SessionWizardView
#from django.db.models import Max, OuterRef, Subquery



class MakeReservationView(CreateView):
    form_class = MakeReservationForm
    template_name = "make_reservation.html"
    model = Reservation

    def get_initial(self):
        return {'vehicle': self.kwargs.get('vehicle_pk')}
    

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    

    def get_success_url(self):
        from django.urls import reverse
        return reverse('reservations')

class DetailReservationView(CreateView):
    form_class = DetailReservationForm
    template_name = "detail_reservation.html"
    model = Reservation

    def get_initial(self):
        return {'vehicle': self.kwargs.get('vehicle_pk')}
    

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    

    def get_success_url(self):
        from django.urls import reverse
        return reverse('reservations')



class MyReservationView(FormView):
    form_class = MakeReservationForm  #new form goes here for status 
    template_name = "reservations.html"

    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        elif self.request.method == 'GET':
            kwargs.update({
                'data': self.request.GET.copy()
            })
        return kwargs 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Reservation.objects.all() # start here to be able to read get request query parameters for django 
        

        

        context.update({
        "reservation_list": queryset,
        
        })

        return context


class ReservationWizard(SessionWizardView):
    

    def get_template_names(self):
        if self.steps.current =='0':
            return 'make_reservation.html'
        if self.steps.current =='1':
            return 'vehicle_reservation_list.html'
        elif self.steps.current =='2':
            return "detail_reservation.html"

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        if self.steps.current == '1':
            vehicles = Vehicle.objects.filter()
            context.update({'vehicle_list': vehicles})
        elif self.steps.current == '2':
            vehicle_form_data = self.get_cleaned_data_for_step('1')
            vehicle = vehicle_form_data['vehicle']
            context.update({'vehicle':vehicle})
            reservation_form_data = self.get_cleaned_data_for_step('0')
            reservation = reservation_form_data['leaving_From']
            context.update({'leaving_From':reservation}) 
            reservation_form_data = self.get_cleaned_data_for_step('0')
            reservation = reservation_form_data['heading_To']
            context.update({'heading_To':reservation})
            reservation = reservation_form_data['leaving_By']
            context.update({'leaving_By':reservation})
            reservation = reservation_form_data['returning_By']
            context.update({'returning_By':reservation})
            

        return context

    def done(self, form_list, **kwargs):
         return HttpResponseRedirect(reverse('reservations'))

    
        
   