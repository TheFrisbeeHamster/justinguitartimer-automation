from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def read_lines_from_txt_file(filename):
    """Reads in the text file and saves every line in a list."""
    lines = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            lines.append(line)
    return lines


def open_new_tabs(driver, links):
    """Opens new tabs for every link in the links list."""
    for link in links:
        nr_tabs = len(driver.window_handles)
        if links.index(link) >= 1:
            driver.execute_script('window.open('');')

    for i in range(len(links)):
        driver.switch_to.window(driver.window_handles[i])
        driver.get(links[i])


def open_guitar_timer(driver):
    """Opens the JustinGuitar timer and returns the minute+ and the start buttons."""
    # driver.execute_script('window.open('');')
    # driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])
    driver.get('https://old.justinguitar.com/apps/timer/index.html')
    min_plus = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/input[1]')
    sec_plus = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/input[3]')
    start_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/input[1]')
    time.sleep(3)
    return min_plus, sec_plus, start_button


def create_intervals(min_plus, sec_plus, start_button, intervals):
    """Only creates an interval but doesn't start it."""
    for interval in intervals:
        interval = interval.split(':')
        create_and_start_interval(min_plus, sec_plus, interval)
        start_button.click()
        try:
            time.sleep(int(interval[0]) * 60 + int(interval[1]) + 3)
        except:
            time.sleep(int(interval[0]) * 60 + 3)



def create_and_start_interval(min_plus, sec_plus, interval):
    """Creates and starts an interval in the JustinGuitar timer."""
    for i in range(int(interval[0])):
        min_plus.click()
    try:
        for i in range(int(interval[1])):
            sec_plus.click()
    except:
        return



# Read the YouTube links for the backing tracks to be loaded
# links = read_lines_from_txt_file('links.txt')

# Open Chrome
chrome_driver = 'D:\Downloads\Treiber\chromedriver.exe'
options = Options()
options.page_load_strategy = 'none'
options.add_argument('user-data-dir=C:\\Users\Andreas\AppData\Local\Google\Chrome\\User Data\Default')
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(chrome_driver, options=options)
driver.maximize_window()

# Open the links from the link list
# open_new_tabs(driver, links)

# Read in the intervals from the text file
intervals = read_lines_from_txt_file('intervals.txt')

# Open JustinGuitar timer
min_plus, sec_plus, start_button = open_guitar_timer(driver)

create_intervals(min_plus, sec_plus, start_button, intervals)
