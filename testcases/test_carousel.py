import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
from jd_automation.pages.HomePage import HomePage


class TestCarousel:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.home_page = HomePage(browser)
        self.home_page.get_url()


    # 测试轮播图是否存在
    def test_carousel_items_count(self):
        assert self.home_page.wait.until(EC.presence_of_all_elements_located(self.home_page.carousel)), "轮播图未找到"


    # 测试轮播图数量
    def test_carousel_num(self):
        num = self.home_page.get_carousel_item_account()
        assert num>0,"轮播图数量为0"


     # 测试指示点导航功能
    @pytest.mark.parametrize("dot_index",[0,1,2,3,4,5])
    def test_dot_nav(self,dot_index):
        self.home_page.click_dot(dot_index)
        time.sleep(1)
        assert self.home_page.get_cative_item_index() == dot_index,f"指示点{dot_index}导航功能异常"