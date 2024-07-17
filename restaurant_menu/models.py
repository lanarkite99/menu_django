from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE=(("starters","Starters"),("salads","Salads"),
           ("main_course","Main Course"),("desserts","Desserts"))

STATUS=((0,"Unavailable"),
        (1,"Available"))

class Menu(models.Model):
    menu_type=models.CharField(max_length=200,choices=MEAL_TYPE)
    meal=models.CharField(max_length=1000, unique=True)
    description=models.CharField(max_length=2000)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    author=models.ForeignKey(User,on_delete=models.PROTECT)
    status=models.IntegerField(STATUS,default=0)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal

