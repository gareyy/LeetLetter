init python:
    import os
    from pathlib import Path
    UP_ARROW = "⬆️"
    DOWN_ARROW = "⬇️"
    command = ""

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
        
        def get_curr_list(self) -> str:
            return self.open_dir(self.path_list[-1])
        
        def get_curr_path(self) -> str:
            return self.path_list[-1]

        def restrict_view(self, items: list[str]) -> list[str]:
            to_return = [items[i:i + 5] for i in range(0, len(items), 5)]

            if self.viewpoint < 0:
                self.viewpoint = 0
            elif self.viewpoint >= len(to_return):
                self.viewpoint = len(to_return) - 1
            
            if len(to_return) != 0:
                focus = to_return[self.viewpoint]
                focus.insert(0, "../")
                if self.viewpoint != 0:
                    focus.insert(0, UP_ARROW)
                if self.viewpoint != len(to_return)-1:
                    focus.append(DOWN_ARROW)
                return focus
            else:
                return ["../"]

        def get_full_path(self, file: str) -> str:
            return str(self.get_curr_path()) + "/" + file

        def process_view(self, command: str) -> list[str]:
            if command == UP_ARROW:
                self.viewpoint -= 1
            elif command == DOWN_ARROW:
                self.viewpoint += 1
            elif command == "../":
                if len(self.path_list) > 1: self.path_list.pop()
            elif command.endswith("/") and \
            self.path_list[-1] != self.get_full_path(command):
                    self.path_list.append(self.get_full_path(command))
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
    if not command.endswith(".py"):
        jump file_loading
    else:
        "[file_loader.get_full_path(command)]"