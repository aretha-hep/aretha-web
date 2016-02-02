from celery import shared_task

@shared_task
def submit_swarm(config):
    print "submitting swarm with config: {}".format(config)