from facebook import GraphAPI

token = "your access token"
graph = GraphAPI(token)

j = graph.getcontent(id="your id", data="posts.limit(10)")
print(j)