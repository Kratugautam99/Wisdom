import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    const streamKey = 'mystream';

    const id1 = await client.xAdd(streamKey, '*', { type: 'order', orderId: 'A1', amount: '100' });
    const id2 = await client.xAdd(streamKey, '*', { type: 'order', orderId: 'A2', amount: '200' });
    console.log('added ids:', id1, id2);

    console.log('entries:', await client.xRange(streamKey, '-', '+', { COUNT: 10 }));

    try {
      await client.xGroupCreate(streamKey, 'workers', '$', { MKSTREAM: true });
    } catch {}

    const read = await client.xReadGroup('workers', 'consumer-1', [{ key: streamKey, id: '>' }], { COUNT: 10, BLOCK: 2000 });
    console.log('xreadgroup result:', read);

    if (read) {
      for (const stream of read) {
        for (const [id] of stream.messages) {
          await client.xAck(streamKey, 'workers', id);
        }
      }
    }
  } finally {
    await client.quit();
  }
}

run().catch(console.error);
