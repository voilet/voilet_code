#说明:
import salt.config
opts = salt.config.client_config('/etc/salt/master')
import salt.runner
rclient = salt.runner.RunnerClient(opts)
rclient.cmd('jobs.list_jobs', '')

