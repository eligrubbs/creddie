# Creddie Webserver

This directory contains the webserver that hosts Creddie.

It is designed to be very simple with the following endpoints.


- `/form` - supports GET method. Displays the form and forwards results to `/log_transaction`  
- `/log_transaction` - Supports POST method. Records the transaction information by appending to the `.csv` file you specified.

#### Favicon Credit

The favicon for creddie was sourced from [here](https://favicon.io/emoji-favicons/money-bag). And is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
