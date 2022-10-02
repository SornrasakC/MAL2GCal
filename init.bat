@REM set virtual env folder name
SET venv=venv

py -m venv %venv%


SET pip=.\%venv%\Scripts\pip
SET py=.\%venv%\Scripts\python

%pip% install -r .\requirements.txt

@REM Enable sibling module import
%pip% install -e .

%py% .\scripts\optionals\mal_generate_token.py

%py% .\scripts\optionals\g_generate_token.py

%py% .\scripts\validate.py
