@REM set virtual env folder name
SET venv=venv

py -m venv %venv%


SET pip=.\%venv%\Scripts\pip
SET py=.\%venv%\Scripts\python

%pip% install -r .\requirements.txt

@REM Enable sibling module import
%pip% install -e .

%py% .\scripts\mal_generate_token.py

%py% .\scripts\g_generate_token.py

%py% .\scripts\validate.py
