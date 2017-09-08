from django.conf.urls import url
from .import views
from researchapp.views import JournalDetailView, JournalListView


app_name='researchapp'
urlpatterns = [ 
				url(r'^$',views.index, name='index'),				
				url(r'^journals/$', views.JournalListView.as_view(), name='journal-list'),
				url(r'^journal/(?P<pk>\d+)/$', views.JournalDetailView.as_view(), name='journal-detail'),
				url(r'^journal/create/$',views.JournalCreate.as_view(), name='journal_create'),
				url(r'^journal/(?P<pk>\d+)/update/$',views.JournalUpdate.as_view(), name='journal_update'),
				url(r'^journal/(?P<pk>\d+)/delete/$',views.JournalDelete.as_view(), name='journal_delete'),
				url(r'^conferences/$', views.ConferenceListView.as_view(), name='conference-list'),
				url(r'^conference/(?P<pk>\d+)/$', views.ConferenceDetailView.as_view(), name='conference-detail'),
				url(r'^conference/create/$',views.ConferenceCreate.as_view(), name='conference_create'),
				url(r'^conference/(?P<pk>\d+)/update/$',views.ConferenceUpdate.as_view(), name='conference_update'),
				url(r'^conference/(?P<pk>\d+)/delete/$',views.ConferenceDelete.as_view(), name='conference_delete'),
				url(r'^externalfps/$', views.ExternalfpListView.as_view(), name='externalfp-list'),
				url(r'^externalfp/(?P<pk>\d+)/$', views.ExternalfpDetailView.as_view(), name='externalfp-detail'),
				url(r'^externalfp/create/$',views.ExternalfpCreate.as_view(), name='externalfp_create'),
				url(r'^externalfp/(?P<pk>\d+)/update/$',views.ExternalfpUpdate.as_view(), name='externalfp_update'),
				url(r'^externalfp/(?P<pk>\d+)/delete/$',views.ExternalfpDelete.as_view(), name='externalfp_delete'),
				url(r'^facultyifps/$', views.FacultyifpListView.as_view(), name='facultyifp-list'),
				url(r'^facultyifp/(?P<pk>\d+)/$', views.FacultyifpDetailView.as_view(), name='facultyifp-detail'),
				url(r'^facultyifp/create/$',views.FacultyifpCreate.as_view(), name='facultyifp_create'),
				url(r'^facultyifp/(?P<pk>\d+)/update/$',views.FacultyifpUpdate.as_view(), name='facultyifp_update'),
				url(r'^facultyifp/(?P<pk>\d+)/delete/$',views.FacultyifpDelete.as_view(), name='facultyifp_delete'),
				url(r'^studentifps/$', views.StudentifpListView.as_view(), name='studentifp-list'),
				url(r'^studentifp/(?P<pk>\d+)/$', views.StudentifpDetailView.as_view(), name='studentifp-detail'),
				url(r'^studentifp/create/$',views.StudentifpCreate.as_view(), name='studentifp_create'),
				url(r'^studentifp/(?P<pk>\d+)/update/$',views.StudentifpUpdate.as_view(), name='studentifp_update'),
				url(r'^studentifp/(?P<pk>\d+)/delete/$',views.StudentifpDelete.as_view(), name='studentifp_delete'),
						
			]
'''url(r'^conferences/$', views.ConferenceListView.as_view(), name='conference-list'),
				url(r'^conference/(?P<pk>\d+)/$', views.ConferenceDetailView.as_view(), name='conference-detail'),
				url(r'^conference/create/$',views.ConferenceCreate.as_view(), name='conference_create'),
				url(r'^conference/(?P<pk>\d+)/update/$',views.ConferenceUpdate.as_view(), name='conference_update'),
				url(r'^conference/(?P<pk>\d+)/delete/$',views.ConferenceDelete.as_view(), name='conference_delete'),
				
				url(r'^journals',views.journals, name='journals'),
				url(r'^conferences',views.conferences, name='conferences'),
				url(r'^externalfp',views.externalfp, name='externalfp'),
				url(r'^facultyifp',views.facultyifp, name='facultyifp'),
				url(r'^studentifp',views.studentifp, name='studentifp'),
				'''