import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from jd_automation.pages.BasePage import BasePage


class HomePage(BasePage):

    # 初始化实例对象
    def __init__(self,driver):
        super().__init__(driver)
        self.url = "https://www.jd.com/"
        self.wait = WebDriverWait(driver,10)

    # 导航栏分类链接
    nav_link = (By.CSS_SELECTOR,".cate_menu li")
    # 搜索框
    serach_input = (By.ID,"key")
    # 搜索按钮
    search_button = (By.CSS_SELECTOR, ".button")
    # 轮播图元素
    carousel = (By.ID, "J_focus")
    carousel_items = (By.CSS_SELECTOR, ".slider_list .slider_item")
    carousel_dots = (By.CSS_SELECTOR, ".slider_indicators .slider_indicators_btn ")


    # 打开京东首页
    def get_url(self):
        self.driver.get(self.url)

    # 获取页面加载时间
    def get_load_time(self):
        load_time = self.driver.execute_script(
            "return (window.performance.timing.loadEventEnd - window.performance.timing.navigationStart)/1000;"
        )
        return load_time

    # 获得导航栏所有链接
    def get_nav_links(self):
        return self.find_elements(self.nav_link)

    # 通过索引点击导航链接
    def click_nav_link_by_index(self,index):
        self.close_popups()
        links = self.get_nav_links()
        if index < len(links):
            links[index].click()
        else:
            raise IndexError("导航栏索引超出范围")

    # 获取轮播图数量
    def get_carousel_item_account(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.carousel_items))
        num=len(items)
        print(f"轮播图的数量为:{num}")
        return len(items)

    # 点击指定位置的指示点
    def click_dot(self,index):
        self.close_popups()
        dots = self.wait.until(EC.presence_of_all_elements_located(self.carousel_dots))
        if index < len(dots):
            dots[index].click()

    # 获取当前激活的轮播图索引
    def get_cative_item_index(self):
        items =self.wait.until(EC.presence_of_all_elements_located(self.carousel_items))
        for i,item in enumerate(items):
            if "slider_active" in item.get_attribute("class"):
                return i
        return -1
























