import win32api

class GtaExecutable:
    """
    A GTA 4 Executable
    """
    
    
    def __init__(self, path :str, version :int = 0) -> None:
        """Return a new GtaExecutable object

        Args:
            path (str): path of the executable
            version (int, optional): version of the executable. Defaults to 0.

        Note : version can only be an int between 1000 and 1300
        """
        self.path = path
        self.version = 0 or self.get_version()

    def get_version(self) -> int:
        """Get the version of the executable based on the path

        Returns:
            int: version of the executable
        """
        info = win32api.GetFileVersionInfo(self.path, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        major = win32api.HIWORD(ms)
        minor = win32api.LOWORD(ms)
        build = win32api.HIWORD(ls)
        revision = win32api.LOWORD(ls)
        
        version_str = f"{major}{minor}{build}{revision}"

        return int(version_str)
