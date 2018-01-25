"""
获取知乎专栏粉丝
DATE：20180125
"""
import requests

# 请求链接
url = 'https://zhuanlan.zhihu.com/api/columns/alenxwn/followers'
# 模拟浏览器
header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/63.0.3239.132 Mobile Safari/537.36'}
# 参数
data = {'limit': 20, 'offset': 40}


# 获得数据
def get_data():
    html = requests.get(url, params=data, headers=header)
    for n in range(len(html.json())):
        print(html.json()[n]['hash'])


if __name__ == '__main__':
    get_data()
