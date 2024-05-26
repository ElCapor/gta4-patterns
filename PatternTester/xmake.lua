add_rules("mode.debug", "mode.release")
set_allowedarchs("x86")

add_requires("asmjit", "asmtk", "capstone")
target("PatternTester")
    set_kind("binary")
    set_languages("cxx23")

    add_files("src/**.cpp")
    add_files("../PatternBuilder/src/**.cpp")

    add_includedirs("include")

    add_packages("asmjit", "asmtk", "capstone")

    after_build(function(target)
        os.cp(target:targetfile(), path.join(os.scriptdir(), "../out"))
        -- temporary hack
        os.cp(path.join(os.scriptdir(), "../assembly"), path.join(os.scriptdir(), "../out"))
    end)