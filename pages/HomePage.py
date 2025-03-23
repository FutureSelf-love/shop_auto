
class HomePage:

    # 初始化实例对象
    def __init__(self,driver):
        self.driver = driver
        self.url = "https://www.jd.com/"

    # 打开京东首页
    def get_url(self):
        self.driver.get(self.url)

    # 获取页面加载时间
    def get_load_time(self):
        load_time = self.driver.execute_script(
            "return (window.performance.timing.loadEventEnd - window.performance.timing.navigationStart)/1000;"
        )
        return load_time