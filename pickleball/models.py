from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class CustomUser(AbstractUser):
    
    # player phone number
    phone_number = models.CharField(max_length=15, blank=True)

    # player levels
    PLAYER_LEVELS = (
        ('beginner', 'Beginner'),
        ('advanced_beginner', 'Advanced Beginner'),
        ('intermediate', 'Intermediate'),
        ('high_intermediate', 'High Intermediate'),
        ('advanced', 'Advanced'),
        ('high_advanced', 'High Advanced'),
    )
    
    # default level is beginner
    level = models.CharField(
        max_length=20,
        choices=PLAYER_LEVELS,
        default='Beginner'
    )

    is_active = models.BooleanField(default=True)

    # use logic the 3 columns for logic to determine if player is active_player or inactive_player (waitlist)
    # (a) if player active_player, and date_joined before deadline date -> player remains as an active player
    # (b) if player active_player, and date_joined after deadline date -> player is made to be in-active player (waitlist)
    # (c) if player in-active_player -> player is made in-active player (waitlist) regardless of the date joined
    active_player = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateField(null=True, blank=True)
    
    # setting the type of league someone plays in
    LEAGUE_TYPES = (
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        # Add more choices here if needed
    )

    league_type = models.CharField(
        max_length=10,
        choices=LEAGUE_TYPES,
        default='morning',
    )

    time_playing = models.CharField(max_length=50, null=True, blank=True)  # CharField for time range

    def save(self, *args, **kwargs):
        # Evening conditions
        if self.league_type == 'evening':
            if self.level in ['advanced_beginner', 'beginner']:
                self.time_playing = '6:00pm-7:15pm'
            elif self.level in ['intermediate', 'high_intermediate']:
                self.time_playing = '7:15pm-8:30pm'
            elif self.level in ['advanced', 'high_advanced']:
                self.time_playing = '8:30pm-9:45pm'

        # Morning conditions
        elif self.league_type == 'morning':
            if self.level in ['advanced_beginner', 'beginner']:
                self.time_playing = '1:30pm-2:45pm'
            elif self.level in ['intermediate', 'high_intermediate']:
                self.time_playing = '2:45pm-4:00pm'

        super(CustomUser, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username
        return full_name
    


        


