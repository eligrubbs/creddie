# Creddie Server

This directory holds the Creddie webserver.


The Creddie Webserver is a FastAPI application. 

The webserver is not configured to connect asynchrnously to the database you choose to use, because by default it will use sqlite, which is synchronous only. But additionally, who cares about synchronous/async when Creddie is designed for a single user. I add the async keyword even if I don't use await because it can't hurt, and maybe somewhere that I don't know, using async gives some benefits.

Below are a list of features that it has.

Features:
- [X] Start script to launch server v0.1.0
    - Hello World index route
    - test the index route