from django.core.mail import send_mail
from django.conf import settings
from django_cron import CronJobBase, Schedule
import requests
import time
from agent import process_incidents
from pymongo import MongoClient
import json


while True:
    process_incidents()  # Run the function
    time.sleep(10)  # Wait 10 seconds before running again



