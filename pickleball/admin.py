from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'is_staff', 'first_name', 'last_name', 'active_player', 'date_joined', 'level', 'league_type', 'time_playing', 'phone_number')
    list_filter = ('active_player','league_type','date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'league_type')
    ordering = ('-active_player', 'date_joined')
    readonly_fields = ('date_joined',)

    # customize fieldsets in change user form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('level', 'active_player', 'league_type')}),
    )

    # customize fieldsets in create user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'active_player', 'is_staff', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_number', 'level'),
        }),
    )

    # all information is added to user upon signup, so take admin back to listview of users after creation
    def response_add(self, request, obj, post_url_continue=None):
        """
        Determines the HttpResponse for the add_view stage. It customizes the redirection after
        adding a new user.
        """
        opts = obj._meta
        
        if "_addanother" not in request.POST and "_continue" not in request.POST:
            post_url_continue = reverse('admin:%s_%s_changelist' % (opts.app_label, opts.model_name), current_app=self.admin_site.name)
        
        return HttpResponseRedirect(post_url_continue)

admin.site.register(CustomUser, CustomUserAdmin)


