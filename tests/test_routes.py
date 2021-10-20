import pytest


def test_add_user(client):
  res = client.post('/user', headers={'Content-Type': 'application/json'})

  assert res.status_code == 200
  assert b'"name":"Fred"' in res.data 


def test_user(client):
  res = client.get('/user', headers={'Content-Type': 'application/json'})

  assert res.status_code == 200
  assert b'[]' in res.data 
