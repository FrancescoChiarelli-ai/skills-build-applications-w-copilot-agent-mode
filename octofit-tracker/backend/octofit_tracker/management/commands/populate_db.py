from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create users (superheroes)
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Iron Man', type='run', duration=30, date='2025-10-20'),
            Activity(user='Captain America', type='cycle', duration=45, date='2025-10-21'),
            Activity(user='Spider-Man', type='swim', duration=25, date='2025-10-22'),
            Activity(user='Batman', type='run', duration=40, date='2025-10-20'),
            Activity(user='Superman', type='cycle', duration=60, date='2025-10-21'),
            Activity(user='Wonder Woman', type='swim', duration=35, date='2025-10-22'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=100, rank=1)
        Leaderboard.objects.create(team='dc', points=90, rank=2)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body strength', difficulty='easy'),
            Workout(name='Squats', description='Lower body strength', difficulty='medium'),
            Workout(name='Plank', description='Core strength', difficulty='hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
