FROM node:18.16.0-alpine3.18

WORKDIR /app

COPY package.json .

RUN yarn install

COPY . .

EXPOSE 5173

# CMD ["npm", "run", "dev"]