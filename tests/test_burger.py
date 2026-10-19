import pytest


class TestBurger:
    def test_new_burger_is_empty(self, burger):
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns_replaces_bun(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_ingredient_appends(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.ingredients == [sauce, filling]

    @pytest.mark.parametrize("index, expected", [(0, "filling"), (1, "sauce")])
    def test_remove_ingredient_by_index(self, burger, sauce, filling, index, expected):
        burger.ingredients = [sauce, filling]
        burger.remove_ingredient(index)
        assert burger.ingredients == [filling if expected == "filling" else sauce]

    @pytest.mark.parametrize("from_index,to_index,expected", [
        (0, 2, ["filling", "extra", "sauce"]),
        (2, 0, ["extra", "sauce", "filling"]),
        (1, 1, ["sauce", "filling", "extra"]),
    ])
    def test_move_ingredient(self, burger, sauce, filling, from_index, to_index, expected):
        extra = object()
        burger.ingredients = [sauce, filling, extra]
        burger.move_ingredient(from_index, to_index)
        names = ["sauce" if x is sauce else "filling" if x is filling else "extra"
                 for x in burger.ingredients]
        assert names == expected

    @pytest.mark.parametrize("add_sauce, add_filling, expected", [
        (False, False, 201.0),
        (True, False, 226.25),
        (True, True, 296.25),
    ])
    def test_get_price(self, burger, bun, sauce, filling, add_sauce, add_filling, expected):
        burger.set_buns(bun)
        if add_sauce:
            burger.add_ingredient(sauce)
        if add_filling:
            burger.add_ingredient(filling)
        assert burger.get_price() == pytest.approx(expected)

    @pytest.mark.parametrize("with_ingredients, expected", [
        (False, "(==== Краторная булка ====)\n(==== Краторная булка ====)\n\nPrice: 201.0"),
        (True, "(==== Краторная булка ====)\n= sauce Космо-соус =\n= filling Котлета =\n(==== Краторная булка ====)\n\nPrice: 296.25"),
    ])
    def test_get_receipt(self, burger, bun, sauce, filling, with_ingredients, expected):
        burger.set_buns(bun)
        if with_ingredients:
            burger.add_ingredient(sauce)
            burger.add_ingredient(filling)
        assert burger.get_receipt() == expected
        assert bun.get_name.called
