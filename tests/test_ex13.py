import requests
import json
import pytest
import yaml
y = open("../configs/config.yaml")
yaml_conf = yaml.safe_load(y)

@pytest.mark.parametrize("agent", [i for i in yaml_conf])
def test_ex13(agent):
    request = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": yaml_conf.get(agent).get('User-Agent')}).content
    response = json.loads(request)
    assert yaml_conf.get(agent).get('platform') in response['platform'], f"Wrong response param value 'platform': {response['platform']}"
    assert yaml_conf.get(agent).get('browser') in response['browser'], f"Wrong response param value 'browser': {response['browser']}"
    assert yaml_conf.get(agent).get('device') in response['device'], f"Wrong response param value 'platform': {response['device']}"