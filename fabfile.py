from fabric.api import local
from fabric.decorators import task


@task
def install(requirements_env="dev"):
    """
    Install required packages
    """
    local("pip install -r requirements/%s.txt" % requirements_env)


@task
def run():
    local("./manage.py runserver")


@task
def pycodestyle():
    """
    check the project for PEP8 compliance using `pycodestyle`
    """
    local("pycodestyle .")


@task
def tag_version(version):
    """
    Tag new version
    """
    local("git tag %s" % version)
    local("git push origin %s" % version)


@task
def fetch_version(version):
    """
    Fetch git version
    """
    local("wget https://codeload.github.com/russellyue/blog/tar.gz/%s" %
          version)


@task
def test():
    """
    Run test
    """
    local("./manage.py test")
