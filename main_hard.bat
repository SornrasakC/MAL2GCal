@REM set virtual env folder name
SET venv=venv

SET pip=.\%venv%\Scripts\pip
SET py=.\%venv%\Scripts\python

%py% .\scripts\generate.py
%py% .\scripts\main.py
