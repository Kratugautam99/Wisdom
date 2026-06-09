import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    await client.hSet('user:1000', {
      id: '1000',
      name: 'Alice',
      email: 'alice@example.com',
      points: '120'
    });

    console.log('user:', await client.hGetAll('user:1000'));
    await client.hIncrBy('user:1000', 'points', 30);
    console.log('points after:', await client.hGet('user:1000', 'points'));
    console.log('name:', await client.hGet('user:1000', 'name'));
  } finally {
    await client.quit();
  }
}

run().catch(console.error);
