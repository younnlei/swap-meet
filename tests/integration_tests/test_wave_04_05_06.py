import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
#@pytest.mark.integration_test
def test_integration_wave_04_05_06():
    camila = Vendor()
    valentina = Vendor()

    item_clothing1 = Clothing(condition=1.0, id=123, fabric="Geometric Pattern")
    item_clothing2 = Clothing(condition=2.0, id=321)
    item_electronics1 = Electronics(condition=1.0, id=456)
    item_electronics2 = Electronics(condition=2.0, id=654, type="Kitchen Appliance")
    item_decor1 = Decor(condition=1.0, id=789)
    item_decor2 = Decor(condition=2.0, id=987, width=4, length=2)

    camila.add(item_electronics1)
    camila.add(item_clothing1)
    camila.add(item_clothing2)

    valentina.add(item_electronics2)
    valentina.add(item_decor1)
    valentina.add(item_decor2)


    # swap first item
    result = camila.swap_first_item(valentina)

    assert result
    assert len(camila.inventory) == 3
    assert item_electronics2 in camila.inventory
    assert item_clothing1 in camila.inventory
    assert item_clothing2 in camila.inventory

    assert len(valentina.inventory) == 3
    assert item_electronics1 in valentina.inventory
    assert item_decor1 in valentina.inventory
    assert item_decor2 in valentina.inventory

    # get item by category, truthy
    items = camila.get_by_category("Electronics")
    assert len(items) == 1
    assert item_electronics2 in items

    # get item by category, empty list
    items = valentina.get_by_category("Clothing")
    assert len(items) == 0

    # swap_best_category - falsy
    result = camila.swap_best_by_category(valentina, "Clothing", "Decor")

    assert not result
    assert len(camila.inventory) == 3
    assert item_electronics2 in camila.inventory
    assert item_clothing1 in camila.inventory
    assert item_clothing2 in camila.inventory

    assert len(valentina.inventory) == 3
    assert item_electronics1 in valentina.inventory
    assert item_decor1 in valentina.inventory
    assert item_decor2 in valentina.inventory

    # swap_best_category - truthy
    result = camila.swap_best_by_category(valentina, "Decor", "Clothing")

    assert result
    assert len(camila.inventory) == 3
    assert item_electronics2 in camila.inventory
    assert item_clothing1 in camila.inventory
    assert item_decor2 in camila.inventory

    assert len(valentina.inventory) == 3
    assert item_electronics1 in valentina.inventory
    assert item_decor1 in valentina.inventory
    assert item_clothing2 in valentina.inventory



