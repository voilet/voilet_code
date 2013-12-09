#说明:
import salt.config
opts = salt.config.client_config('/etc/salt/master')
import salt.runner
rclient = salt.runner.RunnerClient(opts)
rclient.cmd('jobs.list_jobs', '')

分页
https://django-pagination.googlecode.com/files/django-pagination-1.0.5.tar.gz