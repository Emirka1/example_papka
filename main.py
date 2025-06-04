from core import *
from interface import *

Bot = MyStat("zulmu_aa95","Mjm74#ng")
schedule = Bot.get_schedule(week=True,date="2025-05-20")

print_schedule(schedule)
