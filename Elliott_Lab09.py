import unittest
import requests

class MyTestCase(unittest.TestCase):

    def test_ddg(self):
        Presidents = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison",
              "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin Van Buren",
              "William Henry Harrison", "John Tyler", "James K. Polk", "Zachary Taylor",
              "Millard Fillmore", "Franklin Pierce", "James Buchanan", "Abraham Lincoln",
              "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James Garfield",
              "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison", "Grover Cleveland"
              "William McKinley", "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson",
              "Warren G. Harding", "Calvin Coolidge", "Herbert Hoover", "Franklin D. Roosevelt",
              "Harry S. Truman", "Dwight D. Eisenhower", "John F. Kennedy", "Lyndon B. Johnson"
              "Richard M. Nixon", "Gerald R. Ford", "James Carter", "Ronald Reagan"
              "George H. W. Bush", "William J. Clinton", "George W. Bush", "Barrack Obama"
              "Donald Trump", "Joseph R. Biden Jr."]


        url_duckduckgo = "https://api.duckduckgo.com"
        response = requests.get(url_duckduckgo + "/?q=presidents+of+the+united+states&format=json")
        rsp_data = response.json()
        print(rsp_data['RelatedTopics'])
        #assert "George Washington" in rsp_data["RelatedTopics"]
        #assert "John Adams" in rsp_data["RelatedTopics"]


