from __future__ import absolute_import
from celery import Celery
from celery.schedules import crontab

app = Celery('telegram',
             broker='redis://0.0.0.0:6379/0',
             include=['main'])


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(seconds='*/5'),
        add(),
    )


@app.task
def add():
    print('works')


if __name__ == '__main__':
    app.start()