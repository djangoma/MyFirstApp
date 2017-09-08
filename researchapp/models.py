import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
#from django.core.urlresolvers import reverse
from django.urls import reverse

# Create your models here.
class Faculty(models.Model):
	empid = models.CharField(primary_key=True, verbose_name="Employee ID",max_length=20)
	deptname= models.CharField(verbose_name="Department Name",max_length=20)
	facultyname=models.CharField(verbose_name="Faculty Name",max_length=100)
	username=models.CharField(verbose_name="User Name",max_length=20)
	password=models.CharField(verbose_name="Password",max_length=20)
	
	def __str__(self):
		return self.facultyname
	
class Journal(models.Model):
	#empid = models.ForeignKey('Faculty',verbose_name="Employee ID",max_length=20,on_delete=models.CASCADE)
	empid = models.ManyToManyField('Faculty',verbose_name="Employee ID",max_length=20)
	#facultyname=models.CharField(verbose_name="Faculty Name",max_length=50)
	papertitle=models.CharField(verbose_name="Paper Title",max_length=100,blank=False,default='x')
	jtitle=models.CharField(verbose_name="Journal Name",max_length=200,blank=False,default='x')
	facultyauthorname=models.CharField(verbose_name="Author-Faculty",max_length=200,blank=True)
	ugauthorname=models.CharField(verbose_name="Author-UG",max_length=200,blank=True)
	pgauthorname=models.CharField(verbose_name="Author-PG",max_length=200,blank=True)
	rscholarauthorname=models.CharField(verbose_name="Author-ResearchScholar",max_length=200,blank=True)
	publishedon=models.DateField(verbose_name="Published On",default=timezone.now())
	pageno=models.CharField(verbose_name="Page No",max_length=50,blank=True)
	volume=models.CharField(verbose_name="Volume",max_length=50,blank=True)
	issnno=models.CharField(verbose_name="ISSN NO",max_length=50,blank=True)
	sjr=models.CharField(verbose_name="SJR",max_length=50,blank=True)
	snip=models.CharField(verbose_name="SNIP",max_length=50,blank=True)
	sciif=models.CharField(verbose_name="SCI-IF",max_length=50,blank=True)
	refformat=models.TextField(verbose_name="Citation Format",max_length=500,blank=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.papertitle
	
	def get_absolute_url(self):
	    return reverse('researchapp:journal-detail',kwargs={'pk': self.pk} )
	    #return reverse('journal-detail',args=[str(self.id)])
	    #return reverse('journal-detail',kwargs={'pk': str(self.id)} )
	    #args=[str(self.id)]
		#kwargs={'pk':self.pk}
	
class Conference(models.Model):
	#empid = models.ForeignKey('Faculty',verbose_name="Employee ID",max_length=20,on_delete=models.CASCADE)
	empid = models.ManyToManyField('Faculty',verbose_name="Employee ID",max_length=20)
	#facultyname=models.CharField(verbose_name="Faculty Name",max_length=50)
	cpapertitle=models.CharField(verbose_name="Paper Title",max_length=200)
	ctitle=models.CharField(verbose_name="Conference Title",max_length=100)
	facultyauthorname=models.CharField(verbose_name="Author-Faculty",max_length=200,blank=True)
	ugauthorname=models.CharField(verbose_name="Author-UG",max_length=200,blank=True)
	pgauthorname=models.CharField(verbose_name="Author-PG",max_length=200,blank=True)
	rscholarauthorname=models.CharField(verbose_name="Author-ResearchScholar",max_length=200,blank=True)
	venue=models.CharField(verbose_name="Venue",max_length=50)
	cdatefrom=models.DateField(verbose_name="Conference Date From: ")
	cdateto=models.DateField(verbose_name="Conference Date To: ")
	NATIONAL='National'
	INTERNATIONAL='International'
	conferencecategory_choice=((NATIONAL,'National'),(INTERNATIONAL,'International'),)
	conferencecategory=models.CharField(verbose_name="Conference Category",max_length=50,choices=conferencecategory_choice, default=INTERNATIONAL)
	presentedby=models.CharField(verbose_name="Presented By",max_length=50)
	#presentedon=models.CharField(verbose_name="Presented On",max_length=50, blank=False,null=False,default='')
	bestpaperaward=models.BooleanField()
	refformat=models.TextField(verbose_name="Citation Format",max_length=500, blank=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.cpapertitle
	
	def get_absolute_url(self):
	    return reverse('researchapp:conference-detail', kwargs={'pk': self.pk})
    
	class Meta:
		ordering = ["cdatefrom"]
		
class Externalfp(models.Model):
	#empid = models.ForeignKey('Faculty',verbose_name="Employee ID",max_length=20,on_delete=models.CASCADE)
	empid = models.ManyToManyField('Faculty',verbose_name="Employee ID",max_length=20)
	#facultyname=models.CharField(verbose_name="Faculty Name",max_length=100)
	projecttitle=models.CharField(verbose_name="Project Title",max_length=100)
	pi=models.CharField(verbose_name="PI",max_length=100)
	copi=models.CharField(verbose_name="Co-PI",max_length=100,blank=True)
	fundingagency=models.CharField(verbose_name="Funding Agency",max_length=200)
	duration=models.CharField(verbose_name="Duration",max_length=50)
	sanctioneddate=models.DateField(verbose_name="Sanctioned Date",max_length=50)
	sanctionedamount=models.CharField(verbose_name="Sanctioned Amount",max_length=50)
	fundreleasedon=models.CharField(verbose_name="Fund Released On",max_length=100, blank=True)
	amountreceived=models.CharField(verbose_name="Amount Received",max_length=100, blank=True)
	completiondate=models.DateField(verbose_name="Completion Date", blank=True)
	outcome=models.TextField(verbose_name="Outcome",max_length=500, blank=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.projecttitle
	
	def get_absolute_url(self):
	    return reverse('researchapp:externalfp-detail',kwargs={'pk': self.pk} )
	
	class Meta:
		ordering = ["sanctioneddate"]
	
	
class Facultyifp(models.Model):
	#empid = models.ForeignKey('Faculty',verbose_name="Employee ID",max_length=20,on_delete=models.CASCADE) 
	empid = models.ManyToManyField('Faculty',verbose_name="Employee ID",max_length=20)
	#facultyname=models.CharField(verbose_name="Faculty Name",max_length=50)
	projecttitle=models.CharField(verbose_name="Project Title",max_length=100)
	pi=models.CharField(verbose_name="PI",max_length=100)
	copi=models.CharField(verbose_name="Co-PI",max_length=100,blank=True)
	duration=models.CharField(verbose_name="Duration",max_length=50)
	sanctioneddate=models.DateField(verbose_name="Sanctioned Date",max_length=50)
	sanctionedamount=models.CharField(verbose_name="Sanctioned Amount",max_length=50)
	fundreleasedon=models.CharField(verbose_name="Fund Released On", max_length=100, blank=True)
	amountreceived=models.CharField(verbose_name="Amount Received",max_length=100, blank=True)
	completiondate=models.DateField(verbose_name="Completion Date", blank=True)
	outcome=models.TextField(verbose_name="Outcome",max_length=500, blank=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.projecttitle
	
	def get_absolute_url(self):
	    return reverse('researchapp:facultyifp-detail', kwargs={'pk':self.pk})
    
	class Meta:
	    ordering = ["sanctioneddate"]
		
class Studentifp(models.Model):
	#empid = models.ForeignKey('Faculty',verbose_name="Employee ID",max_length=20,on_delete=models.CASCADE)
	empid = models.ManyToManyField('Faculty',verbose_name="Employee ID",max_length=20)
	#facultyname=models.CharField(verbose_name="Faculty Name",max_length=100)
	studentname=models.CharField(verbose_name="Student Name",max_length=200)
	projecttitle=models.CharField(verbose_name="Project Title",max_length=100)
	pi=models.CharField(verbose_name="PI",max_length=100)
	copi=models.CharField(verbose_name="Co-PI",max_length=100,blank=True)
	duration=models.CharField(verbose_name="Duration",max_length=50)
	sanctioneddate=models.DateField(verbose_name="Sanctioned Date",max_length=50)
	sanctionedamount=models.CharField(verbose_name="Sanctioned Amount",max_length=50)
	fundreleasedon=models.CharField(verbose_name="Fund Released On", max_length=100, blank=True)
	amountreceived=models.CharField(verbose_name="Amount Received",max_length=100, blank=True)
	completiondate=models.DateField(verbose_name="Completion Date", blank=True)
	outcome=models.TextField(verbose_name="Outcome",max_length=500, blank=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.projecttitle
	
	def get_absolute_url(self):
	    return reverse('researchapp:studentifp-detail',kwargs={'pk': self.pk} )
	
	class Meta:
		ordering = ["sanctioneddate"]
		
