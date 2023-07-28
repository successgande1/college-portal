from django.core.management.base import BaseCommand
from academics.models import Semester
from datetime import date

class Command(BaseCommand):
    help = 'Update the is_active field for Semesters based on current date'

    def handle(self, *args, **kwargs):
        today = date.today()
        active_semesters = Semester.objects.filter(start_date__lte=today, end_date__gte=today)

        for semester in active_semesters:
            semester.is_active = True
            semester.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully activated Semester: {semester}'))
