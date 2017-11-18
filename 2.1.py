# 爬取豆瓣TOP250电影
import requests
from bs4 import BeautifulSoup


def get_movies():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/61.0.3163.100 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    a = 1
    f = open('movie.txt', 'w+')
    for i in range(0, 10):
        link = 'http://movie.douban.com/top250?start='+str(i*25)+'&filter=unwatched'
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')
        list2 = soup.find_all('div', class_="pic")
        rank = soup.find_all('span', class_="rating_num")
        for each, each2, each3 in zip(div_list, list2, rank):
            movies = each.a.span.text.strip()
            url = each.a.get('href')
            pic = each2.a.img.get('src')
            mark = each3.text.strip()
            movie_list.append(movies)
            f.write("第"+str(a)+"名:"+movies+"\r\n")
            f.write("链接:" + url + "\r\n")
            f.write("图片地址:" + pic + "\r\n")
            f.write("评价等级:" + mark + "\r\n")
            a += 1
    print("完成")
    f.close()
    return 0
movie = get_movies()
