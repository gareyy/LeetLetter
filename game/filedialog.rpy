init python:
    import os
    from pathlib import Path
    path_name = Path.home()

    def open_dir(path: str) -> list[str]:
        curr_path = os.scandir(path)
        to_return = []
        for x in curr_path:
            if x.is_dir():
                to_return.append(x.name + "/")
            elif x.name.endswith(".py"):
                to_return.append(x.name)
        return to_return


screen choose_menu(lister):
    style_prefix "choice"
    vbox:
        for l in lister:
            textbutton "[l]" action [SetVariable("need", l), Return()]

label file_loading:
    "[path_name]: [open_dir(path_name)]"
    #call screen choose_menu(filter_folders_and_py(curr_path))
    #$ p = need
    #"[p]"