from unittest.mock import Mock
import pytest


@pytest.fixture
def burger():
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture
def bun():
    return Mock(get_name=Mock(return_value="Краторная булка"),
                get_price=Mock(return_value=100.5))


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
