from fabric.api import *
from traceback import print_exc

def archive():
  local("zip -r powertalk css js images *.html")

@task
@hosts('deone@deone.webfactional.com')
def deploy():
  archive()
  try:
    local("echo 'Copying script archive to host...'")
    put("powertalk.zip", "powertalk.zip")

    local("echo 'Deploying site...'")
    with cd("webapps/powertalk"):
      run("unzip -o ~/powertalk.zip")
  except Exception:
    print_exc()
  finally:
    local("echo 'Cleaning up litter...'")
    local("rm powertalk.zip")
