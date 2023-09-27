from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerID=models.CharField(max_length= 10, primary_key=True)
    Name=models.CharField(max_length=15)
    Address_Line1=models.CharField(max_length=50, blank=True)
    Address_Line2=models.CharField(max_length=50, blank=True, null=True)
    Contact_Person=models.CharField(max_length=50, blank=True, null=True)
    state=models.CharField(max_length=50,  null=True)
    country=models.CharField(max_length=50, default="India")
    createdOn=models.DateField(auto_created=True)
    email=models.EmailField("Email: ", max_length=254)

    def __str__(self):
        return self.Name

class Consingment(models.Model):
    PNI_No=models.CharField("PNI No",primary_key=True,auto_created=True,max_length= 10)
    product=models.CharField("Product Name", max_length=20)
    weight= models.DecimalField("Weight of Container", max_digits=5, decimal_places=2)
    accepted=models.BooleanField(" Accepted or not")
    No_of_boxes= models.IntegerField()
    Arrival_date=models.DateField()
    Dispatch_date=models.DateField(blank=True, null=True)
    Customer=models.ForeignKey(Customer,null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.product+ " (" + self.PNI_No + ")"
class DosimeterBatch(models.Model):
    batchNo= models.IntegerField(primary_key=True)
    bDate=models.DateField()
    Qnty =models.IntegerField()

    def __str__(self):
        return self.batchNo
    
class DosimeterVial(models.Model):
    slNo= models.IntegerField(" Serial No.", primary_key=True)
    batchNo=models.ForeignKey(DosimeterBatch,on_delete=models.CASCADE)
    
        
    
        class Meta:
            verbose_name = _("")
            verbose_name_plural = _("s")
    
        def __str__(self):
            return self.name
    
        def get_absolute_url(self):
            return reverse("_detail", kwargs={"pk": self.pk})
    
