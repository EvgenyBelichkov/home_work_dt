from main import MenuPrinter


class Menu:
    def getItems(self):

        return {
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



def test_class_MenuPrinter(capsys):
    menu = Menu()
    menu_printer = MenuPrinter(menu)
    menu_printer.print_menu()
    out, err = capsys.readouterr()
    assert out == '/welcome\n/dishes/main/fish\n/dishes/main/meat\n/dishes/salads\n'

