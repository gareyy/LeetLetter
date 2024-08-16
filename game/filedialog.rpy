init python:
    class fileLoader:
        def open_dir(self, path: str) -> list[str]:
            curr_path = os.scandir(path)
            to_return = []
            for x in curr_path:
                if x.is_dir():
                    to_return.append(x.name + "/")
                elif x.name.endswith(".py"):
                    to_return.append(x.name)
            return to_return

        def __init__(self) -> None:
            import os
            from pathlib import Path
            self.path_name = Path.home()
            self.upper_path = self.path_name
            self.curr_list = self.open_dir(self.path_name)
        
        def get_curr_list(self):
            return self.curr_list

        def restrict_view(self, items: list[str]) -> list[str]:
            pass
    
    file_loader = fileLoader()


screen choose_menu(lister):
    style_prefix "choice"
    vbox:
        for l in lister:
            textbutton "[l]" action [SetVariable("opened", l), Return()]

label file_loading:
    call screen choose_menu(file_loader.get_curr_list())
    $ p = opened
    "[p]"