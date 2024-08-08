FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
# COPY vuetify-project/package*.json /app

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY app/. /app

# install project dependencies
RUN npm install



# inject all environment vars we'll need
ARG VUE_APP_BACKEND_URL
# expose the variable to the finished cotainer
ENV VUE_APP_BACKEND_URL=$VUE_APP_BACKEND_URL

# build app for production with minification
RUN npm run build

EXPOSE 3000
# CMD [ "http-server", "dist" ]