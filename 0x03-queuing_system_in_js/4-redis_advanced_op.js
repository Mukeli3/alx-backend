import { createClient, print } from "redis";
const client = createClient();
import { promisify } from "util";
const hgetall = promisify(client.hgetall).bind(client);

async function setHashvalue() {
  const vals = {
    Portland: 50,
    Seattle: 80,
    New York: 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  };
  for (const i in vals) {
    client.hset("HolbertonSchools", i, vals[i], print);
  }
  
  const res = await hgetall("HolbertonSchools");
  console.log(res);
}

setHashvalue();
