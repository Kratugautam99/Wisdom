import { createClient } from 'redis';

async function run() {
  // Connect to Redis (could be a Sentinel-managed endpoint or a cluster node)
  const client = createClient({ url: 'redis://localhost:6379' });
  await client.connect();

  try {
    // --- Sentinel Monitoring ---
    // If connected to a Sentinel instance, you can query monitored masters
    // Example: client.sendCommand(['SENTINEL', 'masters'])
    try {
      const masters = await client.sendCommand(['SENTINEL', 'masters']);
      console.log('Sentinel masters:', masters);
    } catch {
      console.log('Not connected to a Sentinel instance.');
    }

    // --- Clustering ---
    // Query cluster info if connected to a cluster-enabled Redis
    try {
      const clusterInfo = await client.sendCommand(['CLUSTER', 'INFO']);
      console.log('Cluster info:\n', clusterInfo);

      const slots = await client.sendCommand(['CLUSTER', 'SLOTS']);
      console.log('Cluster slots:', slots);
    } catch {
      console.log('Not connected to a cluster-enabled Redis.');
    }

    // --- Sharding Strategies ---
    // Sharding is about distributing keys. A simple strategy is to prefix keys.
    await client.set('user:1:name', 'Alice');
    await client.set('user:2:name', 'Bob');
    await client.set('order:100:amount', '250');
    await client.set('order:101:amount', '400');

    console.log('user:1:name =', await client.get('user:1:name'));
    console.log('order:101:amount =', await client.get('order:101:amount'));

    // In a real cluster, these prefixes help distribute keys across slots/nodes.
  } finally {
    await client.quit();
  }
}

run().catch(console.error);
