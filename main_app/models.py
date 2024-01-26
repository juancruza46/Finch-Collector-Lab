from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    description = models.TextField(max_length = 250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
MEALS = (
    # this is a tuple with multiple tuples
    # each of these is called a 2-tuple
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Feeding(models.Model):
    # our model attributes go here
    date = models.DateField()
    # B-reakfast
    # L-unch
    # D-inner
    meal = models.CharField(
        max_length=1,
        # add the custom 'choices' field option
        # this is what will create our dropdown menu
        choices=MEALS,
        # set the default choice, to be 'B'
        default=MEALS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"