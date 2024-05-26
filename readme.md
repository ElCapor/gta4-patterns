# PYTHON VERSION

# GTA IV Pattern Builder & Unit Test

GOAL : Building GTAIV function patterns that work for all gta 4 versions , from 1000 (Base) to 1130 (EFLC) until 1200 (CE). These patterns can be used to build a framework similar to scripthook/iv-sdk

HOW ? <br>
Use assembly code ->  Convert to pattern with flags

WARNING : this is W.I.P and in early stages, structure and code may change at any time

# Structure
PatternBuilder , aka ASM2AOB, main code for converting assembly to patterns

PatternTester , the program who will be testing patterns and validating tests

assembly , this where u put ur assembly code for functions

out => folder where all the binaries/patterns/output goes

versions => gta 4 versions u wanna test

NO UML DIAGRAM FOR NOW I'm too tired

# USE CASE

This is not a cheat.

This is not a mod.

This is not gta4 source code.

This is not newbie-friendly.

This is what you use to grab addresses of essential game functions, to build your own mods/dlls/asi plugins etc

# Running
just use any python version, necessary modules :

```
keystone-engine
```

# FAQ
- Why is versions folder empty ?
    <br>Cuz i don't want to go in jail yet, you can easily find all the versions on the internet by extracting patches from a website like this one https://community.pcgamingwiki.com/files/file/1054-grand-theft-auto-iv-patch-6/

# Credit

GTA IV Modding Discord Server for insane amount of support

AUPX for downgrade patch for my initial reverse

ElCapor - Developer

# Contributing
I suck at explaining stuff, so i don't expect anyone to understand all of what's happening in the code. But if you actually have something to fix or contribute i'll be more than happy to accept.