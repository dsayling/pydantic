from collections.abc import Callable as CollectionsCallable
from typing import Callable

import pytest

from pydantic import BaseModel, ValidationError

collection_callable_types = [Callable, Callable[[int], int], CollectionsCallable, CollectionsCallable[[int], int]]


@pytest.mark.parametrize('annotation', collection_callable_types)
def test_callable(annotation):
    class Model(BaseModel):
        callback: annotation

    m = Model(callback=lambda x: x)
    assert callable(m.callback)


@pytest.mark.parametrize('annotation', collection_callable_types)
def test_non_callable(annotation):
    class Model(BaseModel):
        callback: annotation

    with pytest.raises(ValidationError):
        Model(callback=1)
