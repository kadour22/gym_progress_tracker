from django.db import models 
from django.contrib.auth.models import User

class Program(models.Model) :

    class Gender(models.TextChoices) :
        MAN = "man", "man"
        WOMAN = "woman", "woman"

    class Goal(models.TextChoices) :
        LOSS_FAT = "lossfat", "lossfat"
        BULKING  = "bulk", "bulk"
        CUTTING  = "cut", "cut"

    class DURATION(models.TextChoices) :
        one_month   = "1 Month", "1 Month"
        two_month   = "2 Month", "2 Month"
        three_month = "3 Month", "3 Month"
        four_month  = "4 Month", "4 Month"
        five_month  = "5 Month", "5 Month"

    class DAY_PER_WEEK(models.TextChoices) :
        one_day   = "1 day", "1 day"
        two_day   = "2 day", "2 day"
        three_day = "3 day", "3 day"
        four_day  = "4 day", "4 day"
        five_day  = "5 day", "5 day"

    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='program')
    age         = models.PositiveIntegerField()
    gender      = models.CharField(max_length=30, choices=Gender.choices, default=Gender.MAN)
    progam_goal = models.CharField(max_length=30, choices=Goal.choices, default=Goal.LOSS_FAT)
    durations   = models.CharField(max_length=30, choices=DURATION.choices, default=DURATION.two_month)
    training    = models.CharField(max_length=25, choices=DAY_PER_WEEK.choices, default=DAY_PER_WEEK.three_day)
    height      = models.CharField(max_length=3)
    weight      = models.PositiveIntegerField(null=True)


    # dates(Optional)
    start_date  = models.DateField(null=True)
    end_date    = models.DateField(null=True)

    def __str_(self) :
        return f"{self.user.username} program"

class WorkoutDayLog(models.Model):
    program   = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="logs")
    date      = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('program', 'date')

    def __str__(self):
        return f"{self.program.user.username} - {self.date} - {self.completed}"

class ProgramData(models.Model) :
    program   = models.ForeignKey(Program, on_delete = models.CASCADE, related_name  = "prgram_data")
    data      = models.JSONField()
    createdAt = models.DateTimeField(auto_now_add=True)

    