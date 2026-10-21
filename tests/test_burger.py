import pytest


class TestBurger:
    def test_set_buns_updates_price(self, burger, bun):
        burger.set_buns(bun)
        assert burger.get_price() == pytest.approx(201.0)

    def test_set_buns_replaces_previous_bun(self, burger, bun, second_bun):
        burger.set_buns(bun)
        burger.set_buns(second_bun)
        assert burger.get_price() == pytest.approx(160.0)

    def test_add_sauce_updates_price(self, burger, bun, sauce):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        assert burger.get_price() == pytest.approx(226.25)

    def test_add_filling_updates_receipt(self, burger, bun, filling):
        burger.set_buns(bun)
        burger.add_ingredient(filling)
        assert "= filling Котлета =" in burger.get_receipt()

    @pytest.mark.parametrize(
        "index, expected_price",
        [(0, 271.0), (1, 226.25)],
        ids=["remove_sauce", "remove_filling"],
    )
    def test_remove_ingredient(self, burger, bun, sauce, filling, index, expected_price):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.remove_ingredient(index)
        assert burger.get_price() == pytest.approx(expected_price)

    @pytest.mark.parametrize(
        "from_index, to_index, expected",
        [
            (0, 2, ["= filling Котлета =", "= sauce Дополнительный соус =", "= sauce Космо-соус ="]),
            (2, 0, ["= sauce Дополнительный соус =", "= sauce Космо-соус =", "= filling Котлета ="]),
            (1, 1, ["= sauce Космо-соус =", "= filling Котлета =", "= sauce Дополнительный соус ="]),
        ],
        ids=["first_to_last", "last_to_first", "same_position"],
    )
    def test_move_ingredient(self, burger, bun, sauce, filling, extra_sauce,
                             from_index, to_index, expected):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.add_ingredient(extra_sauce)
        burger.move_ingredient(from_index, to_index)
        assert burger.get_receipt().splitlines()[1:4] == expected

    def test_get_price_without_ingredients(self, burger, bun):
        burger.set_buns(bun)
        assert burger.get_price() == pytest.approx(201.0)

    def test_get_price_with_sauce(self, burger, bun, sauce):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        assert burger.get_price() == pytest.approx(226.25)

    def test_get_price_with_sauce_and_filling(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.get_price() == pytest.approx(296.25)

    def test_get_receipt_without_ingredients(self, burger, bun):
        burger.set_buns(bun)
        assert burger.get_receipt() == (
            "(==== Краторная булка ====)\n"
            "(==== Краторная булка ====)\n\n"
            "Price: 201.0"
        )

    def test_get_receipt_with_ingredients(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.get_receipt() == (
            "(==== Краторная булка ====)\n"
            "= sauce Космо-соус =\n"
            "= filling Котлета =\n"
            "(==== Краторная булка ====)\n\n"
            "Price: 296.25"
        )
