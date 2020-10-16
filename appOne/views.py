from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime


def index(request):
	 
	if 'your_gold' in request.session:
		request.session['your_gold'] = request.session['your_gold']
		request.session['activities'] = request.session['activities']
		request.session['activitieslog']='\n'.join(request.session['activities'])
		
	else:
		request.session['your_gold'] = 0
		request.session['activities'] = []
		request.session['activitieslog']='\n'.join(request.session['activities'])
		

	



	return render(request, "index.html")

def process_gold(request):
		
		context = {
		
		'time': strftime('%Y/%m/%d %I:%M:%S %p', gmtime())
	}
		farm_gold = random.randint(10,20)
		cave_gold = random.randint(5,10)
		house_gold = random.randint(2,5)
		casino_gold = random.randint(-50,50)
		
		
		if request.POST['property'] == 'farm':
			request.session['your_gold'] += farm_gold
			request.session['activities'] = [('<p class=positive> Earned ' + str(farm_gold) + ' gold from farm! </p>') + context['time']] + request.session['activities']
			
			
		if request.POST['property'] == 'cave':
			request.session['your_gold'] += cave_gold
			request.session['activities'] = [('<p class=positive> Earned ' + str(cave_gold) + ' gold from cave! </p>') + context['time']] + request.session['activities']
			
		if request.POST['property'] == 'house':
			request.session['your_gold'] += house_gold
			request.session['activities'] = [('<p class=positive> Earned ' + str(house_gold) + ' gold from house! </p>') + context['time']] + request.session['activities']
			
		if request.POST['property'] == 'casino':
			if casino_gold > 0:
				request.session['your_gold'] += casino_gold
				request.session['activities'] = [('<p class=positive> Won ' + str(casino_gold) + ' gold from the casino! </p>') + context['time']] + request.session['activities']
				
			if casino_gold < 0:
				request.session['your_gold'] += casino_gold
				request.session['activities'] = [('<p class=negative> Lost ' + str(casino_gold) + ' at the casino  </p> ') + context['time']] + request.session['activities']
				
		print(request.session['activities'])


		return redirect('/', context)
