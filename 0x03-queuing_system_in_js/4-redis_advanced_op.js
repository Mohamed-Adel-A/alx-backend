import { createClient, print } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server:', err.message));

client.on('connect', () => {
  console.log('Redis client connected to the server');

  const KEY = 'HolbertonSchools';

  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(hashObj)) {
    client.hset(hashName, fieldName, fieldValue, print);
  }
  
  client.hgetall(KEY, (err, value) => {
    console.log(value);
  });
});
