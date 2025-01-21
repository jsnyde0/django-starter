from celery import shared_task


@shared_task
def simple_print_task():
    print("This print represents a simple background task with Celery.")
