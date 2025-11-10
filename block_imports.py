import os,sys,importlib.abc

def install_from_env(envkey:str="IMPORT_BLOCKLIST"):
    raw=os.getenv(envkey,"")
    block={s.strip() for s in raw.split(",") if s.strip()}
    if(not block): 
        return

    class BlocklistFinder(importlib.abc.MetaPathFinder):
        def __init__(self,roots):
            self.roots=set(roots)
        def find_spec(self,fullname,path,target=None):
            root=fullname.split(".",1)[0]
            if(root in self.roots):
                raise ModuleNotFoundError(f"blocked: {fullname}")
            return None

    for name in list(sys.modules):
        if(name.split(".", 1)[0] in block):
            del sys.modules[name]
    sys.meta_path.insert(0,BlocklistFinder(block))
