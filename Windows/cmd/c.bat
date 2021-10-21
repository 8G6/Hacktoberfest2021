@echo off
cd %CD%
cmd /c gcc %1.c -o %1
timeout 1 > NUL 
start %1.exe
