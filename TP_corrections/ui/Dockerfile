FROM node:lts AS development

WORKDIR /app

# 
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

# Same as npm install
RUN npm ci

COPY . /app

EXPOSE 5173

CMD [ "npm", "run", "dev" ]