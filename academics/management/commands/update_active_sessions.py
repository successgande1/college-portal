# academic/management/commands/update_active_sessions.py
from django.core.management.base import BaseCommand
from academics.models import AcademicSession
from datetime import date

class Command(BaseCommand):
    help = 'Update the is_active field for Academic Sessions based on current date'

    def handle(self, *args, **kwargs):
        today = date.today()
        active_sessions = AcademicSession.objects.filter(start_date__lte=today, end_date__gte=today)

        for session in active_sessions:
            session.is_active = True
            session.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully activated AcademicSession: {session}'))
