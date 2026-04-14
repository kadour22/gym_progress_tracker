from django.utils import timezone

def calculate_program_progress(program):
    if not program.start_date or not program.end_date:
        return 0

    today = timezone.now().date()

    total_days = (program.end_date - program.start_date).days
    passed_days = (today - program.start_date).days

    if total_days <= 0:
        return 0

    return min(100, int((passed_days / total_days) * 100))

def calculate_data_activity(program):
    total_logs = program.prgram_data.count()

    # expected logs = days since start
    if not program.start_date:
        return 0

    days_since_start = (timezone.now().date() - program.start_date).days

    if days_since_start == 0:
        return 0

    return min(100, int((total_logs / days_since_start) * 100))