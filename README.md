# MAL2GCal
Import MAL watching list to Google Calendar
![image](https://user-images.githubusercontent.com/43643389/140039601-90375f78-24a9-47c7-926d-b440d18cd504.png)

## How to use

1. Create .env from [.env.example](https://github.com/SornrasakC/MAL2GCal/blob/main/.env.example), follow the links for each key
2. Run [init.bat](https://github.com/SornrasakC/MAL2GCal/blob/main/init.bat) (Mac user can just <s>begone</s> fix some few lines or just follow it manually)
3. You will be prompted for double redirects, one for MAL, one for GCP, just follow.
4. Activate venv, by default is, ```.\venv\Scripts\activate```
5. (If fails during 2.) ```py .\scripts\optionals\mal_generate_token.py``` and ```py .\scripts\optionals\g_generate_token.py``` are there for you
6. Try ```py .\scripts\validate.py```, if some links showed up, just follow. (It's to enable Calendar API)
7. Profits ```py .\scripts\main.py``` 
8. (Optional) remember to ```py .\scripts\refresh.py``` after at least one hour has passed.
