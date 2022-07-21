import json

def data_list_to_rss_filters():
    with open('data/anime_lists.json') as f:
        anime_list = json.loads(f.read())
    
    with open('data/_anime_rss_lists.txt', 'w') as f:
        for x in anime_list:
            f.write(x['title'] + '\n')
    
if __name__ == '__main__':
    data_list_to_rss_filters()