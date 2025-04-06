from jd_automation.pages.BasePage import BasePage


# 搜索页面类
class SearchPage(BasePage):
    # 初始化实例对象
    def __init__(self, driver):
        super().__init__(driver)
        self.url= "https://search.jd.com/Search?keyword=手机"

    # 打开搜索页面
    def get_url(self):
        self.driver.get(self.url)





