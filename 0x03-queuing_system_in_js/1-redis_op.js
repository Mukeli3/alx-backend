import { createClient, print } from 'redis';

const client = createClient(); // create a Redis client

// successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// unsuccessful
client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
  client.get(schoolName, print);
}

function displaySchoolValue(schoolName) {
  console.log(schoolName);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
