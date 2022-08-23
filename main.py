#from flask import Flask, current_app, redirect, url_for, request
from tokenize import String
import requests
from fastapi import FastAPI
import instaloader
from instaloader import Profile

app = FastAPI()
L = instaloader.Instaloader()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/count_followers/{item}")
def count_followers(item):
    profile = Profile.from_username(L.context,item )
    print(profile.followers)
    #print(profile.get_posts())
    print(profile.biography)
    print(profile.followed_by_viewer)
    profile.full_name
    s = "Count followers :" + str(profile.followers) + "| Biografy :" + profile.biography + " | Full name :" + profile.full_name + str(profile.has_viewable_story)
    return s 

def requestInYandex():
    req = requests.get("https://ya.ru/")
    print(req.cookies)
    print(req.text)
#requestInYandex()