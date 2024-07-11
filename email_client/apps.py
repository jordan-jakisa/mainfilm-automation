import schedule
from django.apps import AppConfig


def start_scheduler():
    import threading
    import time
    from .email_utility import check_email
    def run_scheduler():
        schedule.every(5).seconds.do(check_email)
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_scheduler)
    thread.daemon = True
    thread.start()


class EmailClientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_client'

    def ready(self):
        start_scheduler()
