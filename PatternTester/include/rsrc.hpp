#ifndef RESOURCEMANAGER_HPP
#define RESOURCEMANAGER_HPP
#include <filesystem>
#include "fs.hpp"
namespace fs = std::filesystem;
class ResourceManager
{
public:
    ResourceManager() : m_ResourcesPath(fsutils::executableDirectory().concat("\\")) {}
    fs::path ResourcesPath() {return m_ResourcesPath;}
    fs::path AssemblyPath() {return ResourcesPath().concat("\\assembly");}
    fs::path PatternsPath() {return ResourcesPath().concat("\\patterns");}

    

    std::string ReadAssemblyFile(std::string m_name) {return fsutils::loadFile(AssemblyPath().concat("\\" + m_name + ".asm").string());};
private:
    fs::path m_ResourcesPath;
};

#endif /* RESOURCEMANAGER_HPP */
