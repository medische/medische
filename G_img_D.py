from icrawler.builtin import GoogleImageCrawler


def google_img_downloader():
    filters = dict(
        type='photo', #тип контента photo, face, clipart, animation
        # color='',# отвечает за цвет изображения, напривет blackandwhite
        # size='',#отвечает за размер large, icon, =1024x768
        # license='',#noncommercial, commercial 
        # date=''#отвечает за то когда было опубликовано изображение: pastweek, ((2020,01,01), (2022,01,01))
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './google_downloader/img'})
    crawler.crawl(
        keyword='Fros Mage', 
        max_num=5, 
        min_size=(1000,1000),
        overwrite=True,
        filters=filters,
        file_idx_offset='auto'
        )

def main():
    google_img_downloader()
    
if __name__ == '__main__':
    main()
    
