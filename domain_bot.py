from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pathlib
import random
from itertools import *
from string import ascii_lowercase
from time import sleep as wait
import sys

domain_names = []
domain_names_available = []
maximum_search_input = 20

TLD = str(input("What TLD do you want to look for? (Type it in the following format: .TLD)'\n> "))








class Domain_stuff():

    def __init__(self):
        pass


    def domain_name_generator(self):

        '''It generates with all the permutations the domains
    and put them in the file that is assigned the variable  'filename'''''

        for j in islice(product(ascii_lowercase, repeat= user_input), user_input_limit):
            self.keywords = ''.join(j)
            domain_names.append(self.keywords)

        return domain_names

    ## Copy all the names available on domain_names on the file that the variable filename has stored.

    def domain_to_files(self):
        self.file = open(filename, 'w')
        for i in domain_names:
            self.file.write(i + '\n')
        self.file.close()

    ## Transfer all the names that are in the file to a list








class RunSelenium(Domain_stuff):
    def __init__(self, link):
        """

        :rtype: selenium
        """
        self.driver = webdriver.Chrome()
        self.driver.get(link)

        Domain_stuff.__init__(self)
        self.temp_list = []
        self.count = 0


    def closeBrowser(self):
        self.driver.close()
    #
    # def homePage_run(self):
    #     self.elem_bulksearch_button = self.driver.find_element_by_xpath('//*[@id="ctl00_ctl00_ctl00_ctl00_base_content_web_base_content_home_content_page_content_left_ctl00_heroContainer"]/div[1]/div[2]/div[2]/fieldset/a')
    #     self.elem_bulksearch_button.click()
    #     self.elem_bulk_textarea = self.driver.find_element_by_xpath(
    #         '//*[@id="ctl00_ctl00_ctl00_ctl00_base_content_web_base_content_home_content_page_content_left_ctl00_inputBulkDomain"]')
    #     self.elem_bulk_textarea.clear()
    #     self.search_button_bulk_area = self.driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[3]/div[2]/div/button')
    #     for i in range(self.domain_input_search):
    #         self.elem_bulk_textarea.send_keys(domain_names[i] + TLD)
    #         self.elem_bulk_textarea.send_keys(Keys.RETURN)
    #     self.search_button_bulk_area.click()
    #     self.count = i
    #     print(i)
    #     wait(3)



    def files_to_domain(self):
        self.file = open(filename, 'r')
        for line in self.file:
            domain_names.append(line.replace('\n', ''))
        self.file.close()

    def bulkPage_run(self):

        # for j in range(int(letters_PERM / (domain_input_search_first2Digits + domain_input_search_first2Digits))):
        #   #j : 0
        for j in range(int(letters_PERM / (domain_input_search_first2Digits))):
            self.temp_list = []
            self.bulksearch_button_domain_page = self.driver.find_element_by_xpath(
                '//*[@id="ctl00_ctl00_ctl00_ctl00_base_content_web_base_content_home_content_page_content_left_custom_components_dataview_domainsearch_embeddomainsearch_ascx1_embedDomainSearchResults"]/div[2]/form/a')
            self.bulksearch_button_domain_page.click()
            self.bulk_textarea_domain_page = self.driver.find_element_by_xpath('//*[@id="bulk-search"]')
            #TODO Add secondDigit
            for _ in range(int(domain_input_search_first2Digits)):
                self.temp_list.append(domain_names[self.count])
                self.count += 1
            print('temp_list =', self.temp_list)
            print('Status: Typing domains...')
            #TODO Add secondDigit

            for k in range(int(domain_input_search_first2Digits)):  # k : 0
                #print(domain_input_search_first2Digits + domain_input_search_first2Digits)
                #self.internal_remove = 0
                #print('k', k)
                #print('iterate_twice', iterate_twice)
                #print('k', self.temp_list[k])
                #print('iterate_twice', self.temp_list[iterate_twice])
                self.bulk_textarea_domain_page.send_keys(self.temp_list[k] + TLD)
                self.bulk_textarea_domain_page.send_keys(Keys.RETURN)
                #self.temp_list.remove(self.temp_list[0 + self.internal_remove])
                #self.internal_remove += 1
            self.search_button_domain_page_results = self.driver.find_element_by_xpath(
                '//*[@id="ctl00_ctl00_ctl00_ctl00_base_content_web_base_content_home_content_page_content_left_custom_components_dataview_domainsearch_embeddomainsearch_ascx1_embedDomainSearchResults"]/div[2]/form/div[2]/div/button')
            self.search_button_domain_page_results.click()
            ## Status
            self.wait_check = 3
            for time in range(self.wait_check):
                print("Status: Waiting", int(self.wait_check - time), "seconds...")
                wait(1)
            print('Status: Checking domains...')
            #TODO Add secondDigit

            for check in range(int(domain_input_search_first2Digits)):
                self.domain_to_check = self.temp_list[check] + TLD
                self.checkAvailability(locator = '//li[@data-attr-domain-id="' + self.domain_to_check + '" and @class="register"]')
                self.SeparatePremium(
                    locator1='//li[@data-attr-domain-id="' + self.domain_to_check + '" and @class="premium has-promo"]')
                print(self.domain_to_check)

    def isAvailable(self):
        print('Status: Adding', self.domain_to_check ,'to the appropiate file')
        file_domain_available = open(filename2, 'a')
        file_domain_available.write(self.domain_to_check + '\n')
        file_domain_available.close()


    def isPremium(self):
        print('Status: Adding premium domain:', self.domain_to_check, 'to the appropiate file')
        file_domain_Prm_available = open(filename3, 'a')
        file_domain_Prm_available.write(self.domain_to_check + '\n')
        file_domain_Prm_available.close()

    def SeparatePremium(self, locator1):
        try:
            self.elm_Prm = self.driver.find_element_by_xpath(locator1)
            self.present = True
            if self.present == True:
                print('Status:', self.domain_to_check, 'is a premium domain and is available')
                self.isPremium()
        except NoSuchElementException:
            print('Status:', self.domain_to_check, 'is not a premium domain and/or is not available')
            self.present = False

    def checkAvailability(self, locator):
        try:
            self.elm = self.driver.find_element_by_xpath(locator)
            self.present = True
            if self.present == True:
                print('Status:', self.domain_to_check, 'is available')
                self.isAvailable()
        except NoSuchElementException:
            self.present = False
            print('Status', self.domain_to_check, 'is not available and/or is premium')

    def multipleFinder(self):
        '''Takes the biggest factor'''
        self.multiples = []
        self.minimum_input = 40
        for i in range(1, self.minimum_input + 1):
            self.multiples.append(i)

        print(self.multiples)
        i = 0
        self.factor_list = [0]

        self.multiples_len = len(self.multiples)

        while self.factor_list[-1] <= self.minimum_input:

            if i >= int(self.multiples_len - 1):
                '''To avoid IndexError'''
                if len(domain_names) % self.multiples[-1] != 0:
                    break

            if len(domain_names) % self.multiples[i] == 0:
                self.factor_list.append(self.multiples[i])

            i += 1

        self.maximum_multiple = self.factor_list[-1]

        self.maximum_multiple = str(self.maximum_multiple)

        self.maximum_multiple_first = self.maximum_multiple[0] + '0'

        if int(self.maximum_multiple) <= 10:

            self.maximum_multiple_second = 0

        else:
            self.maximum_multiple_second = self.maximum_multiple[-1]

        return int(self.maximum_multiple_first), int(self.maximum_multiple_second)


if __name__ == '__main__':

    selenium = RunSelenium(
        'https://www.namecheap.com/domains/registration/results.aspx?domain=a.com&tlds=com%2Cnet%2Corg%2Cus%2Cinfo%2Cbiz%2Cme%2Cco%2Cco.uk%2Cuk&usetlds=no&type=bulk')


    extension = ".txt"

    filename = "domain_names-domain-bot_" + TLD[1:] + extension

    filename2 = "domain_availables-domain-bot_" + TLD[1:] + extension

    filename3 = "domain_availables_domain_bot_premium_" + TLD[1:] + extension


    def filename_exist():
        global filename
        global filename2
        global filename3

        if path.is_file() == True:
            filename_extensionless = filename.replace('.txt', '') + '_'
            print("Current file name is:", filename,
                  '\n rename your file by adding an extension to the current name, for example if you want'
                  'to add "example" to your file', 'then your file will be stored as',
                  filename_extensionless + 'example.txt')
            user_input_fileExists = input('Please rename the file...\n> ')
            # Modifying filename3 to avoid overwriting
            filename = "domain_names-domain-bot_" + TLD[1:] + '_' + user_input_fileExists + extension
            filename2 = "domain_availables-domain-bot_" + TLD[1:] + '_' + user_input_fileExists + extension
            filename3 = "domain_availables_domain_bot_premium_" + TLD[
                                                                  1:] + '_' + user_input_fileExists + extension
            open_file = open(filename, 'w')
            open_file.close()

            open_file2 = open(filename2, 'w')
            open_file2.close()



    def clear_specific(file_toClear):
        file_clearMe = open(file_toClear, 'w')
        file_clearMe.close()


    user_fileDomain = input(
        'Would you like to generate them randomly or take them from the dictionary? (Just type dictionary or random)\n> ')

    if user_fileDomain in ['dictionary', 'Dictionary', 'd', 'D']:

        filename = input('Enter file desired to search\n> ') + extension
        print(filename)

        selenium.files_to_domain()
        print(len(domain_names))
        domain_input_search_first2Digits, domain_input_search_secondDigit = selenium.multipleFinder()
        print(domain_input_search_first2Digits, domain_input_search_secondDigit)

        selenium.wait_check = 3
        print('Status: Searching', domain_input_search_first2Digits + domain_input_search_secondDigit, 'domains')
        ## To replace letters_PERM
        letters_PERM = len(domain_names)


    else:
        user_input = int(input("Enter the number of letters you want the domain to contain? \n> "))
        user_input_all = input('Do you want to check them all?\n> ')
        if user_input_all in ['No', 'n', 'N', 'no']:
            user_input_limit = int(input(
                'Enter the number of domains that you want to check (It must not exceed the permutations of the letters)\n> '))
        else:
            user_input_limit = 26 ** user_input
        letters_PERM = 26 ** user_input

        object_domain.domain_name_generator()
        object_domain.domain_to_files()
    print('Status: the domain_name list has', len(domain_names) ,'elements')




    path = pathlib.Path(filename)

    if path.is_file() == True:
        user_overwrite = input('Would you like to overwrite existing files?\n> ')
        if user_overwrite in ['No', 'n', 'N', 'no']:
            filename_exist()

    print(filename)
    print(filename2)
    print(filename3)

    file_clear = input('Would you like to clear all the files?\n> ')


    if file_clear in ['yes', 'Yes', 'y', 'Y']:
        file_clear1 = open(filename, 'w')
        file_clear1.close()
        file_clear2 = open(filename2, 'w')
        file_clear2.close()
    elif file_clear in ['No', 'n', 'N', 'no']:
        file_some_clear = input('Would you like to clear a file in specific\n> ')
        if file_some_clear in ['yes', 'Yes', 'y', 'Y']:
            enter_file = input('Enter the exact name of the file:\n> ')
            enter_file = enter_file + '.txt'
            clear_specific(enter_file)




    object_domain = Domain_stuff()
    selenium.bulkPage_run()

    selenium.closeBrowser()
