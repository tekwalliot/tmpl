from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
import os
from .models import *
from .forms import *
from .filters import *
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date, datetime, timedelta 
import re
from django.db.models import Sum, Avg, Count
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Q
import random
from translate import Translator 
import speech_recognition as sr

from django_xhtml2pdf.utils import generate_pdf
from PyPDF2 import PdfFileMerger

def PDF_File(request, var):
	dt = Donations.objects.get(id=var)
	return render(request, 'inv.html', {'dt': dt})

	# resp = HttpResponse(content_type='application/pdf')
    # result = generate_pdf('inv.html', file_object=resp)
    # return result

def Voice_Name(request):
	name = Voice.objects.all().last()
	if name:
		if name.Name:
			name = name.Name
		else:
			name = ''
	else:
		name = ''
	return render(request, 'VoiceName.html', {'name': name})

def Voice_Gothram(request):
	name = Voice.objects.all().last()
	if name:
		if name.Gothram:
			name = name.Gothram
		else:
			name = ''
	else:
		name = ''
	return render(request, 'VoiceGothram.html', {'name': name})


def upload(request, var):
    # customHeader = request.META['HTTP_MYCUSTOMHEADER']

    # obviously handle correct naming of the file and place it somewhere like media/uploads/
    filename = str(Voice.objects.count())
    filename = filename + "name" + ".wav"
    uploadedFile = open(filename, "wb")
    # the actual file is in request.body
    uploadedFile.write(request.body)
    uploadedFile.close()
    # put additional logic like creating a model instance or something like this here
    r = sr.Recognizer()
    harvard = sr.AudioFile(filename)
    with harvard as source:
        audio = r.record(source)
    msg = r.recognize_google(audio, language='te-IN')
    os.remove(filename)
    data = Voice.objects.all().last()
    print(var)

    if var == '0' and msg != '':
    	print('j')
    	if data:
    		if data.Name:
    			data.Name = msg
    			data.save()
    		else:
    			create = Voice.objects.create(Name=msg)
    	else:
    		create = Voice.objects.create(Name=msg)

    elif var == '1' and msg != '':
    	data.Gothram = msg
    	data.save()

    return redirect('/')


@login_required
def main(request):
	# month = date.today().month
	# year = date.today().year
	table1 = Donations.objects.all().order_by('-id')[:30]
	table2 = Expenses.objects.all().order_by('-id')[:30]

	Don = Donations.objects.all().exclude(Paid_Through='Due').aggregate(Sum('Amount'))['Amount__sum'] or 0
	hundi = Hundi.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	tDon = Don + hundi
	tDue = Donations.objects.filter(Paid_Through='Due').aggregate(Sum('Amount'))['Amount__sum'] or 0
	tDonCash = Donations.objects.filter(Paid_Through='Paid-Cash').aggregate(Sum('Amount'))['Amount__sum'] or 0
	tDonOnline= Donations.objects.filter(Paid_Through='Paid-Online').aggregate(Sum('Amount'))['Amount__sum'] or 0
	tExp = Expenses.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	tExpCash = Expenses.objects.filter(Paid_Through='Cash').aggregate(Sum('Amount'))['Amount__sum'] or 0
	tExpOnline = Expenses.objects.filter(Paid_Through='Online').aggregate(Sum('Amount'))['Amount__sum'] or 0

	Bal = tDon-tExp
	BalCash = tDonCash - tExpCash
	BalOnline = tDonOnline - tExpOnline

	dset = {'tDon':tDon, 'hundi':hundi, 'tDue':tDue, 'tDonCash':tDonCash, 'tDonOnline':tDonOnline, 'tExp':tExp, 'tExpCash':tExpCash, 'tExpOnline':tExpOnline, 'Bal':Bal, 'BalCash':BalCash, 'BalOnline':BalOnline}
	
	return render(request, 'index.html', {'table1': table1, 'table2': table2, 'dset':dset})


@login_required 
def donations_form(request, fnc, var, var1):
	if fnc != 'create' and fnc != 'dlt' and fnc!='copy' : #for update checking
		atnddata=get_object_or_404(Donations, id=var)
		if request.method ==  'POST':
			form = DonationsForm(request.POST, request.FILES, instance=atnddata)
			if form.is_valid():
				p = form.save()
				pid = p.id
				# messages.success(request, "Selected Donation Details Has Been Updated")
				# return render(request, 'donationsform.html')
				dt = Donations.objects.get(id=pid)
				return render(request, 'inv.html', {'dt': dt})				
			else:
				update="True"
				return render(request, 'donationsform.html', {'form': form, 'update':update, 'var1':var1})
		else:
			form = DonationsForm(instance=atnddata)
			update="True"
			return render(request, 'donationsform.html', {'form': form, 'update':update, 'var1':var1})

	elif fnc == 'dlt': #Delete
		atnddata=get_object_or_404(Donations, id=var)
		atnddata.delete()
		messages.success(request, "Selected Donation Details Has Been Deleted")
		return redirect('donations')

	if fnc=='copy':
		atnddata=get_object_or_404(Donations, id=var)

	if request.method ==  'POST': #Create
		form = DonationsForm(request.POST, request.FILES)
		if form.is_valid():
			# p = form.save(commit=False)
			p = form.save()
			pid = p.id
			pdate = p.Date
			if p.Date:
				td = p.Date
			else:
				td = date.today()
			
			if p.Issued_By:
				issued = p.Issued_By
			else:
				issued = request.user.first_name

			last_rec = Donations.objects.all().first()
			vc = Voice.objects.all().last()
			rec_no = str(td.month)+str(td.year)[-2:]+' '+str(p.id)
			updt = Donations.objects.filter(id=pid).update(Date=td, Receipt_No=rec_no, Donor_Name=vc.Name, Issued_By=issued, Gothram=vc.Gothram)
			form = DonationsForm()
			messages.success(request, "Donation Has Been Added")
			# return render(request, 'donationsform.html', {'form': form})
			dt = Donations.objects.get(id=pid)
			dlt = Voice.objects.all()
			dlt.delete()
			return render(request, 'inv.html', {'dt': dt})
		else:
			return render(request, 'donationsform.html', {'form': form})
	else:
		if fnc=='copy':
			form = DonationsForm(instance=atnddata)
			return render(request, 'donations.html', {'form': form})
		else:
			form = DonationsForm()
			return render(request, 'donationsform.html', {'form': form})

@login_required 
def donations_form1(request, fnc, var, var1):
	if fnc != 'create' and fnc != 'dlt' and fnc!='copy' : #for update checking
		atnddata=get_object_or_404(Donations, id=var)
		if request.method ==  'POST':
			form = DonationsForm(request.POST, request.FILES, instance=atnddata)
			if form.is_valid():
				p = form.save()
				pid = p.id
				# messages.success(request, "Selected Donation Details Has Been Updated")
				# return render(request, 'donationsform.html')
				dt = Donations.objects.get(id=pid)
				return render(request, 'inv.html', {'dt': dt})				
			else:
				update="True"
				return render(request, 'donationsform1.html', {'form': form, 'update':update, 'var1':var1})
		else:
			form = DonationsForm(instance=atnddata)
			update="True"
			return render(request, 'donationsform1.html', {'form': form, 'update':update, 'var1':var1})

	elif fnc == 'dlt': #Delete
		atnddata=get_object_or_404(Donations, id=var)
		atnddata.delete()
		messages.success(request, "Selected Donation Details Has Been Deleted")
		return redirect('donations')

	if fnc=='copy':
		atnddata=get_object_or_404(Donations, id=var)

	if request.method ==  'POST': #Create
		form = DonationsForm(request.POST, request.FILES)
		if form.is_valid():
			# p = form.save(commit=False)
			p = form.save()
			pid = p.id
			pdate = p.Date
			if p.Date:
				td = p.Date
			else:
				td = date.today()

			if p.Issued_By:
				issued = p.Issued_By
			else:
				issued = request.user.first_name

			last_rec = Donations.objects.all().first()
			# vc = Voice.objects.all().last()
			rec_no = str(td.month)+str(td.year)[-2:]+' '+str(p.id)
			updt = Donations.objects.filter(id=pid).update(Date=td, Receipt_No=rec_no, Issued_By=issued)
			form = DonationsForm()
			messages.success(request, "Donation Has Been Added")
			# return render(request, 'donationsform.html', {'form': form})
			dt = Donations.objects.get(id=pid)
			dlt = Voice.objects.all()
			dlt.delete()
			return render(request, 'inv.html', {'dt': dt})
		else:
			return render(request, 'donationsform1.html', {'form': form})
	else:
		if fnc=='copy':
			form = DonationsForm(instance=atnddata)
			return render(request, 'donations.html', {'form': form})
		else:
			form = DonationsForm()
			return render(request, 'donationsform1.html', {'form': form})

def donations(request):
	table = Donations.objects.all().order_by('-id')
	filter_data = DonationsFilter(request.GET, queryset=table)
	table = filter_data.qs
	
	tDonations=0
	tCash=0
	tOnline=0
	tDue=0
	for x in table:  
		if x.Paid_Through=='Paid-Cash':
			tCash = tCash + x.Amount
		elif x.Paid_Through=='Paid-Online':
			tOnline = tOnline + x.Amount
		else:
			tDue = tDue + x.Amount
		tDonations=tCash+tOnline

	tMonth = Donations.objects.filter(Date__gte=date.today()-timedelta(days=30), Date__lte=date.today()).exclude(Paid_Through='Due').aggregate(Sum('Amount'))['Amount__sum']


	donset = {'tDonations':tDonations, 'tDue':tDue, 'tCash':tCash, 'tOnline':tOnline, 'tMonth': tMonth}
	return render(request, 'donations.html', {'table': table, 'filter_data':filter_data, 'donset':donset})

@login_required
def expenses_form(request, fnc, var):
	if fnc != 'create' and fnc != 'dlt' and fnc!='copy' : #for update checking
		atnddata=get_object_or_404(Expenses, id=var)
		if request.method ==  'POST':
			form = ExpensesForm(request.POST, request.FILES, instance=atnddata)
			if form.is_valid():
				form.save()
				table = Expenses.objects.all().order_by('-Date')
				messages.success(request, "Selected Expenses Details Has Been Updated")
				return render(request, 'expenses.html', {'table': table})				
			else:
				update="True"
				return render(request, 'expensesform.html', {'form': form, 'update':update})
		else:
			form = ExpensesForm(instance=atnddata)
			update="True"
			return render(request, 'expensesform.html', {'form': form, 'update':update})

	elif fnc == 'dlt': #Delete
		atnddata=get_object_or_404(Expenses, id=var)
		atnddata.delete()
		messages.success(request, "Selected Expenses Details Has Been Deleted")
		return redirect('expns')

	if fnc=='copy':
		atnddata=get_object_or_404(Expenses, id=var)

	if request.method ==  'POST': #Create
		form = ExpensesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			form = ExpensesForm()
			messages.success(request, "Expenses Has Been Added")
			return render(request, 'expensesform.html', {'form': form})
		else:
			return render(request, 'expensesform.html', {'form': form})
	else:
		if fnc=='copy':
			form = ExpensesForm(instance=atnddata)
			return render(request, 'expenses.html', {'form': form})
		else:
			form = ExpensesForm()
			return render(request, 'expensesform.html', {'form': form})


def expenses(request):
	table = Expenses.objects.all().order_by('-Date')
	filter_data = ExpensesFilter(request.GET, queryset=table)
	table = filter_data.qs
	
	tExpenses=0
	for x in table:
		tExpenses=tExpenses+x.Amount
	tMonth = Expenses.objects.filter(Date__gte=date.today()-timedelta(days=30), Date__lte=date.today()).aggregate(Sum('Amount'))['Amount__sum']


	donset = {'tExpenses':tExpenses, 'tMonth': tMonth}
	return render(request, 'expenses.html', {'table': table, 'filter_data':filter_data, 'donset':donset})


@login_required
def staff_form(request, fnc, var):
	if fnc != 'create' and fnc != 'dlt' and fnc!='copy' : #for update checking
		atnddata=get_object_or_404(Staff, id=var)
		if request.method ==  'POST':
			form = StaffForm(request.POST, request.FILES, instance=atnddata)
			if form.is_valid():
				p = form.save(commit=False)
				form.save()
				table = Staff.objects.all()
				messages.success(request, "Selected Staff Details Has Been Updated")
				return redirect('stf')				
			else:
				update="True"
				return render(request, 'staffform.html', {'form': form, 'update':update})
		else:
			form = StaffForm(instance=atnddata)
			update="True"
			return render(request, 'staffform.html', {'form': form, 'update':update})

	elif fnc == 'dlt': #Delete
		atnddata=get_object_or_404(Staff, id=var)
		atnddata.delete()
		messages.success(request, "Selected Staff Details Has Been Deleted")
		return redirect('stf')

	if fnc=='copy':
		atnddata=get_object_or_404(Staff, id=var)

	if request.method ==  'POST': #Create
		form = StaffForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			form = StaffForm()
			messages.success(request, "Staff Details Has Been Added")
			return redirect('stf')
		else:
			return render(request, 'staffform.html', {'form': form})
	else:
		if fnc=='copy':
			form = StaffForm(instance=atnddata)
			return render(request, 'staff.html', {'form': form})
		else:
			form = StaffForm()
			return render(request, 'staffform.html', {'form': form})


def staff(request):
	table = Staff.objects.all()
	
	return render(request, 'Staff.html', {'table': table})

@login_required
def Cat_Form(request, fnc, var):
	if fnc != 'create' and fnc != 'dlt' and fnc!='copy' : #for update checking
		atnddata=get_object_or_404(DonationsCat, id=var)
		if request.method ==  'POST':
			form = DonationsCatForm(request.POST, request.FILES, instance=atnddata)
			if form.is_valid():
				p = form.save(commit=False)
				form.save()
				table = DonationsCat.objects.all()
				messages.success(request, "Selected Donation Category Details Has Been Updated")
				return redirect('cat')				
			else:
				update="True"
				return render(request, 'CatForm.html', {'form': form, 'update':update})
		else:
			form = DonationsCatForm(instance=atnddata)
			update="True"
			return render(request, 'CatForm.html', {'form': form, 'update':update})

	elif fnc == 'dlt': #Delete
		atnddata=get_object_or_404(DonationsCat, id=var)
		atnddata.delete()
		messages.success(request, "Selected Donation Category Details Has Been Deleted")
		return redirect('cat')

	if fnc=='copy':
		atnddata=get_object_or_404(Cat, id=var)

	if request.method ==  'POST': #Create
		form = DonationsCatForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			form = DonationsCatForm()
			messages.success(request, "Donation Category Details Has Been Added")
			return redirect('cat')
		else:
			return render(request, 'CatForm.html', {'form': form})
	else:
		if fnc=='copy':
			form = DonationsCatForm(instance=atnddata)
			return render(request, 'CatForm.html', {'form': form})
		else:
			form = DonationsCatForm()
			return render(request, 'CatForm.html', {'form': form})

def Cat(request):
	table = DonationsCat.objects.all()	
	return render(request, 'Cat.html', {'table': table})

@login_required
def Hundi_Form(request, fnc, var):
	if fnc != 'create' and fnc != 'dlt' and fnc!='copy' : #for update checking
		atnddata=get_object_or_404(Hundi, id=var)
		if request.method ==  'POST':
			form = HundiForm(request.POST, request.FILES, instance=atnddata)
			if form.is_valid():
				p = form.save(commit=False)
				form.save()
				table = Hundi.objects.all()
				messages.success(request, "Selected Hundi Details Has Been Updated")
				return redirect('hnd')				
			else:
				update="True"
				return render(request, 'HundiForm.html', {'form': form, 'update':update})
		else:
			form = HundiForm(instance=atnddata)
			update="True"
			return render(request, 'HundiForm.html', {'form': form, 'update':update})

	elif fnc == 'dlt': #Delete
		atnddata=get_object_or_404(Hundi, id=var)
		atnddata.delete()
		messages.success(request, "Selected Hundi Details Has Been Deleted")
		return redirect('hnd')

	if fnc=='copy':
		atnddata=get_object_or_404(Cat, id=var)

	if request.method ==  'POST': #Create
		form = HundiForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			form = HundiForm()
			messages.success(request, "Hundi Amount Has Been Added")
			return redirect('hnd')
		else:
			return render(request, 'HundiForm.html', {'form': form})
	else:
		if fnc=='copy':
			form = HundiForm(instance=atnddata)
			return render(request, 'HundiForm.html', {'form': form})
		else:
			form = HundiForm()
			return render(request, 'HundiForm.html', {'form': form})

def Hundee(request):
	table = Hundi.objects.all()
	tHundi = Hundi.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	return render(request, 'Hundi.html', {'table': table, 'tHundi':tHundi })

@login_required
def Salaries_Form(request, fnc, var):
	if fnc != 'create' and fnc != 'dlt' and fnc!='copy' : #for update checking
		atnddata=get_object_or_404(Salaries, id=var)
		if request.method ==  'POST':
			form = SalariesForm(request.POST, request.FILES, instance=atnddata)
			if form.is_valid():
				p = form.save()
				print(p.Paid_Through)
				create = Expenses.objects.create(Date=p.Date, Amount=p.Amount, Category='Salary', Towards='Salary', By=p.Name, Paid_Through=p.Paid_Through)
				messages.success(request, "Selected Salaries Details Has Been Updated")
				return redirect('sal')				
			else:
				update="True"
				return render(request, 'SalariesForm.html', {'form': form, 'update':update})
		else:
			form = SalariesForm(instance=atnddata)
			update="True"
			return render(request, 'SalariesForm.html', {'form': form, 'update':update})

	elif fnc == 'dlt': #Delete
		atnddata=get_object_or_404(Salaries, id=var)
		atnddata.delete()
		messages.success(request, "Selected Salaries Details Has Been Deleted")
		return redirect('sal')

	if fnc=='copy':
		atnddata=get_object_or_404(Cat, id=var)

	if request.method ==  'POST': #Create
		form = SalariesForm(request.POST, request.FILES)
		if form.is_valid():
			p = form.save()
			form = SalariesForm()
			messages.success(request, "Salaries Details Has Been Added")
			create = Expenses.objects.create(Date=p.Date, Amount=p.Amount, Category='Salary', By=p.Name, Paid_Through=p.Paid_Through)
			return redirect('sal')
		else:
			return render(request, 'SalariesForm.html', {'form': form})
	else:
		if fnc=='copy':
			form = SalariesForm(instance=atnddata)
			return render(request, 'SalariesForm.html', {'form': form})
		else:
			form = SalariesForm()
			return render(request, 'SalariesForm.html', {'form': form})

def salaries(request):
	table = Salaries.objects.all()	
	return render(request, 'Salaries.html', {'table': table})


@method_decorator(login_required, name='dispatch')
class ChartData(View):
	def get(self, request):	
		try:
			span = request.GET['req_date']
			
			if span=='1':
				span = date.today()

			table = Donations.objects.filter(Date__lte=span).order_by('Date')[:30]

			x1 = []
			y1 = []

			dt = []

			for x in table:
				x1.append(str(x.Date.strftime('%d %b')))
				dt.append(x.Date)
			x1 = list(dict.fromkeys(x1))
			dt = list(dict.fromkeys(dt))

			for p in dt:
				k = Donations.objects.filter(Date=p)
				amount = int(k.aggregate(Sum('Amount'))['Amount__sum']) or 0
				y1.append(amount)
				print(p)

			# dates = span


			return JsonResponse({'x1':x1, 'y1':y1})
		except Exception as e:
			return JsonResponse({"error":str(e)})

def spaa(request):
	p = Voice.objects.all().last()
	spa = p.Name
	if spa:
		print(spa)
	else:
		spa = 12345
	return JsonResponse({'spa':spa})
