import { createClient, print } from 'redis';
import { promisify } from "util";

const client = createClient(); // create a Redis client
const getAsync = promisify(client.get).bind(client); // promisify after creating client

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

async function displaySchoolValue(schoolName) {
  const res = await getAsync(schoolName);
	console.log(res);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

