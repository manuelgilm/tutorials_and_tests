FROM node:18-alpine
RUN mkdir frontend
WORKDIR /frontend 
COPY . /frontend/
RUN npm install 
# Expose the port the app runs in
EXPOSE 5137

CMD ["npm", "run", "dev","--","--host","0.0.0.0", "--port", "5137"]