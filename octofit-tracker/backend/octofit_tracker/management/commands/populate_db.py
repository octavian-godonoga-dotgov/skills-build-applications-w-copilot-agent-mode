from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name="Marvel", description="Marvel superheroes")
        dc = Team.objects.create(name="DC", description="DC superheroes")

        # Create users
        ironman = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=marvel, is_superhero=True)
        hulk = User.objects.create(name="Hulk", email="hulk@marvel.com", team=marvel, is_superhero=True)
        superman = User.objects.create(name="Superman", email="superman@dc.com", team=dc, is_superhero=True)
        batman = User.objects.create(name="Batman", email="batman@dc.com", team=dc, is_superhero=True)

        # Create workouts
        pushups = Workout.objects.create(name="Pushups", description="Upper body", difficulty="Easy")
        running = Workout.objects.create(name="Running", description="Cardio", difficulty="Medium")
        yoga = Workout.objects.create(name="Yoga", description="Flexibility", difficulty="Easy")

        # Create activities
        Activity.objects.create(user=ironman, workout=pushups, duration_minutes=20, calories_burned=200)
        Activity.objects.create(user=hulk, workout=running, duration_minutes=30, calories_burned=400)
        Activity.objects.create(user=superman, workout=yoga, duration_minutes=40, calories_burned=150)
        Activity.objects.create(user=batman, workout=pushups, duration_minutes=25, calories_burned=220)

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=500, rank=1)
        Leaderboard.objects.create(user=hulk, score=450, rank=2)
        Leaderboard.objects.create(user=superman, score=400, rank=3)
        Leaderboard.objects.create(user=batman, score=350, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
