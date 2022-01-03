import django_filters
from django import forms
from django.db import models
from django_filters import DateFilter

from .models import *

class DonationsFilter(django_filters.FilterSet):
	def __init__(self, *args, **kwargs):
  		super().__init__(*args, **kwargs)
  		for field in self.form.fields:
  			self.form.fields[field].widget.attrs.update({'class': 'form-control'})
	from_date 	= DateFilter(field_name='Date', lookup_expr='gte')
	to_date 	= DateFilter(field_name='Date', lookup_expr='lte')	
	class Meta:
		model 	= Donations
		fields = ['Issued_By', 'Donation_Towards', 'Paid_Through']

class ExpensesFilter(django_filters.FilterSet):
	def __init__(self, *args, **kwargs):
  		super().__init__(*args, **kwargs)
  		for field in self.form.fields:
  			self.form.fields[field].widget.attrs.update({'class': 'form-control'})
	from_date 	= DateFilter(field_name='Date', lookup_expr='gte')
	to_date 	= DateFilter(field_name='Date', lookup_expr='lte')	
	class Meta:
		model 	= Expenses
		fields = ['Towards', 'Category']

   