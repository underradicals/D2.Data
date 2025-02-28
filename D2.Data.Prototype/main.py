from Common import get_config, Auth

if __name__ == "__main__":
    data: Auth = get_config(Auth.SECTION_NAME)
    print(data.apikey)
    print(data.baseurl)
