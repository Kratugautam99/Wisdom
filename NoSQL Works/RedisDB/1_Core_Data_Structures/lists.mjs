import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    await client.rPush('queue:tasks', 'task1', 'task2');
    await client.lPush('feed:user', 'post3', 'post2', 'post1');

    console.log('dequeued:', await client.lPop('queue:tasks'));
    console.log('feed:', await client.lRange('feed:user', 0, -1));
  } finally {
    await client.quit();
  }
}

run().catch(console.error);
