from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    return Mock(get_name=Mock(return_value="Краторная булка"),
                get_price=Mock(return_value=100.5))


@pytest.fixture
def second_bun():
    return Mock(get_name=Mock(return_value="Другая булка"),
                get_price=Mock(return_value=80.0))


@pytest.fixture
def sauce():
    return Mock(get_name=Mock(return_value="Космо-соус"),
                get_type=Mock(return_value="SAUCE"),
                get_price=Mock(return_value=25.25))


@pytest.fixture
def filling():
    return Mock(get_name=Mock(return_value="Котлета"),
                get_type=Mock(return_value="FILLING"),
                get_price=Mock(return_value=70.0))


@pytest.fixture
def extra_sauce():
    return Mock(get_name=Mock(return_value="Дополнительный соус"),
                get_type=Mock(return_value="SAUCE"),
                get_price=Mock(return_value=11.0))
