class Settings(object):
    """A class to store all settings."""
    
    def __init__(self):
        """Initialize the game's settings."""

        # Screen setings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

