FROM node:22.5-alpine3.20

# Set the working directory inside the container
WORKDIR /app

COPY package.json .

RUN yarn install

COPY . .

EXPOSE 5173

CMD ["yarn" "dev" "-o"]
