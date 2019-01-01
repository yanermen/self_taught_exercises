import requests
import fire


def url_site(url_link):
    url = requests.get(url_link)
    if url.status_code == 200:
        get_url_status_code = url.status_code
        print("GET method:          " + str(get_url_status_code))
    else:
        print("GET method: 	     NOT SUCCESS")
    url = requests.post(url_link)
    if url.status_code == 200:
        post_url_status_code = url.status_code
        print("POST method:         " + str(post_url_status_code))
    else:
        print("POST method: 	     NOT SUCCESS")
    url = requests.head(url_link)
    if url.status_code == 200:
        head_url_status_code = url.status_code
        print("HEAD method:         " + str(head_url_status_code))
    else:
        print("HEAD method: 	     NOT SUCCESS")
    url = requests.put(url_link)
    if url.status_code == 200:
        put_url_status_code = url.status_code
        print("PUT method:          " + str(put_url_status_code))
    else:
        print("PUT method: 	     NOT SUCCESS")
    url = requests.delete(url_link)
    if url.status_code == 200:
        delete_url_status_code = url.status_code
        print("DELETE method:       " + str(delete_url_status_code))
    else:
        print("DELETE method: 	     NOT SUCCESS")


def main():
    fire.Fire(url_site)


if __name__ == "__main__":
    main()
