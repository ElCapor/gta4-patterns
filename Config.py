import os
class Config:
    def __init__(self) -> None:
        self.allowed_versions = [
            1000,
            1010,
            1020,
            1030,
            1040,
            1050,
            1060,
            1070,
            1080,
            # add 1120 here
            1130,
            1200
        ]
    
    def allowed_version(self) -> list[int]:
        return self.allowed_versions
    
    def get_versions_path(self) -> str:
        return os.getcwd() + "\\versions"
    
    def get_gta_exe_path(self, version :int) -> str:
        if version in self.allowed_versions:
            return self.get_versions_path() + f"\\{version}.exe"
        else:
            return ""