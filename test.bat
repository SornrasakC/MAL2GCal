@REM SET venv=venv2
@REM SET x=%venv%

@REM set virtual env folder name
SET venv=venv

SET pip=.\%venv%\Scripts\pip
SET py=.\%venv%\Scripts\python

@REM %py% .\scripts\refresh.py
@REM %py% .\scripts\main_plan.py
%py% .\scripts\optionals\data_list_to_rss_filters.py
