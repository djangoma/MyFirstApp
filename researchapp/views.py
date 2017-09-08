from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Journal, Conference, Faculty, Externalfp, Facultyifp, Studentifp
from django.shortcuts import redirect
from .forms import ViewJournalForm, ContactForm, JournalForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.urlresolvers import reverse


#############	
	
class JournalCreate(CreateView):
    model = Journal
    fields='__all__'
        
class JournalUpdate(UpdateView):
    model=Journal
    fields='__all__'
    #form_class=JournalForm
    template_name_suffix='_update_form'
    
class JournalDelete(DeleteView):
    model=Journal
    success_url=reverse_lazy('researchapp:journal-list')	

class JournalListView(ListView):
    model=Journal
    
    def get_context_data(self, **kwargs):
	    context= super(JournalListView, self).get_context_data(**kwargs)
	    #context[&#39;now&#39;]=timezone.now()
	    return context
    
class JournalDetailView(DetailView):
    model=Journal
	
    def get_context_data(self, **kwargs):
	    context= super(JournalDetailView, self).get_context_data(**kwargs)
		#context[&#39;now&#39;]=timezone.now()
	    return context
		
############
class ConferenceCreate(CreateView):
    model = Conference
    fields='__all__'
        
class ConferenceUpdate(UpdateView):
    model=Conference
    fields='__all__'
    #form_class=JournalForm
    template_name_suffix='_update_form'
    
class ConferenceDelete(DeleteView):
    model=Conference
    success_url=reverse_lazy('researchapp:conference-list')	

class ConferenceListView(ListView):
    model=Conference
    
    def get_context_data(self, **kwargs):
	    context= super(ConferenceListView, self).get_context_data(**kwargs)
	    #context[&#39;now&#39;]=timezone.now()
	    return context
    
class ConferenceDetailView(DetailView):
    model=Conference
	
    def get_context_data(self, **kwargs):
	    context= super(ConferenceDetailView, self).get_context_data(**kwargs)
		#context[&#39;now&#39;]=timezone.now()
	    return context

############

#Externalfundedproject

class ExternalfpCreate(CreateView):
    model = Externalfp
    fields='__all__'
        
class ExternalfpUpdate(UpdateView):
    model=Externalfp
    fields='__all__'
    #form_class=JournalForm
    template_name_suffix='_update_form'
    
class ExternalfpDelete(DeleteView):
    model=Externalfp
    success_url=reverse_lazy('researchapp:externalfp-list')	

class ExternalfpListView(ListView):
    model=Externalfp
    
    def get_context_data(self, **kwargs):
	    context= super(ExternalfpListView, self).get_context_data(**kwargs)
	    #context[&#39;now&#39;]=timezone.now()
	    return context
    
class ExternalfpDetailView(DetailView):
    model=Externalfp
	
    def get_context_data(self, **kwargs):
	    context= super(ExternalfpDetailView, self).get_context_data(**kwargs)
		#context[&#39;now&#39;]=timezone.now()
	    return context

############
#Facultyinternalfundedproject

class FacultyifpCreate(CreateView):
    model = Facultyifp
    fields='__all__'
        
class FacultyifpUpdate(UpdateView):
    model=Facultyifp
    fields='__all__'
    #form_class=JournalForm
    template_name_suffix='_update_form'
    
class FacultyifpDelete(DeleteView):
    model=Facultyifp
    success_url=reverse_lazy('researchapp:facultyifp-list')	

class FacultyifpListView(ListView):
    model=Facultyifp
    
    def get_context_data(self, **kwargs):
	    context= super(FacultyifpListView, self).get_context_data(**kwargs)
	    #context[&#39;now&#39;]=timezone.now()
	    return context
    
class FacultyifpDetailView(DetailView):
    model=Facultyifp
	
    def get_context_data(self, **kwargs):
	    context= super(FacultyifpDetailView, self).get_context_data(**kwargs)
		#context[&#39;now&#39;]=timezone.now()
	    return context

############
#Studentinternalfundedproject
class StudentifpCreate(CreateView):
    model = Studentifp
    fields='__all__'
        
class StudentifpUpdate(UpdateView):
    model=Studentifp
    fields='__all__'
    #form_class=JournalForm
    template_name_suffix='_update_form'
    
class StudentifpDelete(DeleteView):
    model=Studentifp
    success_url=reverse_lazy('researchapp:studentifp-list')	

class StudentifpListView(ListView):
    model=Studentifp
    
    def get_context_data(self, **kwargs):
	    context= super(StudentifpListView, self).get_context_data(**kwargs)
	    #context[&#39;now&#39;]=timezone.now()
	    return context
    
class StudentifpDetailView(DetailView):
    model=Studentifp
	
    def get_context_data(self, **kwargs):
	    context= super(StudentifpDetailView, self).get_context_data(**kwargs)
		#context[&#39;now&#39;]=timezone.now()
	    return context

############


'''def add_journal(request, pk):
    paper=get_object_or_404(Journal, pk=pk)
    journal_form=JournalForm(request.POST or None)
    if journal_form.is_valid():
	    new_paper=journal_form.save(commit=False)
	    new_paper.paper=paper
	    new_paper.save()
	    return redirect('/')
		
    return render(request, 'researchapp/journal_list.html', {'form':journal_form})'''


#############
		
# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
	try:
		num_j_papers = Journal.objects.all().count()
		context= {'num_j_papers':num_j_papers}
		
		num_c_papers = Conference.objects.all().count()
		context.update({'num_c_papers':num_c_papers})
		
		num_efp = Externalfp.objects.all().count()
		context.update({'num_efp':num_efp})
		
		num_fifp = Facultyifp.objects.all().count()
		context.update({'num_fifp':num_fifp})
		
		num_sifp=Studentifp.objects.all().count()
		context.update({'num_sifp':num_sifp})
		
		jpaper_list=Journal.objects.all()
		context.update({'jpaper_list':jpaper_list})
		
		cpaper_list=Conference.objects.all()
		context.update({'cpaper_list':cpaper_list})
		
					
	except Journal.DoesNotExist:
		raise Http404("Journal does not exist")
	return render(request, 'researchapp/index.html', context)
	
'''def journals(request):
	try:
		jpaper_list=Journal.objects.all()
		context={'jpaper_list':jpaper_list}
	except Journal.DoesNotExist:
		raise Http404("Journal does not exist")
	return render(request, 'app4/journals.html', context)
	
def conferences(request):
	try:
			
		cpaper_list=Conference.objects.all()
		context={'cpaper_list':cpaper_list}
				
	except Conference.DoesNotExist:
		raise Http404("Journal does not exist")
	return render(request, 'app4/conferences.html', context)'''

def externalfp(request):
	try:
			
		efp_list=Externalfundedproject.objects.all()
		context={'efp_list':efp_list}
				
	except Externalfundedproject.DoesNotExist:
		raise Http404("External funded project does not exist")
	return render(request, 'researchapp/externalfp.html', context)
	
def facultyifp(request):
	try:
			
		f_ifp_list=facultyinternalfundedproject.objects.all()
		context={'f_ifp_list':f_ifp_list}
				
	except facultyinternalfundedproject.DoesNotExist:
		raise Http404("Faculty intenal funded project does not exist")
	return render(request, 'researchapp/facultyifp.html', context)
	
def studentifp(request):
	try:
			
		s_ifp_list=studentinternalfundedproject.objects.all()
		context={'s_ifp_list':s_ifp_list}
				
	except studentinternalfundedproject.DoesNotExist:
		raise Http404("Student intenal funded project does not exist")
	return render(request, 'researchapp/studentifp.html', context)
	

