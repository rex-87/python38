@echo off
REM - Setup environment for main program
call %~dp0\setup\setup.bat

@echo off
REM - Run main program
call %MINICONDA_INSTALL_FOLDER%\Scripts\activate.bat %ENVIRONMENT_FOLDER%