import unittest
from flask import Flask
from flask_classy import FlaskView, route

class BasicTestView(FlaskView):

    def index(self):
        return "Index"

    def get(self, id):
        return "Get " + id

    def put(self, id):
        return "Put " + id

    def post(self):
        return "Post"

    def delete(self, id):
        return "Delete " + id

    def other_method(self):
        return "Other Method"

    @route("/another")
    def another_method(self):
        return "Another Method"

class IndexTestView(FlaskView):
    route_base = "/"

    def index(self):
        return "Home Page"

class CommonTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        BasicTestView.register(self.app)
        IndexTestView.register(self.app)

    def test_basic_index(self):
        res = self.client.get("/basictest/")
        self.assertEqual("Index", res.data)

    def test_basic_get(self):
        res = self.client.get("/basictest/1234/")
        self.assertEqual("Get 1234", res.data)

    def test_basic_put(self):
        res = self.client.put("/basictest/1234/")
        self.assertEqual("Put 1234", res.data)

    def test_basic_post(self):
        res = self.client.post("/basictest/")
        self.assertEqual("Post", res.data)

    def test_basic_delete(self):
        res = self.client.delete("/basictest/1234/")
        self.assertEqual("Delete 1234", res.data)

    def test_basic_method(self):
        res = self.client.get("/basictest/other_method/")
        self.assertEqual("Other Method", res.data)

    def test_routed_method(self):
        res = self.client.get("/basictest/another")
        self.assertEqual("Another Method", res.data)

        #.Make sure the automatic route wasn't generated
        res = self.client.get("/basictest/another_method/")
        self.assertNotEqual("Another Method", res.data)

    def test_index_route_base(self):
        res = self.client.get("/")
        self.assertEqual("Home Page", res.data)

    def tearDown(self):
        pass

if __name__ == "main":
    unittest.main()