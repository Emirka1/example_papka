from core import *

def print_schedule(data):
        for i in data['data']:
                print(f"{i['date']} | {i['teacher_name']}")
        return None
