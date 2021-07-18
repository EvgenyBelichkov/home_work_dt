"""
We have class Menu to work with app menu items.
It has method getItems(): dict that returns us a dict of menu items.
It looks like following dictionary.

Write a new class (using class Menu) that prints all breadcrumbs
(/dishes/main/fish) for all captions.
Each level comes from the key.
Each item can have an infinite number of sub items.
"""


class MenuPrinter:
    def __init__(self, menu):
        self.menu = menu

    def print_menu(self):
        self.print_menu_items(self.menu.getItems(), "")

    def print_menu_items(self, items, parent):
        if items is None:
            print(parent)
            return

        for title, menu_item in items.items():
            self.print_menu_items(menu_item.get('items'), parent + "/" + title)

