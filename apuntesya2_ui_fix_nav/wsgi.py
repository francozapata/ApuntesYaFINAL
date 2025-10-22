# WSGI entry point for Render/WSGI servers
# Adjust the import below if your app factory/module path is different.
# For ApuntesYa (version estable), the app lives at apuntesya2.app:app
from apuntesya2.app import app  # noqa: F401  # exposes "app" as WSGI callable
