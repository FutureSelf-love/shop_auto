from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 封装通用方法
class BasePage:

    def __init__(self,driver):
        self.driver = driver

    """关闭所有可能遮挡的弹窗"""
    def close_popups(self):
        try:
            self.driver.execute_script("""
                       let count = 0;
                       const removePopup = () => {
                           const popups = document.querySelectorAll('.umc-equity, .popup-layer, .j-modal');
                           popups.forEach(el => el.remove());
                           return popups.length;
                       };

                       // 循环尝试3次，每次间隔0.3秒
                       const interval = setInterval(() => {
                           if (removePopup() === 0 || count++ >= 3) {
                               clearInterval(interval);
                           }
                       }, 300);
                   """)
        except:
            pass

    # 查找单个元素
    def find_element(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(
            EC.presence_of_element_located(locator)
        )

    # 查找多个元素
    def find_elements(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    # 元素点击
    def click(self,locator):
        self.find_element(locator).click()

    # 获取页面标题
    def get_title(self):
        return self.driver.title