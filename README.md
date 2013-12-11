#说明:
import salt.config
opts = salt.config.client_config('/etc/salt/master')
import salt.runner
rclient = salt.runner.RunnerClient(opts)
rclient.cmd('jobs.list_jobs', '')

分页
https://django-pagination.googlecode.com/files/django-pagination-1.0.5.tar.gz

两地代码重新合并提交

#转成json
mimetype="application/json"


date1 = datetime.datetime.now()
this_week_start_dt = date1-datetime.timedelta(days=date1.weekday())
this_week_end_dt = date1+datetime.timedelta(days=6-date1.weekday())