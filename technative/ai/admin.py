from django.contrib import admin
from .models import AIContext
from teams.models import TeamMember, Team


@admin.register(AIContext)
class AIContextAdmin(admin.ModelAdmin):
    list_display = ["team", "context"]
    list_filter = ["team"]

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        """Filter to only show AI contexts for the user's team"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        try:
            team_member = TeamMember.objects.get(user=request.user)
            return qs.filter(team=team_member.team)
        except TeamMember.DoesNotExist:
            return qs.none()

    def has_change_permission(self, request, obj=None):
        """Only allow editing if user belongs to the team"""
        if request.user.is_superuser:
            return True

        if obj is None:
            return True

        try:
            team_member = TeamMember.objects.get(user=request.user)
            return obj.team == team_member.team
        except TeamMember.DoesNotExist:
            return False

    def has_view_permission(self, request, obj=None):
        """Only allow viewing if user belongs to the team"""
        if request.user.is_superuser:
            return True

        if obj is None:
            return True

        try:
            team_member = TeamMember.objects.get(user=request.user)
            return obj.team == team_member.team
        except TeamMember.DoesNotExist:
            return False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Restrict team field to user's team only"""
        if db_field.name == "team" and not request.user.is_superuser:
            try:
                team_member = TeamMember.objects.get(user=request.user)
                kwargs["queryset"] = Team.objects.filter(id=team_member.team.id)
            except TeamMember.DoesNotExist:
                kwargs["queryset"] = Team.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
