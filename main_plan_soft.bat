@REM set virtual env folder name
SET venv=venv

SET pip=.\%venv%\Scripts\pip
SET py=.\%venv%\Scripts\python

%py% .\scripts\refresh.py
%py% .\scripts\main_plan.py
