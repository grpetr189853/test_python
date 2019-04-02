from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render_to_response
from consolecommand import models
from datetime import datetime
import datetime
from django.db import connection
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import IntegerField

def search(request):
	date_start = request.GET.get('date_start', '')
	date_end = request.GET.get('date_end', '')
	if bool(date_start) & bool(date_end):
		qset = (
			Q(created_date__gte=datetime.datetime.strptime(date_start, '%m/%d/%Y')) &
			Q(created_date__lte=datetime.datetime.strptime(date_end, '%m/%d/%Y'))
		)

		results = models.Order.objects.filter(qset).distinct()

		items_count = models.OrderItems.objects.annotate(total_sum=Sum(Cast('product_price',IntegerField())*Cast('amount',IntegerField()))).first()

		items = models.OrderItems.objects.all()
	
		#print(items_count.query)
		queries = connection.queries
		total_queries = len(queries)
		print(items_count.total_sum)
	else:
		results = []
		items = []
		items_count = []
		total_queries = []
	return render_to_response("reportorder_template.html", {
		"results" : results,
		"items" : items,
		"items_count" : items_count,
		"date_start": date_start,
		"date_end": date_end,
		"total_queries": total_queries,		
	})