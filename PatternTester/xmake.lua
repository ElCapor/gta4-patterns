add_rules("mode.debug", "mode.release")
set_allowedarchs("x86")

add_requires("asmjit", "asmtk", "capstone")
target("PatternTester")
    set_kind("binary")
    set_languages("cxx23")

    add_files("src/**.cpp")
    add_files("../PatternBuilder/src/**.cpp")

    add_packages("asmjit", "asmtk", "capstone")