from activities.models import Activity
import datetime
from django.core.mail import send_mail
from django.conf import settings
import time

def main():
    while(True):
        send_notif()
        print("executing")
        time.sleep(60)

def send_notif():
    try:
        time_threshold = datetime.now()
        print(time_threshold)
        activity_objs = Activity.objects.filter(time_start__date=time_threshold.date).filter(time_start__hour=time_threshold.hour).filter(time_start__minute=time_threshold__minute)

        print(activity_objs)
        for activity in activity_objs:
            subject = 'Activity Reminder!'
            message = "test"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [activity.users.email]
            print(recipient_list)
            send_mail(subject, message, email_from, recipient_list)

    except Exception as e:
        print(e)
