try:
    import subprocess
    from typing_extensions import Self
except ModuleNotFoundError.__doc__ as mnfe:
    raise mnfe
finally:
    ...
class InstallDependencies:
    def __init__(self : Self) -> None:
        subprocess.call(args=['py' , '-m' , 'pip' , 'install' , '--upgrade' , 'pip'])
        subprocess.call(args=['py' , '-m' , 'pip' , 'install' , '--upgrade' , 'pytube' , 'tk' , 'customtkinter'])
if (__name__ == '__main__' and __package__ is None):
    InstallDependencies()