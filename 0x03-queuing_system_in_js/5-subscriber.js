#!/usr/bin/yarn dev
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const publishMsg = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
};

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

publishMsg('Holberton Student #1 starts course', 100);
publishMsg('Holberton Student #2 starts course', 200);
publishMsg('KILL_SERVER', 300);
publishMsg('Holberton Student #3 starts course', 400);
