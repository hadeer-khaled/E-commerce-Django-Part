# products/views.py

from django.http import HttpResponse
from utils.insert_dummy_data import insert_dummy_data

def insert_dummy_data_view(request):
    # Call the insert_dummy_data function
    insert_dummy_data()
    return HttpResponse("Dummy data inserted successfully!")
