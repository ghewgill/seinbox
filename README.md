# Stack Exchange headless inbox app

This code can be used to get your Stack Exchange inbox in a headless environment.

## Setup

1. Obtain a Stack Exchange account.
2. Go to http://stackapps.com/apps/oauth/register and add an application (this will be just for you).
3. Application Name: **whatever you like**
4. Description: **whatever**
5. OAuth Domain: `stackexchange.com`
6. Application Website: **whatever, must be a valid domain though**
7. Do *not* check the "Enable Client Side OAuth Flow"
8. Click "Register Your Application"

You will get an application page on Stack Exchange. Copy the information from the application page (Client Id, Client Secret, and Key) to a file called `seinbox.app` (based on `seinbox.app.sample`).

Run `python seinbox.py` to set up your access token (this only needs to be done once). Click on the URL given, approve your app, then copy the resulting code from the URL and paste it into the "code:" prompt. This will then create a file called `seinbox.token` that contains your login token.

# Usage

After doing the above setup, `python seinbox.py` should use the `seinbox.token` that already exists, and print out the inbox information in JSON format to stdout. The token requests has the `no_expiry` scope, so it should not expire.

The `go.py` is a little bit of glue code that connects this with the LED badge from [Codemania](http://codemania.co.nz) using [ledbadge](https://github.com/ghewgill/ledbadge).
