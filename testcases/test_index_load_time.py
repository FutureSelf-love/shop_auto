import pytest
from jd_automation.pages.HomePage import HomePage


class TestIndexLoadTime:

    # 测试前置操作
    @pytest.fixture(autouse=True)
    def setup(self,browser):
        self.home_page = HomePage(browser)
        self.home_page.get_url()

    # 测试页面加载时间
    def test_load_time(self):
        time = self.home_page.get_load_time()
        print(f"页面的加载时间为{time}秒")
        assert time<8,"首页加载时间过长"




