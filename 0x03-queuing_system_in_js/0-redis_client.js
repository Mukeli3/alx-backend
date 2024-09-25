import { createClient } from 'redis';

const client = createClient(); // create a Redis client

// successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

//unsuccessful
client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});
