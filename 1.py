import yaml


try:
    with open('config.yaml') as f:
        config = yaml.safe_load(f)

        print(config['password'])
        print(config['Email'])
        print(config['sdfsdf'])
        print(config)

except FileNotFoundError:
    print("没有找到配置文件 'config.yaml'。")
except KeyError as e:
    print(f"配置文件 'config.yaml' 中缺少必要的字段：{e}")
