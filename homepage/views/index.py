from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage.models import Completion_Record
from django.http import HttpResponseRedirect
from homepage.tasks import create_record
from datetime import datetime
import time

@view_function
def process_request(request):
    records = Completion_Record.objects.all()
    record = records.first()
    print(record.end_time)
    print(record.start_time)
    print(record.end_time - record.start_time)
    context = {
        'records': records,
    }
    return request.dmp.render('index.html', context)

@view_function
def celery_execution(request):
	create_record.delay(int(request.GET.get('num')))
	return HttpResponseRedirect('/')

@view_function
def http_execution(request):
	start_time = datetime.now()
	time.sleep(int(request.GET.get('num')))
	end_time = datetime.now()
	c = Completion_Record(start_time=start_time, end_time=end_time)
	c.save()
	return HttpResponseRedirect('/')