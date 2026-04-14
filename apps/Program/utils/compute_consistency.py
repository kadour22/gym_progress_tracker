from django.utils import timezone

def get_days_per_week(training):
    return int(training.split()[0])

def get_duration_weeks(duration):
    months = int(duration.split()[0])  
    return months * 4


def calculate_consistency(program):
    days_per_week = get_days_per_week(program.training)
    total_weeks = get_duration_weeks(program.durations)

    expected_workouts = days_per_week * total_weeks

    completed_workouts = program.logs.filter(completed=True).count()

    if expected_workouts == 0:
        return 0

    return int((completed_workouts / expected_workouts) * 100)