# MAL2GCal
Import MyAnimeList (MAL) watching list to Google Calendar

![image](https://user-images.githubusercontent.com/43643389/140039601-90375f78-24a9-47c7-926d-b440d18cd504.png)

## Installation

1. Create .env from [.env.example](https://github.com/SornrasakC/MAL2GCal/blob/main/.env.example), follow the links for each key
2. Run [init.bat](https://github.com/SornrasakC/MAL2GCal/blob/main/init.bat) (Mac user can just <s>begone</s> fix some few lines or just follow it manually)
3. You will be prompted for double redirects, one for MAL, one for GCP, just follow.
4. (Optional) If anything fails, activate venv, by default is, ```.\venv\Scripts\activate```
5. (Optional) If any token generation fails, try 
- ```py .\scripts\optionals\mal_generate_token.py``` 
- ```py .\scripts\optionals\g_generate_token.py```
7. (Optional) After manual token generation, try ```py .\scripts\validate.py```, if some links showed up, just follow. (It's to enable Calendar API)
8. Either use [main_soft.bat](https://github.com/SornrasakC/MAL2GCal/blob/main/main_soft.bat) or [main_plan_soft.bat](https://github.com/SornrasakC/MAL2GCal/blob/main/main_plan_soft.bat), or both. 
- ```main_soft``` for importing "watching" list. 
- ```main_plan_soft``` for importing "plan to watch" list.

### Subsequent usage

After long period (maybe one whole season),
- [main_hard.bat](https://github.com/SornrasakC/MAL2GCal/blob/main/main_hard.bat) ( watching list )
- [main_plan_hard.bat](https://github.com/SornrasakC/MAL2GCal/blob/main/main_plan_hard.bat) ( plan to watch list )

Used recently (maybe one or two hours),
- [main_soft.bat](https://github.com/SornrasakC/MAL2GCal/blob/main/main_soft.bat) ( watching list )
- [main_plan_soft.bat](https://github.com/SornrasakC/MAL2GCal/blob/main/main_plan_soft.bat) ( plan to watch list )
