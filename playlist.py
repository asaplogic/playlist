import requests
import datetime
from bs4 import BeautifulSoup



def pull_data(playlist):

   
    file_name = 'play_list_data.txt'
    save_file = open(file_name, 'w')


    playlist_url = "http://www.radiomilwaukee.org.php56-15.dfw3-2.websitetestlink.com/playerstream/getstream.php?history"
    list_code = requests.get(playlist_url).text
    
    



pull_data(list)

block_list = list_code.split()
print(block_list)