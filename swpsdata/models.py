from django.db import models 

class DonationsCat(models.Model):
	Donations_Category = models.CharField(max_length=100, null=True, blank=True, help_text='Donations Category')
	
	def __str__(self):
		return str(self.Donations_Category)

class Staff(models.Model):
	Name 		= models.CharField(max_length=100, null=True, help_text='Staff Name')
	Phone_No 	= models.IntegerField(null=True, blank=True, help_text='Phone Number')
	Designation = models.CharField(max_length=50, null=True, help_text='Designation of Staff')
	Address 	= models.TextField(max_length=1000, null=True, blank=True, help_text='Address')
	Join_Date 	= models.DateField(help_text='Join Date', blank=True, null=True) 
	User_Name 	= models.CharField(max_length=20, null=True, blank=True, help_text='User Name')
	Is_Active  	= models.BooleanField(default=True, help_text='Unmark if Staff Resigned')

	def __str__(self):
		return str(self.Name)

class Expenses(models.Model):
	Date 	= models.DateField() 
	Towards = models.ForeignKey(DonationsCat, on_delete=models.CASCADE, null=True, blank=True)
	Category = models.CharField(max_length=20, choices=(('Puja Samagri', 'Puja Samagri'), ('Transport', 'Transport'), ('Food', 'Food'), ('Salary', 'Salary'),  ('General', 'General')))
	Amount 	= models.FloatField(help_text='Amount in Rupees')
	Paid_Through= models.CharField(max_length=20, null=True, choices=(('Cash', 'Cash'), ('Online', 'Online')))
	By 		= models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
	
	def __str__(self):
		return str(self.Date)+'-'+str(self.Category)

class Donations(models.Model):
	Donor_Name 	= models.CharField(max_length=100, null=True, help_text='Donor Name', blank=True)
	Phone_No 	= models.IntegerField(null=True, blank=True, help_text='Phone Number')
	Receipt_No 	= models.CharField(max_length=10, null=True, blank=True, unique=True, help_text='Receipt Number')
	# Date 		= models.DateTimeField(null=True, auto_now_add=True)
	Date 		= models.DateField(null=True, blank=True)
	Gothram 	= models.CharField(max_length=100, null=True, blank=True, help_text='Donor Name')
	Donation_Towards = models.ForeignKey(DonationsCat, on_delete=models.CASCADE, null=True)
	Amount 		= models.IntegerField(null=True, help_text='Amount in Rupees')
	Paid_Through= models.CharField(max_length=20, choices=(('Paid-Cash', 'Paid-Cash'), ('Paid-Online', 'Paid-Online'), ('Due', 'Due')))
	Issued_By 	= models.CharField(max_length=30, blank=True, null=True)
	Address 	= models.TextField(max_length=1000, null=True, blank=True, help_text='Optional')

	def __str__(self):
		return str(self.Donor_Name)+'-'+str(self.Phone_No)+'-'+str(self.Amount)


class Salaries(models.Model):
	Name 		= models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
	Date 		= models.DateField()
	Amount 		= models.IntegerField(null=True, help_text='Amount in Rupees')
	Paid_Through= models.CharField(max_length=20, choices=(('Cash', 'Cash'), ('Online', 'Online')))

	def __str__(self):
		return str(self.Name)+'-'+str(self.Date)+'-'+str(self.Amount)

class Hundi(models.Model):
	Date 		= models.DateField(help_text='Enter any Date within the hundi collection month')
	Amount 		= models.IntegerField(null=True, help_text='Amount in Rupees')
	By 		= models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.Date)+'-'+str(self.Amount)


class Voice(models.Model):
	Name = models.CharField(max_length=255, blank=True, null=True)
	Gothram = models.CharField(max_length=255, blank=True, null=True)
	Address 	= models.TextField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return str(self.Name)+'-'+str(self.Gothram)