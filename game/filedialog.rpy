init python:
    import os
    from pathlib import Path
    '''
    UP_ARROW = "⬆️"
    DOWN_ARROW = "⬇️"

    class fileLoader:
        def open_dir(self, path: str) -> list[str]:
            print(path)
            curr_path = os.scandir(path)
            to_return = []
            for x in curr_path:
                if x.is_dir():
                    to_return.append(x.name + "/")
                elif x.name.endswith(".py"):
                    to_return.append(x.name)
            return to_return

        def __init__(self) -> None:
            self.path_name = Path.home()
            self.path_list = [self.path_name]
            self.viewpoint = 0

        def restrict_view(self, items: list[str]) -> list[str]:
            to_return = [items[i:i + 5] for i in range(0, len(items), 5)]

    file_loader = fileLoader()
    '''


screen choose_menu(lister):
    style_prefix "choice"
    vbox:
        for l in lister:
            textbutton "[l]" action [SetVariable("opened", l), Return()]

label file_loading:
    $ file = renpy.input("Please paste in a full path (/home/user/file.py) to your python file")
    menu:
        "Are you sure you this is the desired file? [file]"

        "Yes":
            if not file.endswith(".py")

        "No":
            jump file_loading