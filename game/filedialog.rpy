init python:
    UP_ARROW = "⬆️"
    DOWN_ARROW = "⬇️"
    command = ""

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
            self.viewpoint = 0
        
        def get_curr_list(self):
            return self.curr_list

        def restrict_view(self, items: list[str]) -> list[str]:
            to_return = [items[i:i + 5] for i in range(0, len(items), 5)]
            if self.viewpoint < 0:
                self.viewpoint = 0
            elif self.viewpoint >= len(to_return):
                self.viewpoint = len(to_return) - 1

            focus = to_return[self.viewpoint]
            if self.viewpoint != 0:
                focus.insert(0, UP_ARROW)
            if self.viewpoint != len(to_return)-1:
                focus.append(DOWN_ARROW)

            return focus

        def process_view(self, command: str) -> list[str]:
            if command == UP_ARROW:
                self.viewpoint -= 1
            elif command == DOWN_ARROW:
                self.viewpoint += 1
            return self.restrict_view(self.get_curr_list())
    
    file_loader = fileLoader()


screen choose_menu(lister):
    style_prefix "choice"
    vbox:
        for l in lister:
            textbutton "[l]" action [SetVariable("opened", l), Return()]

label file_loading:
    call screen choose_menu(file_loader.process_view(command))
    $ command = opened
    if command in [UP_ARROW, DOWN_ARROW]:
        jump file_loading
    else:
        "[command]"