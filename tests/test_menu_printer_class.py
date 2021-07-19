from main import MenuPrinter
import pytest

example_1 = {
            'welcome': {
                'caption': 'Welcome',
            },
            'dishes': {
                'caption': 'Our menu',
                'items': {
                    'main': {
                        'caption': 'Main dishes',
                        'items': {
                            'fish': {
                                'caption': 'Fish menu',
                            },
                            'meat': {
                                'caption': 'Meat menu',
                            }
                        }
                    },
                    'salads': {
                        'caption': 'Salads',
                    },
                }
            },
            # Here comes more and more
        }


@pytest.mark.parametrize("dictionary, expected_result", [(example_1, '/welcome\n/dishes/main/fish\n/dishes/main/meat\n/dishes/salads\n')])
def test_class_MenuPrinter(capsys, dictionary, expected_result):
    class Menu:
        def getItems(self):
            return dictionary

    menu = Menu()
    menu_printer = MenuPrinter(menu)
    menu_printer.print_menu()
    out, err = capsys.readouterr()
    assert out == '/welcome\n/dishes/main/fish\n/dishes/main/meat\n/dishes/salads\n'
    assert err == ''


def test_class_MenuPrinter_with_empty_dict(capsys):
    class Menu:
        def getItems(self):
            return {}
    menu = Menu()
    menu_printer = MenuPrinter(menu)
    menu_printer.print_menu()
    out, err = capsys.readouterr()
    assert out == ''
