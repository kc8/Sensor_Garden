from graphene import ObjectType, String, Schema
from google.cloud import firestore



class Query(ObjectType): 
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(root, info, name):
        return f'Hello {name}'

    def resolve_goodbye(root, info):
        return f'Peace @ bro!'



def main(request):
    data = request.get_json()
    ask = data['ask']
    return str(ask)


if __name__ == '__main__': 
    schema = Schema(query=Query)
    app.run(host='127.0.0.1', port=8080, debug=True)

#query_string = '{hello(name: "Kyle")}'
#result = schema.execute(query_string)
#print(result.data['hello'])
