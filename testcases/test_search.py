import pytest
from jd_automation.pages.HomePage import HomePage
from jd_automation.pages.SearchPage import SearchPage


# 搜索功能测试用例
class TestSearch:

    # 测试前置操作
    @pytest.fixture(autouse=True)
    def setup(self,browser):
        self.driver = browser
        self.search_page = SearchPage(browser)

    # 验证是否搜索成功
    def test_search_success(self):
        self.search_page.get_url()
        assert "search.jd.com" in self.driver.current_url,"搜索失败，未搜索商品"

