#include <asmjit/asmjit.h>
#include <asmtk/asmtk.h>
#include <iostream>
#include <fs.hpp>
#include <rsrc.hpp>
#include <sstream>

using namespace asmjit;
using namespace asmtk;

/// Binary to hex
std::string b2h(uint8_t b0, uint8_t b1) {
    static const char hex_table[] = "0123456789ABCDEF";
    std::stringstream ret;
    ret << hex_table[b0 >> 4] << hex_table[b1 & 0xF];
    return ret.str();
}

template <typename T>
std::vector<T> array2vector(T* array, int size)
{
    std::vector<T> ret;
    for (int i=0; i < size; i++)
    {
        ret.push_back(array[i]);
    }
    return ret;
}

template <typename T>
class PairIterator {
public:
    using iterator_category = std::input_iterator_tag;
    using value_type = std::pair<T, T>;
    using difference_type = std::ptrdiff_t;
    using pointer = value_type*;
    using reference = value_type&;

    PairIterator(typename std::vector<T>::const_iterator it, typename std::vector<T>::const_iterator end)
        : current(it), end(end) {}

    PairIterator& operator++() {
        std::advance(current, 2);
        return *this;
    }

    value_type operator*() const {
        auto next = std::next(current);
        return std::make_pair(*current, (next != end) ? *next : T());
    }

    bool operator!=(const PairIterator& other) const {
        return current != other.current;
    }

private:
    typename std::vector<T>::const_iterator current;
    typename std::vector<T>::const_iterator end;
};

template <typename T>
class PairRange {
public:
    PairRange(const std::vector<T>& vec) : vec(vec) {}

    PairIterator<T> begin() const {
        return PairIterator<T>(vec.begin(), vec.end());
    }

    PairIterator<T> end() const {
        return PairIterator<T>(vec.end(), vec.end());
    }

private:
    const std::vector<T>& vec;
};

int main(int argc, char *argv[])
{
    Environment env(Arch::kX86);
    CodeHolder code;
    code.init(env);

    x86::Assembler a(&code);

    AsmParser p(&a);
    
    ResourceManager* rsrc = new ResourceManager();
    auto asmcode = rsrc->ReadAssemblyFile("pool\\cpool");
    Error err = p.parse(asmcode.c_str());
    if (err)
    {
        printf("ERROR: %08x (%s)\n", err, DebugUtils::errorAsString(err));
        return 1;
    }

    // Now you can print the code, which is stored in the first section (.text).
    CodeBuffer &buffer = code.textSection()->buffer();
    for (size_t i = 0; i < buffer.size(); i++)
        printf("%02X", buffer.data()[i]);
    /*
    auto ret = array2vector<uint8_t>(buffer.data(), buffer.size());
    for (int i =0; i < ret.size(); i+=2)
    {
        std::cout << std::hex << b2h(ret[i], ret[i+1]) << std::endl;
    }*/
    std::cin.ignore();
    return 0;
}