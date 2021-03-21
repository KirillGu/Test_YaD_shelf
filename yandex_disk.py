import unittest
import requests



id_VK = 1
YD_URL = 'https://cloud-api.yandex.net:443/v1/disk'
YANDEX_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

TOKEN_YD = 'Token'

YD_OAUTH = {'Authorization': f'OAuth {TOKEN_YD}'}
yandex_oauth_header = {
    'Accept': 'application/json',
    'Authorization': f'OAuth {TOKEN_YD}'
}



class YDUser:


    def put_request(self, url, params, headers):
        response = requests.put(url, params=params, headers=headers)
        return response.json()

    def yandex_folder(self):
        yandex_folder_url = f'{YD_URL}{"/resources"}'
        yandex_folder_params = {
            'path': f'{"id_VK-"}{id_VK}',
            'overwrite': 'true' #перезапись
        }
        response = self.put_request(yandex_folder_url, params=yandex_folder_params, headers=yandex_oauth_header)
        return response

    def yandex_upload(self, files_for_upload):
        for file in files_for_upload:
            yandex_upload_params = {
                'path': f'{"id_VK-"}{id_VK}{"/"}{file}',
                'overwrite': 'true'
            }
            response = requests.get(YANDEX_UPLOAD_URL, params=yandex_upload_params, headers=yandex_oauth_header)
            put_url = response.json().get('href')
            with open(file, 'rb') as f:
                data_upload = f.read()
            response_upload = requests.put(put_url, data=data_upload)

            for i in tqdm(range(2)):
                time.sleep(1)
            print(f'{file} - успешно загружен!')


        return print(f'Выполнено')

user1 = YDUser()
user1.yandex_folder()
#user1.yandex_upload(files)
