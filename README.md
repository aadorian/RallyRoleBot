# RallyRoleBot 

A bot for managing roles based on Rally.io holdings. It is ready to be deployed to `heroku` but it can also be deployed elsewhere. For `heroku` it is important that you set the `SECRET_TOKEN` enviroment variable!

* `SECRET_TOKEN` - bot secret token obtained from discord.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Adding the bot to your server

Click this link to add the bot to your server [https://rallybot.app](https://rallybot.app)

Once the bot has been added to your server you need to ensure that it can access and change your roles and channels.

The role for the bot must be above any roles it is meant to manage.

![Bot role above managed roles](docs/Roles.PNG)

The bot must also have permissions for any private channels it needs to manage.

![Bot given permissions in channel](docs/Channel.PNG)

To set role or channel mappings for the bot to manage you must have the administrator privilege on your server.

## Usage

Type `$help` to see a list of commands

## Development

This is a discord bot. To use it you must have a bot set up through
the discord developers portal.


Then simply install the requirements and run `python rallyrolebot/main.py --secret_token <your_secret_token>`

More specifically:

`python3 -m venv venv`

Linux/MacOS: `source venv/bin/activate`
Windows: `.\venv\Scripts\Activate.ps1`

`pip install -r requirements.txt`

`python rallyrolebot/main.py --secret_token <your_secret_token>`

If you run into a Privileged Intents Error, your bot must have the following options enabled
![Privileged Intents Enabled](docs/PrivilegedIntents.PNG) 

## Bot API

The bot also comes with a REST API based on [fastapi](https://fastapi.tiangolo.com/) to allow communication outside of discord.
To start the API you can run `python rallyrolebot/api.py`.
The API should now be available at `http://127.0.0.1:8000` and the API documentation will be available at `/docs` or `/redoc`.

To configure the host and port for the API, include the following arguments:

```sh
python rallyrolebot/api.py --host <custom_host> --port <custom_port>
```

To run the API asynchronously with the bot check [this](https://github.com/Ju99ernaut/RallyRoleBot/blob/api/rallyrolebot/main.py) example.

## Contributing

If contributing to the main repository, please use the Black python package to format all code before submitting a pull request.  

Please DO NOT format all documents in one pull request. Format only the specific code edited per commit. *i.e. Do NOT `black *` from the working folder or the main project directory.

[More info about contributing](https://github.com/CreatorCoinTools/RallyRoleBot/blob/master/CONTRIBUTING.md)
