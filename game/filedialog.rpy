init python:
    import os
    from pathlib import Path
    
    import importlib.util
    def load_script(path: str):
        spec = importlib.util.spec_from_file_location("tester", path)
        package = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(package)
        return package

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
I met a traveller from an antique land,
Who said—“Two vast and trunkless legs of stone
Stand in the desert. . . . Near them, on the sand,
Half sunk a shattered visage lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them, and the heart that fed;
And on the pedestal, these words appear:
My name is Ozymandias, King of Kings;
Look on my Works, ye Mighty, and despair!
Nothing beside remains. Round the decay
Of that colossal Wreck, boundless and bare
The lone and level sands stretch far away.”
    '''


#screen choose_menu(lister):
#    style_prefix "choice"
#    vbox:
#        for l in lister:
#            textbutton "[l]" action [SetVariable("opened", l), Return()]


label file_loading:
    #this is example code to be loaded into the path rpy files
    $ file = renpy.input("Please paste in a full path (/home/user/file.py) to your python file")
    menu:
        "Are you sure you this is the desired file? [file]"

        "Yes":
            if not file.endswith(".py"):
                "File is not a python file"
                jump file_loading
            else:
                python: 
                    pack = load_script(file)
                    try:
                        pack.testie() # HAHA I DID IT
                    except Exception as e:
                        raise e

        "No":
            jump file_loading