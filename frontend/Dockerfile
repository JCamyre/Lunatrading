FROM node:14.17.0-alpine

WORKDIR /app/frontend

ENV PATH /app/frontend/node_modules/.bin:$PATH

COPY package.json ./

COPY package-lock.json ./

RUN npm install --silent

RUN npm install react-scripts@3.4.1 -g --silent

COPY . ./

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]