from fabric.decorators import task
from fabric.operations import sudo, run
from fabric.state import env


@task
def git_pull():
    """
    Updates the repository
    """
    run("cd ../home/django/django_project && git pull origin master")


@task
def celery_logs():
    """
    Updates the repository
    """
    sudo("tail -f /var/log/celery/django_project.log")


@task
def update_supervisor():
    # sudo("cp ~/{}/configs/supervisor/celery.conf /etc/supervisor/conf.d".format(env.repo_name))
    sudo("supervisorctl reread; supervisorctl restart celery; supervisorctl restart celerybeat; supervisorctl restart flower; supervisorctl update; supervisorctl status celery")


@task
def update():
    """
    Restarts server
    """
    # run("cd /home/dev/pillowz_backend/ && . ./run.sh")
    sudo("systemctl restart gunicorn")
    sudo("systemctl restart nginx")
    update_supervisor()
