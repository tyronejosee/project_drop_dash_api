"""Services for Blogs App."""

from rest_framework import serializers
from .models import PostReport
from .choices import PriorityChoices


class PostService:
    """
    Service for Post model.
    """

    @staticmethod
    def validate_report(post, user):
        """Validate if the user has already reported the post."""
        if PostReport.objects.filter(post_id=post, user_id=user).exists():
            raise serializers.ValidationError("You have already reported this post.")

    @staticmethod
    def update_post_points(post):
        """Update the points of the post and set its availability."""
        post.points = post.points - 1
        if post.points <= 5:
            post.is_available = False
        post.save()

    @staticmethod
    def determine_priority(post):
        """Determine the priority for the report based on post points."""
        if post.points <= 25:
            return PriorityChoices.URGENT
        elif post.points <= 50:
            return PriorityChoices.HIGH
        elif post.points <= 75:
            return PriorityChoices.MEDIUM
        else:
            return PriorityChoices.LOW

    @staticmethod
    def create_report(serializer, post, user):
        """Create a new report for the post."""
        priority = PostService.determine_priority(post)
        serializer.save(user_id=user, post_id=post, priority=priority)
