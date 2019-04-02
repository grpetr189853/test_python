from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render_to_response
from consolecommand import models
from datetime import datetime
import datetime
from django.db.models import Count
from django.db import connection

def top_100(request):
	items = models.OrderItems.objects.all().annotate(product_name_=Count('product_name')).order_by('amount')[:100]#values('product_name').annotate(product_name_=Count('product_name'))#.values('product_name','order_id','product_price','order_id').order_by('amount')

	print(items.query)
	total_count = 0

	queries = connection.queries
	total_queries = len(queries)
	return render_to_response("reporttop100_template.html", {
		"items" : items,
		"total_queries": total_queries,
	})