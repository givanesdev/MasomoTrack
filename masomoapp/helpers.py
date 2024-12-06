# masomoapp/helpers.py
from django.http import HttpResponseForbidden
from masomoapp.models import Member

def check_role(user, allowed_roles):
    """
    Helper function to check if the user's role is allowed.
    """
    if not user.is_authenticated:  # Handle anonymous users
        return False  # Deny access for anonymous users

    try:
        member = Member.objects.get(email=user.email)
        return member.role in allowed_roles
    except Member.DoesNotExist:
        return False  # Deny access if no Member entry exists
