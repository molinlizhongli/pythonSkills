from snapshot_selenium import snapshot as driver

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot


def bar_chart() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
            .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c


# 需要安装 snapshot-selenium 或者 snapshot-phantomjs
# 需要注意下可能会报Message: 'chromedriver' executable needs to be in PATH异常，这个原因是没有下载对应的Chrome驱动，并把环境添加到环境变量中
# http://npm.taobao.org/mirrors/chromedriver/ 或者  http://chromedriver.storage.googleapis.com/index.html ，这个selenium爬虫也会用到
# 安装过程可参考：https://blog.csdn.net/su_2018/article/details/100127223
make_snapshot(driver, bar_chart().render(), "bar.png")
