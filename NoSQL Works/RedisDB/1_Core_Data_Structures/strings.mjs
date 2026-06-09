import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    await client.set('session:token:abc', 'xyz123');
    console.log('token:', await client.get('session:token:abc'));

    await client.set('page:views', 0);
    await client.incr('page:views');
    await client.incrBy('page:views', 5);
    console.log('page views:', await client.get('page:views'));

    const old = await client.getSet('config:version', 'v2.0');
    console.log('old config version:', old);

    await client.set('cache:item:42', JSON.stringify({ name: 'Widget' }), { EX: 60 });
    console.log('cache TTL:', await client.ttl('cache:item:42'));
  } finally {
    await client.quit();
  }
}

run().catch(console.error);
