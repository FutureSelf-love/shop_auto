
from jd_automation.pages.HomePage import HomePage


class TestHomePage:
    def test_load_time(self,browser):
        home_page = HomePage(browser)
        home_page.get_url()
        time = home_page.get_load_time()
        print(f"页面的加载时间为{time}秒")
        assert time<5,"首页加载时间过长"

