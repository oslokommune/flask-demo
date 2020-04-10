from app import hello


from aws_xray_sdk.core import xray_recorder

xray_recorder.begin_segment("Test")


class TestApp:
    def test_hello(self):
        response = hello()
        assert response == "Hello, world!"
