from celery import shared_task
import time
from homepage.models import Completion_Record
from datetime import datetime

@shared_task
def create_record(num):
	start_time = datetime.now()
	time.sleep(num)
	end_time = datetime.now()
	c = Completion_Record(start_time=start_time, end_time=end_time)
	c.save()
	