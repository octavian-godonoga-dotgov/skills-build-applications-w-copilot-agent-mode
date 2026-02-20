from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name="Marvel", description="Marvel superheroes")
        self.assertEqual(str(team), "Marvel")

    def test_user_create(self):
        team = Team.objects.create(name="DC", description="DC superheroes")
        user = User.objects.create(name="Superman", email="superman@dc.com", team=team, is_superhero=True)
        self.assertEqual(str(user), "Superman")

    def test_workout_create(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body", difficulty="Easy")
        self.assertEqual(str(workout), "Pushups")

    def test_activity_create(self):
        team = Team.objects.create(name="Marvel")
        user = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=team)
        workout = Workout.objects.create(name="Running", description="Cardio", difficulty="Medium")
        activity = Activity.objects.create(user=user, workout=workout, duration_minutes=30, calories_burned=300)
        self.assertEqual(activity.user.name, "Iron Man")

    def test_leaderboard_create(self):
        team = Team.objects.create(name="Marvel")
        user = User.objects.create(name="Hulk", email="hulk@marvel.com", team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
