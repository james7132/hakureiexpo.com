# Hakurei Expo

[Development Discord Server](https://discord.gg/7drdA3j)

Website for Hakurei Expo, a global annual event for doujin creators to share
their works with the community.

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
