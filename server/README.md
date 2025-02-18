# Creddie Webserver

This directory contains the webserver that hosts Creddie.

It is designed to be very simple with the following endpoints.


- `/form` - supports GET method. Displays the form and forwards results to `/log_transaction`  
- `/log_transaction` - Supports POST method. Records the transaction information by appending to the `.csv` file you specified.



## Setup

This project uses [uv](https://docs.astral.sh/uv/) to manage python. 

Make sure you have uv installed.

### Environment Configuration

To run creddie, make sure you create a `.env` file that contains the values you want for all of the variables listed in `creddie/config.py:APISettings`. These variables determine

You can take a look at `example.env` for example variable values.

### Running

Then simply run `start.sh` to start the server locally.



#### Favicon Credit

The favicon for creddie was sourced from [here](https://favicon.io/emoji-favicons/money-bag). And is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
