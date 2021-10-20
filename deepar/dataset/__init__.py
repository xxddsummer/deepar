from abc import ABC
from time_series import *


class Dataset(ABC):
    def __init__(self):
        super().__init__()

    def next_batch(self, **kwargs):
        pass
