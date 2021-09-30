from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from random import randint

class Bot():

    links = []

    comments = ['Great post', 'Amazing work!']

    def __init__(self):
         self.login('internshipstarks')
         self.like_comment_by_hashtag('technology')

    def login(self, username):
         self.driver = webdriver.Chrome(ChromeDriverManager().install())
         self.driver.get('https://www.instagram.com/')
         time.sleep(5)
         username_field = self.driver.find_element_by_xpath("//input[@name='username']")
         username_field.send_keys('internshipstarks')
         password_field = self.driver.find_element_by_xpath("//input[@name='password']")
         password_field.send_keys('intern_academy')
         time.sleep(3)
         login_btn = self.driver.find_element_by_xpath("//button[@type='submit']")
         login_btn.click()
         time.sleep(5)
         notnow = self.driver.find_element_by_xpath('//*[@id=\"react-root\"]/section/main/div/div/div/div/button')
         notnow.click()
         time.sleep(5)
         notnow1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
         notnow1.click()
         time.sleep(3)

    def like_comment_by_hashtag(self, hashtag):
         search_box = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
         search_box.send_keys('#'+hashtag)
         time.sleep(3)
         self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a').send_keys(Keys.ENTER)
         time.sleep(5)

         # follow
         self.driver.find_element_by_xpath('//button[text()="Follow"]').click()
         time.sleep(5)

         links = self.driver.find_elements_by_tag_name('a')
         def condition(link):
             return '.com/p/' in link.get_attribute('href')
         valid_links = list(filter(condition, links))

         for i in range(5):
             link = valid_links[i].get_attribute('href')
             if link not in self.links:
                 self.links.append(link)

         for link in self.links:
             self.driver.get(link)

             #like
             time.sleep(3)
             self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()
             time.sleep(5)

             #comment
             self.driver.find_element_by_class_name('RxpZH').click()
             time.sleep(3)
             self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
             time.sleep(3)
             self.driver.find_element_by_xpath("//button[@type='submit']").click()
             time.sleep(3)


def main():
    my_bot = Bot()

if __name__== '__main__':
    main()