from django.contrib import admin
from .models import Product
from teams.models import TeamMember, Team


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "team", "price", "stars", "created_date"]
    list_filter = ["team", "stars", "created_date"]
    search_fields = ["title", "description"]

    def get_queryset(self, request):
        """Filter to only show products for the user's team"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        try:
            team_member = TeamMember.objects.get(user=request.user)
            return qs.filter(team=team_member.team)
        except TeamMember.DoesNotExist:
            return qs.none()

    def has_add_permission(self, request):
        """Allow adding products only for user's team"""
        if request.user.is_superuser:
            return True

        try:
            TeamMember.objects.get(user=request.user)
            return True
        except TeamMember.DoesNotExist:
            return False

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

    def has_delete_permission(self, request, obj=None):
        """Only allow deleting if user belongs to the team"""
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
