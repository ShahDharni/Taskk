from celery import shared_task



@shared_task(bind=True)
def test_func(self):
    ## Performing operations
    for i in range(10):
        print(i)
