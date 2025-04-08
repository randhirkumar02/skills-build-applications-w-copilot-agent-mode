from django.core.management.base import BaseCommand
from octofit_tracker.test_data import get_test_data
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Get test data
        data = get_test_data()

        # Populate users
        users = []
        for user_data in data['users']:
            user = User(
                _id=user_data['_id'],
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )
            user.save()
            users.append(user)

        # Populate teams
        for team_data in data['teams']:
            team = Team(
                _id=team_data['_id'],
                name=team_data['name']
            )
            team.save()

        # Populate activities
        for activity_data in data['activities']:
            activity = Activity(
                _id=activity_data['_id'],
                user=None,  # Assign users later if needed
                activity_type=activity_data['activity_type'],
                duration=activity_data['duration']
            )
            activity.save()

        # Populate leaderboard
        for leaderboard_data in data['leaderboard']:
            leaderboard = Leaderboard(
                _id=leaderboard_data['_id'],
                user=None,  # Assign users later if needed
                score=leaderboard_data['score']
            )
            leaderboard.save()

        # Populate workouts
        for workout_data in data['workouts']:
            workout = Workout(
                _id=workout_data['_id'],
                name=workout_data['name'],
                description=workout_data['description']
            )
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
