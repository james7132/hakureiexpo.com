# Hakurei Expo

[Development Discord Server](https://discord.gg/7drdA3j)

Website for Hakurei Expo, a global annual event for doujin creators to share
their works with the community.

## Architecture

 * Frontend: Vue.js Single Page Application
 * Backend: Google Cloud Endpoints REST API built on Google App Engine (Python)

# Project Setup

 * Client (Under the `client` directory):
  * Install node.js and npm
  * Run `npm install` to install required node packages.
 * Server (Under the project root directory):
  * Install python 2.x and pip (NOTE: this project does NOT work with python 3.x+)
  * Make a `lib` folder: (e.g. `mkdir lib`)
  * Run `pip install --target lib --requirement requirements.txt`. You may need
    to execute with escalated priviledges. This may also invoke native binary
    builds. If on Linux, be sure to have the `build-essential` package installed
    on your machine.

## Development

This project is built on Vue.js on the frontend and webapp2, intended to be used
within the Google App Engine enviroment.

Prerequisites:

 * Google Cloud SDK
 * node.js/npm: Only needed for building frontend

To start the frontend, under the `client` directory:

```
npm run serve
```

To start the backend, under the root directory:

```
dev_appserver.py app.yaml
```

This will start a local instance of the backend server, as well as a development
instance of the Cloud Datastore database used.
