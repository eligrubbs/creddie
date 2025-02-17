# Creddie Webserver

This directory contains the webserver that hosts Creddie.

It is designed to be very simple with the following endpoints.


`/form` - supports GET method. Displays the form and forwards results to `/record`
`/record` - Supports POST method. Records the transaction information by appending to the `.csv` file you specified.



## Python

This project uses [uv](https://docs.astral.sh/uv/) to manage python. I will update the documentation when I understand the ramifications of this, but for now it is just a note.

Project initialized with the following command:
```
uv init --name creddie --package --no-readme --python-preference only-managed --python 3.12
```


## Setup

To run creddie, make sure you create a `.env` file that contains the values you want for all of the variables listed in `creddie/config.py:APISettings`. These variables determine