FROM node:12.18.1-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install -g vue-cli
RUN npm install axios -f
RUN npm install vee-validate -f
RUN npm install sweetalert -f
RUN npm install
COPY . .
RUN npm run build
CMD cp -r dist/. result_build
