import pytest
from jd_automation.pages.HomePage import HomePage


class TestNav:

    # 测试前置操作
    @pytest.fixture(autouse=True)
    def setup(self,browser):
        self.home_page = HomePage(browser)
        self.home_page.get_url()

    # 测试导航栏数量
    def test_nav_number(self):
        nav_links_mun  = self.home_page.get_nav_links()
        print(f"导航栏链接数量为{len(nav_links_mun)}")
        assert len(nav_links_mun) > 0,"导航栏没有找到任何链接"

    # 测试未登录时通过索引点击导航栏链接
    @pytest.mark.parametrize("index",[0,1,2,3,4])
    def test_click_by_index(self,index):
        self.home_page.click_nav_link_by_index(index)
        assert self.home_page.get_title()!="京东(JD.COM)","点击导航栏后页面标题未改变"


