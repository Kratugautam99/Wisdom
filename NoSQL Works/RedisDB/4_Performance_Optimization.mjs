import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    // --- Eviction Policies ---
    // Eviction policies are configured at the server level (redis.conf).
    // Here we demonstrate TTL-based expiration.
    await client.set('temp:key', 'value', { EX: 5 }); // expires in 5 seconds
    console.log('temp:key TTL:', await client.ttl('temp:key'));

    // --- Memory Management ---
    // Inspect memory usage of a key
    await client.set('big:key', 'some large value repeated'.repeat(100));
    console.log('Memory usage of big:key:', await client.memoryUsage('big:key'));

    // General memory info
    const memInfo = await client.info('memory');
    console.log('Memory info:\n', memInfo);

    // --- Pipelining ---
    // Batch multiple commands to reduce network overhead
    const pipeline = client.multi();
    pipeline.set('pipe:key1', 'v1');
    pipeline.set('pipe:key2', 'v2');
    pipeline.get('pipe:key1');
    pipeline.get('pipe:key2');
    const results = await pipeline.exec();
    console.log('Pipeline results:', results);

    // --- Monitoring Tools ---
    // INFO provides server statistics
    const serverInfo = await client.info();
    console.log('Server info:\n', serverInfo);

    // MONITOR streams every command (use carefully!)
    // Example: run for 3 seconds then stop
    const monitorClient = client.duplicate();
    await monitorClient.connect();
    monitorClient.monitor((err, monitor) => {
      if (err) throw err;
      console.log('Entering monitoring mode...');
      monitor.on('monitor', (time, args, source, database) => {
        console.log(time, args);
      });
    });

    // Stop monitoring after 3 seconds
    setTimeout(async () => {
      await monitorClient.quit();
      console.log('Stopped monitoring.');
    }, 3000);

  } finally {
    // Quit main client after delay to allow monitor demo
    setTimeout(async () => {
      await client.quit();
    }, 4000);
  }
}

run().catch(console.error);
