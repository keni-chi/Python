# coding: utf-8
import os
import json


def deploy():
    """deploy. """
    print('deploy--------------------start')

    # ファイル読み出し
    file_path = os.getcwd() + '/' + 'input.json'
    f = open(file_path)
    file_data = json.load(f)
    f.close()
    
    # ファイル生成
    policy = file_data['a']['ak1'].replace('v1', 'v100')
    role = file_data['b']['bk1'].replace('bv', 'bv200')    
    file_data.update({"a":{"ak1": policy}})
    file_data.update({"b":{"bk1": role}})
    
    # ファイル出力
    output_str = json.dumps(file_data)
    file = open("output.json", "w")
    file.write(output_str)
    file.close()

    # デプロイ実行
    # os.system('シェルコマンド')

    print('deploy--------------------end')


def main():
    """main. """
    deploy()


if __name__ == '__main__':
    main()
