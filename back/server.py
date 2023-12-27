from blacksheep import Application, get, post

app = Application()


@get("/")
def home(request):
    return "GET Example"


@get("/name")
def greetings(name: str):
    return f"Hello, {name}!"


@post("/")
def post_example(request):
    return "POST Example"
