from urllib import response


try:
    from tests.__common__ import *
except:
    from __common__ import *


class BasicFunction(unittest.TestCase):
    def setUp(self) -> None:
        root = "http://localhost"
        port = "10219"
        self.base_url = f"{root}:{port}"
        return super().setUp()

    def test_ping(self):
        url = self.get_url("/ping")
        res = requests.get(url)
        self.print_result(res)

    def test_sing_up(self):
        url = self.get_url("/sign-up")
        param = {"name": "test1", "age": 12}
        res = requests.post(url, json=param)
        self.print_result(res)

    def test_wrong_route(self):
        url = self.get_url("/wrong")
        res = requests.get(url, timeout=3)
        self.print_result(res)

    def test_tweet_over_300(self):
        url = self.get_url("/tweet-300")
        param = {"id": 1, "tweet": "".join(["안녕하세요. 저는 300자가 넘어요."] * 30)}
        res = requests.post(url, json=param)
        self.print_result(res)

    def test_tweet_under_300(self):
        url = self.get_url("/tweet-300")
        param = {"id": 1, "tweet": "".join(["안녕하세요. 저는 300자가 넘어요."])}
        res = requests.post(url, json=param)
        self.print_result(res)

    def get_url(self, route):
        url = self.base_url + route
        cPrint("TARGET : ", styles=["header"], end="")
        cPrint(route, styles=["okblue", "underline", "bold"])
        return self.base_url + route

    @staticmethod
    def print_result(res: requests.Response):
        color = "fail" if res.status_code > 300 else "okgreen"
        cPrint(res.status_code, styles=[color], end=" ")
        cPrint(res.reason, styles=[color, "underline"])
        cPrint(res.text, color="yellow")
        print()


if __name__ == "__main__":
    unittest.main()
