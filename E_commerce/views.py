from django.http import HttpResponse
from utils.insert_dummy_data import insert_dummy_data

def insert_dummy_data_view(request):
    insert_dummy_data()
    return HttpResponse("Dummy data inserted successfully!")
