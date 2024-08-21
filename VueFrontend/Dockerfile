
FROM node:22.5-alpine3.20

# Set the working directory inside the container
WORKDIR /app
# Copy the output from the build stage to the working directory
COPY .output .

# Define environment variables
ENV HOST=0.0.0.0 NODE_ENV=production
ENV NODE_ENV=production

# Expose the port the application will run on
EXPOSE 3000

# Start the application
CMD ["node","/app/server/index.mjs"]
