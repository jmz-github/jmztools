def get_config_from_json(fp):
    import json
    f = open(fp, 'r', encoding='utf-8')
    content = f.read()
    a = json.loads(content)
    f.close()
    return a



def save_config_to_json(config, fp):
    import json
    str_config = json.dumps(config)
    f = open(fp, 'w', encoding='utf-8')
    f.write(str_config)
    f.close()



if __name__ == '__main__':
    config ={'config_path': 'config.json', 'office': [0], 'web': [0], 'way': 0, 'enquiryIndexFile': '', 'freightDailyFile': '', 'freightExcel': ''}
    save_config_to_json(config, 'config.json')