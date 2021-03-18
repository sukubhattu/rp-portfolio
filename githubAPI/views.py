from django.shortcuts import render


# import request for calling api
import requests


# Create your views here.
def home(request):
    users = {}
    # Check if the request method is post
    if request.method == "POST":
        # get username from form
        username = request.POST["username"]
        # print(username)
        api_end_point = f"https://api.github.com/search/users?q={username}"
        response = requests.get(api_end_point)
        res1 = response.json()
        users = res1["items"][:20]
        # print(type(users))

    return render(request, "githubAPI/home.html", {"users": users})


def single_user(request):
    user = {}

    # check if request method is post
    if request.method == "POST":
        username = request.POST["username"]
        print(username)
        api_end_point = f"https://api.github.com/users/{username}"
        # send request
        response = requests.get(api_end_point)
        # check if user is actually there
        if response.status_code == 200:
            user = response.json()
            user["rate"] = {
                "limit": response.headers["X-RateLimit-Limit"],
                "remaining": response.headers["X-RateLimit-Remaining"],
            }

        else:
            print("no user found")

        # print(user)

    return render(request, "githubAPI/single.html", {"user": user})
