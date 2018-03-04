from . import common

from fabric.state import env
from fabric.decorators import task

env.repository = "https://github.com/bekbossyn/django_project.git"
env.repo_name = "django_project"


@task
def telecom():
    env.user = "dev"
    env.password = "root"
    env.hosts = ["185.22.67.213"]


@task
def ocean():
    env.user = "root"
    env.password = "Truesight7"
    env.hosts = ["128.199.61.232"]
