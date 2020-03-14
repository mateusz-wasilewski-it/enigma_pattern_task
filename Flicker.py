import flickrapi

#api_key = "45923a7bfe1c74e203ec20b7a8ecb150"
#api_secret = "6b5b680a83194751"


class FlickerConnection:
    def __init__(self, api_key, api_secret):
        self._api_key = api_key
        self._api_secret = api_secret
        self.flicker = flickrapi.FlickrAPI(self._api_key, self._api_secret)

    def get_photos_as_url(self, keyword="", number_of_images=100) -> list:
        photos_urls = []
        if keyword != "":
            photos = self.flicker.walk(tag_mode='all', tags=keyword,
                                    extras='url_c', per_page=100, sort='relevance')
        else:
            photos = self.flicker.photos.getRecent(extras='url_c', sort='relevance')
        num_of_valid_urls = 0
        for i, photo in enumerate(photos):
            url = photo.get('url_c')
            if url is not None and url != "":
                photos_urls.append(url)
                num_of_valid_urls +=1
            if num_of_valid_urls == number_of_images:
                break

        return photos_urls

