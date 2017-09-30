
## CENTRAL ACADEMY BACKEND PLUS DIA 4 ##

# 2017-09-29
## HTTP Python

<strong>http://cats</strong>

```python
import urllib

def call_web_url(url):
    request = urllib.urlopen("http://www.google.com")
    content = request.read()
    print(content)
    
```
### Json 

Using json library

```python
import urllib
import json
    
def call_web_api_json(url_api):
    request = urllib.urlopen("https://cdn.rawgit.com/Naramsim/ninjask/master/data/api/v2/pokemon/1/index.json")
    json_data = json.loads(request.read())

```

## Request API
POST request using http://jsonplaceholder.typicode.com/

```python
def call_web_api_json_post():
    values = {
        "userId": 17,
        "id": 17,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    url_api = "http://jsonplaceholder.typicode.com/posts"
    values_bytes = bytes(json.dumps(values).encode('utf-8'))
    post = urllib.request.urlopen(url_api, data=values_bytes)
    content = post.read()
    json_content = json.loads(content)
    return json_content

print(call_web_api_json_post())
```

Tarea: Crear un loggin para nuestras funciones.