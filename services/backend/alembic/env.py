from app.core.config import settings
from app.models import *  # Import your models here

# Update the config with your DB URL
config.set_main_option("sqlalchemy.url", settings.DB_URL)