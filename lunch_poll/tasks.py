""" Task to run aysnc with celery"""

from celery.decorators import task
from celery.utils.log import get_task_logger

from lunch_poll.models import Menu

LOGGER = get_task_logger(__name__)


@task(name="send_slack_task")
def send_slack_task(menu, host):
    """sends slack message with lunch options"""
    LOGGER.info("Sent slack reminder")
    menu = Menu.objects.get(pk=menu)

    return menu.send_slack(host)
