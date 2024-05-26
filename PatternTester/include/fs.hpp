#ifndef FILESYSTEMUTILS_HPP
#define FILESYSTEMUTILS_HPP
#include <cstdint>
#include <exception>
#include <filesystem>
#include <fstream>
#include <sstream>
#include <string>

namespace fs = std::filesystem;

namespace fsutils
{
    std::string loadFile(const char *const name);
    std::string loadFile(const std::string &name);

    std::string loadFile(const char *const name)
    {
        fs::path filepath(fs::absolute(fs::path(name)));

        std::uintmax_t fsize;

        if (fs::exists(filepath))
        {
            fsize = fs::file_size(filepath);
        }
        else
        {
            throw(std::invalid_argument("File not found: " + filepath.string()));
        }

        std::ifstream infile;
        infile.exceptions(std::ifstream::failbit | std::ifstream::badbit);
        try
        {
            infile.open(filepath.c_str(), std::ios::in | std::ifstream::binary);
        }
        catch (...)
        {
            std::throw_with_nested(std::runtime_error("Can't open input file " + filepath.string()));
        }

        std::string fileStr;

        try
        {
            fileStr.resize(fsize);
        }
        catch (...)
        {
            std::stringstream err;
            err << "Can't resize to " << fsize << " bytes";
            std::throw_with_nested(std::runtime_error(err.str()));
        }

        infile.read(fileStr.data(), fsize);
        infile.close();

        return fileStr;
    }

    std::string loadFile(const std::string &name) { return loadFile(name.c_str()); };
    
    fs::path executableDirectory()
    {
        return fs::current_path();
    }
}

#endif /* FILESYSTEMUTILS_HPP */
