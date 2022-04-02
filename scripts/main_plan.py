from utils import mal_refresh_token, g_refresh_token, create_anime_plan_lists, create_anime_events
import time

print('Starting "create_anime_plan_lists"')
create_anime_plan_lists() 
print('End of "create_anime_plan_lists"')

print('Sleeping')
time.sleep(1)

print('Starting "create_anime_events"')
create_anime_events()
print('End of "create_anime_events"')
