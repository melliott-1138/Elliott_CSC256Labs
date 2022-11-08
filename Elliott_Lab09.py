import unittest
import requests

class MyTestCase(unittest.TestCase):

    def test_ddg1(self):
        presidents = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison",
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

        duckduckgo = "https://api.duckduckgo.com"
        response = requests.get(duckduckgo + "/?q=presidents+of+the+united+states&format=json")
        rsp_data = response.json()
        related = rsp_data['RelatedTopics']
        q = related[0]
        w = q['Text']

        print(q)
        assert "Lincoln" in w
