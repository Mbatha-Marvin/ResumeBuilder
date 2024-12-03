FROM node:20-alpine3.19

WORKDIR /app

COPY package.json .

RUN yarn install

COPY . .

EXPOSE 5173

# CMD ["yarn" "dev" "-o"]
