from django.db import models

# Create your models here.
class Poll(models.Model):
    def __unicode__(self):
        return self.question
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __unicode__(self):
        return self.choice
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()


class Category(models.Model):
    def __unicode__(self):
        return self.servicename
    servicename = models.CharField(max_length=200)
    categoryImage = models.ImageField(upload_to='images',
                     verbose_name = "Image",
                     blank=True
            )
    serviceRanking=models

class ServiceProvider(models.Model):
     def __unicode__(self):
         return self.providername
     providername =  models.CharField(max_length=200)
     fullName=models.CharField(max_length=200, verbose_name="Full Name")
     contactNum1= models.CharField(max_length=100, verbose_name="Primary Phone")
     contactNum2=models.CharField(max_length=100,blank=True, verbose_name="Phone Number 2")
     email=models.EmailField(verbose_name="Email")
     image=models.ImageField(upload_to='images',
                     verbose_name = "ServiceImage",
                     blank=True
            )
     address1=models.CharField(max_length=200,verbose_name="Address Line 1")
     address2=models.CharField(max_length=200, blank=True, verbose_name="Address Line 2")
     city=models.CharField(max_length=100,verbose_name="City")
     state=models.CharField(max_length=100, verbose_name="State")
     country=models.CharField(max_length=100, verbose_name="Country")
     zipcode=models.CharField(max_length=10,verbose_name="Zipcode")
     website=models.URLField(max_length=200, blank=True, verbose_name="Website or Blog") #optional
     #ipaddress=models.CharField(max_length=200)
     servicename=models.ForeignKey('Category')
     speciality=models.CharField(max_length=200, blank=True)
     sponsorlevel=models.IntegerField(max_length=2,blank=True )
     averageRating=models.DecimalField(max_digits=3,decimal_places=2, blank=True)
     latlon=models.CharField(max_length=200,blank=True)
     selfRegistered=models.BooleanField(blank=True)
     description=models.TextField(blank=True)
     serviceCharge=models.CharField(max_length=200,blank=True)




class TestMurali(models.Model):

    king = models.CharField(max_length=20)
    city = models.CharField(max_length=200)


    #image= models.URLField(max_length=200)
    #image = models.URLField(
    #   max_length = 100,
    #    verbose_name = "Images",
    #    blank=True
    #    )