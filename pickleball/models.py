from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    # player phone number
    phone_number = models.CharField(max_length=15, blank=True)

    # player levels
    PLAYER_LEVELS = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    
    # default level is beginner
    level = models.CharField(
        max_length=12,
        choices=PLAYER_LEVELS,
        default='Beginner'
    )

    is_active = models.BooleanField(default=True)

    # use logic the 3 columns for logic to determine if player is active_player or inactive_player (waitlist)
    # (a) if player active_player, and date_joined before deadline date -> player remains as an active player
    # (b) if player in-active_player -> player is made in-active player regardless of the date joined
    active_player = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateField(null=True, blank=True)

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username
        return full_name
    


        


