import re  # 正则
from collections import OrderedDict  # 创建有序字典

from django.conf import settings  # 导入setting配置文件(获取项目根路径urls.py)
from django.urls import URLPattern, URLResolver  # Django自定义的类，可以判断当前URL是否为根路径(URLPattern)或继续向下分发(URLResolver )
from django.utils.module_loading import import_string  # 字符串导入模块


def check_url_exclude(url):
    """
    排除一些特定的URL
    :param url: 待检验的URL
    :return:
    """
    for regex in settings.AUTO_DISCOVER_EXCLUDE:  # 将要定向排除的URL(可包含正则) 按照列表的形式写入配置文件 settings.AUTO_DISCOVER_EXCLUDE  下
        if re.match(regex, url):
            return True


"""
示例：
AUTO_DISCOVER_EXCLUDE = [
    '/admin/.*',
    '/login/',
    '/logout/',
    '/index/',
]
"""


def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    """
    递归的去获取URL
    :param pre_namespace: namespace前缀，用于拼接name
    :param pre_url: url前缀，用于拼接url
    :param urlpatterns: 路由关系列表
    :param url_ordered_dict: 用于保存递归中获取的所有路由
    :return:
    """
    for item in urlpatterns:
        if isinstance(item, URLPattern):  # 已经是根网址，获取name及url写入url_ordered_dict
            if not item.name:  # 没有别名(name)的路由地址直接跳过
                continue
            # 拼接路由别名(包含分发下来的namespace；如 "rbac:menu_list")
            if pre_namespace:
                name = "%s:%s" % (pre_namespace, item.name)
            else:
                name = item.name
            # 拼接路由地址URl(包含分发下来的上层路由；如 "/rbac/menu/list")
            url = pre_url + item.pattern.regex.pattern  # 此时拼接的路由包含起止符号，如：/^rbac/^menu/list/$
            url = url.replace("^", "").replace("$", "")  # 删除起止符：/rbac/menu/list/
            # 排除一些特定的路由URL
            if check_url_exclude(url):  # 调用check_url_exclude函数定向排除部分URL
                continue
            url_ordered_dict[name] = {"name": name, "url": url}

        elif isinstance(item, URLResolver):  # 路由分发，递归操作
            if pre_namespace:  # 上次循环(上一层)分发是否包含namespace
                if item.namespace:  # 本次循环(当前层)是否包含namespace
                    namespace = "%s:%s" % (pre_namespace, item.namespace,)  # 上层、当前层都包含直接拼接两层的namespace
                else:
                    namespace = pre_namespace  # 当前层分发不包含namespace，直接用上一层的
            else:
                if item.namespace:
                    namespace = item.namespace  # 上一层分发不包含namespace，直接使用当前层的
                else:
                    namespace = None  # 上一层、当前层都没有，直接定义层none
            recursion_urls(namespace, pre_url + item.pattern.regex.pattern, item.url_patterns,
                           url_ordered_dict)  # 递归继续执行


def get_all_url_dict():
    """
    获取项目所有路由
    :return:
    """
    url_ordered_dict = OrderedDict()  # 包含本项目所有权限URl的有序字典
    md = import_string(settings.ROOT_URLCONF)  # 配置文件内的 ROOT_URLCONF 为本项目根路由urls.py 的路径(字符串)，使用 import_string 用字符串加载模块
    recursion_urls(None, "/", md.urlpatterns,
                   url_ordered_dict)  # 调用 recursion_urls 函数获取所有路由字典，根路径下没有namespace 定义为 None；没有url前缀 定义为 /
    return url_ordered_dict


if __name__ == '__main__':

    dict = get_all_url_dict()

