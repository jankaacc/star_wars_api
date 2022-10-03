FROM node:14.17-alpine

# RUN mkdir -p /usr/src/app
# WORKDIR /usr/src/app

# ENV LOG_LEVEL=info \
#     NATS_CLUSTER="test-cluster" \
#     NATS_SERVER="nats://localhost:4222" \
#     REDIS_URL="redis://localhost:6379" \
#     NODE_ENV=production \
#     COOKIE_MAX_AGE=3600000 \
#     COOKIE_SECURE=false \
#     SESSION_SECRET=shhhhhhh \
#     PORT=3000

# COPY package.json yarn.lock /usr/src/app/
# RUN yarn install &&\
#     chown -R node:node /usr/src/app

# COPY . /usr/src/app
# RUN yarn run build

# USER node

# CMD ["yarn", "start"]


RUN mkdir -p /app && \
      chown node:node /app -R

USER node

WORKDIR /app

COPY --chown=node:node package.json package-lock.json /app/

# when NODE_ENV is set to production, it will not install devDependencies
RUN npm install --production=false

COPY --chown=node:node . /app

RUN npm run build

CMD ["npm", "run", "start"]