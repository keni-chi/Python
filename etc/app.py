# coding: utf-8

def os_path_append():
    """"method_os."""
    print('os_path_append--------------------start')
    import os
    import sys
    sys.path.append(os.path.abspath('../etc'))

    # クラスのメソッド呼び出し
    from path_sample import PathSample
    PathSample.path_classmethod('test1')
    PathSample().path_instancemethod('test2')

    # メソッド呼び出し
    import path_sample as ps
    ps.global_method('test3')

    # 継承したクラスのメソッド呼び出し
    from path_sample import PathSampleChild
    PathSampleChild.path_classmethod('test4')
    PathSampleChild.path_classmethod_child('test5')
    PathSampleChild().path_instancemethod('test6')

    # フィールド操作
    inst = PathSample('test1')
    print(inst.data)
    inst.data = 'test2'
    print(inst.data)

    # getter
    inst = PathSample()
    x = inst._get_indata()
    print(x)
    print('os_path_append--------------------end')


def _urllib_request(url, body, headers, method):
    """HTTP request by JSON. """
    import urllib.request
    import json

    if body is not None:
        body_str = json.dumps(body).encode('utf-8')
    else:
        body_str = None

    req = urllib.request.Request(url, body_str, headers, method=method)

    try:
        res = urllib.request.urlopen(req)
        res_code = res.status
        res_headers = res.info()
        res_body_tmp = res.read()
    except urllib.error.HTTPError as err:
        res_code = err.code
        res_headers = err.info()
        res_body_tmp = err.read()

    bodystr = res_body_tmp.decode('utf-8')
    if len(bodystr) > 0:
        res_body = json.loads(res_body_tmp.decode('utf-8'))
    else:
        res_body = res_body_tmp
    res_json = {
        "code": res_code,
        "headers": res_headers,
        "body": res_body
    }
    return res_json


def requests_sample():
    import requests
    headers = {
        'Content-Type': 'application/json',
        'charset': 'utf-8',
        'Content-Language': 'en',
        'Cache-Control': 'no-cache'
    }
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=400040'
    r = requests.get(url, headers=headers)
    print(r)
    # print(r.content)
    # print(r.text)
    # print(r.json)

    print('post---------')
    r = requests.post('https://httpbin.org/post', data = {'key':'value'})
    print(r.content)

    print('put---------')
    r = requests.put('https://httpbin.org/put', data = {'key':'value'})
    print(r.content)

    print('delete---------')
    r = requests.delete('https://httpbin.org/delete')
    print(r.content)



def urllib_request_sample():
    """urllib_request_sample. """
    print('urllib_request_sample--------------------start')
    url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=400040"
    body = None
    headers = {
        'Content-Type': 'application/json',
        'charset': 'utf-8',
        'Content-Language': 'en',
        'Cache-Control': 'no-cache'
    }
    res_json = _urllib_request(url, body, headers, 'GET')
    print(res_json['code'])
    print('urllib_request_sample--------------------end')


def read_json():
    """read_json. """
    print('read_json--------------------start')
    import os
    import json

    test_path = os.getcwd() + '/file/'
    file_path001 = test_path + 'input.json'
    f = open(file_path001)
    file_data001 = json.load(f)
    print(file_data001)
    f.close()

    print('read_json--------------------end')
    return file_data001


def check_datetime(data, type='second'):
    """check_datetime. """
    from datetime import datetime
    try:
        if type == 'second':
            datetime.strptime(data, '%Y-%m-%dT%H:%M:%SZ')
            return True
        elif type == 'millisecond':
            datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%fZ')
            return True
        else:
            return False
    except ValueError as err:
        return False


def check_uuid(data):
    """check_uuid."""
    import re
    result = True
    uuid_format = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    if not re.match(uuid_format, str(data).lower()):
        result = False
    return result


def in_xxxx():
    """in_xxxx."""
    print('in_xxxx--------------------start')
    x = ['abc', 'def']
    y = 'abc'
    z = [1, 'abc']

    if y in x:
        print('リスト項目あり')

    if 'a' in y:
        print('aを含む文字列です.')

    for i in z:
        print(type(i))
    print('in_xxxx--------------------end')


def _check_data(s):
    """_check_data."""
    if s == 'v2':
        return True
    else:
        return False


def list_inner():
    """list_inner."""
    print('list_inner--------------------start')
    data = {"k": "v1,v2,v3"}
    data_params = [s for s in data['k'].split(',') if not _check_data(s)]
    print(data_params)
    print('list_inner--------------------end')


def _xpath_get(data, path):
    """_xpath_get."""
    elem = data
    key_list = path.strip("/").split("/")
    for key in key_list:
        if key in elem:
            elem = elem[key]
        else:
            return None
    return elem


def xpath_get_sample():
    """xpath_get_sample."""
    print('xpath_get_sample--------------------start')
    sample_data = {
        "k1": {
            "k2-1": "v2-1",
            "k2-2": "v2-2"
        }
    }

    path = "/k1/k2-1"
    data = _xpath_get(sample_data, path)
    print(data)

    path = "/k1"
    data = _xpath_get(sample_data, path)
    print(data)
    print('xpath_get_sample--------------------end')


def _dict_merge(dct, merge_dct):
    import collections
    for k, v in merge_dct.items():
        if (k in dct and isinstance(dct[k], dict) and isinstance(merge_dct[k], collections.Mapping)):
            _dict_merge(dct[k], merge_dct[k])
            return dct
        else:
            dct[k] = merge_dct[k]
            return


def excel_sample():
    print('excel_sample--------------------start')
    import pandas as pd
    import json
    df = pd.read_excel('file/read_data.xlsx', 'Sheet1', parse_cols=[0, 2, 5])
    print(df)
    oneJson_list = []
    res_dict = {}

    for index, row_item in df.iterrows():
        # 変数宣言
        row_item_dict = {}
        row_item_first = "true"

        # keyの読み出し処理
        en = str(row_item['k1'])
        en_list = en.split('/')
        pro = str(row_item['k3'])
        test_value = str(row_item['k6'])

        # 入れ子構築
        for en_item in reversed(en_list):
            # 1回目
            if row_item_first == "true":
                row_item_dict.update({pro: test_value})
                row_item_first = "false"
                continue
            # 2回目以降
            row_item_dict = {en_item: row_item_dict}
        oneJson_list.append(row_item_dict)
    print(oneJson_list)

    # merge処理
    json_first = "true"
    for oneJson_item in oneJson_list:
        #1回目
        if json_first == "true":
            res_dict = oneJson_item
            json_first = "false"
            continue
        #2回目以降
        res_dict = _dict_merge(res_dict, oneJson_item)
    print(res_dict)

    # JSON出力
    res_str = json.dumps(res_dict)
    file = open("file/output.json", "w")
    file.write(res_str)
    file.close()
    print('excel_sample--------------------end')


def list_copy():
    print('list_copy--------------------start')
    x_list = [0, 1]
    y_list = x_list[:]
    z_list = ['a', 'b']

    print(x_list)
    print(y_list)
    print(z_list)

    x_list.extend(z_list)

    print(x_list)
    print(y_list)
    print(z_list)

    print('deep copy------')
    from copy import deepcopy
    x = [[1, 2, 3], 4, 5]
    y = deepcopy(x)
    print(x)
    print(y)
    y[0][0] = 123
    print(x)
    print(y)
    print('list_copy--------------------end')


def dict_into():
    print('dict_into--------------------start')
    sample_data = {
        "k1": {
            "k2-1": "v2-1",
            "k2-2": "v2-2"
        }
    }
    print(sample_data)

    sample_data['k_new1'] = 'v_new1'
    print(sample_data)
    print('dict_into--------------------end')


def arg_sample(x, *arg):
    print('arg_sample--------------------start')
    print('x: ' + x)
    print(arg)
    print(arg[0])
    print('arg_sample--------------------end')


def kwargs_sample(x, **kwargs):
    print('kwargs_sample--------------------start')
    print('x: ' + x)
    print(kwargs)
    print(kwargs['k1'])
    print('kwargs_sample--------------------end')


def yaml_sample():
    print('yaml_sample--------------------start')
    import yaml
    f = open("./file/input.yml", "r+")
    data = yaml.load(f)
    print(data)
    f.close

    f = open("file/output.yml", "w")
    f.write(yaml.dump(data, default_flow_style=False))
    f.close
    print('yaml_sample--------------------end')


def csv_sample():
    print('csv_sample--------------------start')
    import csv
    f = open('file/input.csv', 'r')
    reader = csv.reader(f)
    print('reader----------')
    print(reader)
    print('header----------')
    header = next(reader) # ヘッダーを読み飛ばしたい時
    print(header)
    print('row----------')
    for row in reader:
        print (row)
    f.close()

    f = open('file/output.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    list=[1,2,3]
    array2d=[[11,12,13], [14,15,16]]
    writer.writerow(list)
    writer.writerows(array2d)
    f.close()

    import pandas as pd
    df = pd.read_csv('file/input.csv')
    print (df)
    print (df['C'])
    print('csv_sample--------------------end')


def encode_decode():
    print('encode_decode--------------------start')
    import base64
    import gzip
    data = 'abcde'
    print(data)
    compress_b = gzip.compress(bytes(data, 'utf-8'))
    encoded_b = base64.b64encode(compress_b)
    encoded_str = encoded_b.decode()
    print(type(encoded_str))
    print(encoded_str)

    decoded_b = base64.b64decode(encoded_str)
    decompress_b = gzip.decompress(decoded_b)
    print(decompress_b)
    raw_data = decompress_b.decode()
    print(raw_data)
    print('encode_decode--------------------end')


def calc_type():
    print('calc_type--------------------start')
    x = 0.1 + 0.1 + 0.1
    print(x)
    print(type(x))

    # 浮動小数点ではなく固定点少数として定義
    # 小数点を文字列型で定義
    from decimal import Decimal, ROUND_HALF_UP
    x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
    print(x)
    print(type(x))

    # 四捨五入
    print(Decimal("123.456789").quantize(Decimal("0.01"),rounding=ROUND_HALF_UP))
    print('calc_type--------------------end')


def dateteime_conv():
    print('dateteime_conv--------------------start')
    from datetime import datetime, timezone
    t_str = '2019-01-01T13:15:55.123Z'
    t_d = datetime.strptime(t_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    print(type(t_d))
    print(t_d)

    t_raw = datetime.strftime(t_d, '%Y-%m-%dT%H:%M:%S.%fZ')[:-4] + 'Z'
    print(type(t_raw))
    print(t_raw)

    tz = timezone.utc
    now = datetime.now(tz)
    print(now)
    now_conv = datetime.strftime(now, '%FT%T.%f')[:-3] + 'Z'
    print(now_conv)
    print('dateteime_conv--------------------end')


def ujson_sample():
    print('ujson_sample--------------------start')
    import ujson
    data = {"key": "value"}
    x = ujson.dumps(data)
    print(x)
    y = ujson.loads(x)
    print(type(y))
    print('ujson_sample--------------------end')


def dict_string():
    print('dict_string--------------------start')
    import json
    data = '{\"key\": \"value1\", \"key\": \"value2\"}'
    print(data)
    data_dict = json.loads(data)
    print(data_dict)

    print('----')
    data = {"key": "value1", "key": "value2"}
    print(data)
    print('dict_string--------------------end')


def reflection_sample():
    print('reflection_sample--------------------start')

    print('globalsを使うパターン----')
    import classes
    cls = getattr(classes, 'Hoge')
    instance = cls()
    instance.get_name()  #=> 'hoge'
    cls = getattr(classes, 'Fuga')
    instance = cls()
    instance.get_name()  #=> 'fuga'

    print('reflection_sample--------------------end')


def none_type():
    print('none_type--------------------start')
    x = None
    print(x)
    x = 1
    print(x)

    print('none_type--------------------end')

def map_sample():
    print('map_filter_reduce--------------------start')
    items = [1, 2, 3]

    def plus(n): # 10加算して返すだけの関数plus
        return n+10
    x = map(plus, items) #itemsの要素すべてにplus関数の実行し、新しいlistを返す
    print(x)
    for i in x:
        print(i)
    
    y = map(lambda n:n+20, items) #関数部分をlambda関数で指定
    print(y)
    for i in y:
        print(i)

    z = [x+20 for x in items] #同じ事をリスト内包表記で（最適な方法）
    print(z)

    print('map_filter_reduce--------------------end')

def main():
    # ################################################
    # ファイル操作
    # ################################################
    read_json()
    yaml_sample()
    csv_sample()
    excel_sample()

    # ################################################
    # クラス、外部関数
    # ################################################
    os_path_append()

    # ################################################
    # 通信
    # ################################################
    # urllib_request_sample()

    # # requests_sample
    # print('requests_sample--------------------start')
    # requests_sample()
    # print('requests_sample--------------------end')

    # ################################################
    # 正規表現
    # ################################################
    print('check_datetime--------------------start')
    print(check_datetime('2019-02-04T07:06:06.379Z', 'millisecond'))
    print(check_datetime('20190204T07:06:06.379Z', 'millisecond'))
    print('check_datetime--------------------end')

    # check_uuid
    print('check_uuid--------------------start')
    print(check_uuid('12345678-1234-1234-1234-abcde1234567'))
    print(check_uuid('12345678-1234-1234-1234-abcde123456G'))
    print('check_uuid--------------------end')

    # ################################################
    # dict, list, str操作
    # ################################################
    in_xxxx()
    list_inner()
    xpath_get_sample()
    list_copy()
    dict_into()
    arg_sample('a', 1)
    arg_sample('a', 2, 'a')
    kwargs_sample('a', k1=1)
    kwargs_sample('a', k1=2, k2='a')
    # ujson_sample()
    dict_string()

    # ################################################
    # 変換
    # ################################################
    encode_decode()
    dateteime_conv()

    # ################################################
    # 型
    # ################################################
    calc_type()
    none_type()

    # ################################################
    # リフレクション
    # ################################################
    reflection_sample()

    # ################################################
    # map,filter,reduce
    # ################################################
    map_sample()



if __name__ == '__main__':
    print('main---start')
    main()
