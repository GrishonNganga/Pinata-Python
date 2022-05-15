from src.pinata import Pinata
import pytest

class TestPinata():

    @pytest.fixture
    def pinata_inputs(self):
        api_key = "7a1f59937cb69ffa86f9"     
        secret_key = "f6bfbb866bbe665dbd325cf88c4c3436debfca419d6d9e81e0bf0e01f3509db1"
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIwZTI2NTk0NC1hMTgzLTRlMjgtODA5NS1iYzRkNDZkMmJmYjEiLCJlbWFpbCI6ImdyaXNob24ubmdhbmdhMDFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJGUkExIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZX0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6Ijg3ZGZkN2Q4Yjk2NzczYzJmMWNmIiwic2NvcGVkS2V5U2VjcmV0IjoiZDdmMWIyY2QyZjRjOTQ2ZWU3ZTc0M2VkZmY0NmUxYzg0MmM4OTE1Yjc2ZjliOTNmZDI3YTgwYjhlYTFiNmVlYiIsImlhdCI6MTY1MjYyOTQzMH0.23CN11cmQSCI1TsJyipVD8e4acBa732yno-IemrvC2U"

        return {'api_key': api_key, 'secret_key': secret_key, 'access_token': access_token}

    def test_no_credentials(self):
        pinata = Pinata("", "", "")
        pins = pinata.get_pins()
        assert pins["status"], "error"

    def test_missing_access_token(self, pinata_inputs):
        api_key = pinata_inputs["api_key"]
        secret_key = pinata_inputs["secret_key"]
        access_token = pinata_inputs["access_token"]
        pinata = Pinata(api_key, secret_key, access_token)
        pins = pinata.get_pins()
        assert pins["status"], "error"


    def test_get_pins_success(self, pinata_inputs):
        api_key = pinata_inputs["api_key"]
        secret_key = pinata_inputs["secret_key"]
        access_token = pinata_inputs["access_token"]
        pinata = Pinata(api_key, secret_key, access_token)
        pins = pinata.get_pins()
        assert (pins["status"] == "success")

    def test_pin_nonexistent_local_file(self, pinata_inputs):
        api_key = pinata_inputs["api_key"]
        secret_key = pinata_inputs["secret_key"]
        access_token = pinata_inputs["access_token"]
        pinata = Pinata(api_key, secret_key, access_token)
        pins = pinata.pin_file('non_existent_file.txt')
        assert (pins["status"] == "error")
        assert (pins["message"] == 'File does not exist')

    def test_pin_file_success(self, pinata_inputs):
        api_key = pinata_inputs["api_key"]
        secret_key = pinata_inputs["secret_key"]
        access_token = pinata_inputs["access_token"]
        pinata = Pinata(api_key, secret_key, access_token)
        open("test.txt", 'w').write("Test file")
        pin = pinata.pin_file('/tmp/test.txt')
        assert(pin['status'] == "success")

    def test_unip_non_existent_file(self, pinata_inputs):
        api_key = pinata_inputs["api_key"]
        secret_key = pinata_inputs["secret_key"]
        access_token = pinata_inputs["access_token"]
        pinata = Pinata(api_key, secret_key, access_token)
        unpin = pinata.unpin_file("xxxxxxxxxxxxxxxxxxxxxxx")
        assert(unpin['status'] == 'error')
        assert(unpin['message'] == 'The current user has not pinned the cid: xxxxxxxxxxxxxxxxxxxxxxx')

    def test_unpin_file_success(self, pinata_inputs):
        api_key = pinata_inputs["api_key"]
        secret_key = pinata_inputs["secret_key"]
        access_token = pinata_inputs["access_token"]
        pinata = Pinata(api_key, secret_key, access_token)
        open("test.txt", 'w').write("Test file")
        pin = pinata.pin_file('/tmp/test.txt')
        unpin = pinata.unpin_file(pin['data']['IpfsHash'])
        assert(unpin['status'] == 'success')