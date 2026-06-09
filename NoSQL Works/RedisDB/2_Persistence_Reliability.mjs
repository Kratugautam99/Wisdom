import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    // --- RDB Snapshot Trigger ---
    const saveResult = await client.sendCommand(['SAVE']);
    console.log('RDB snapshot triggered:', saveResult);

    // --- AOF Rewrite Trigger ---
    const aofResult = await client.sendCommand(['BGREWRITEAOF']);
    console.log('AOF rewrite triggered:', aofResult);

    // --- Persistence Tuning ---
    const configSave = await client.configGet('save');
    const configAppendfsync = await client.configGet('appendfsync');
    console.log('Current RDB save policy:', configSave);
    console.log('Current AOF fsync policy:', configAppendfsync);

    // Adjust snapshot frequency (save every 60s if at least 100 changes)
    await client.configSet('save', '60 100');
    console.log('Updated RDB save policy:', await client.configGet('save'));

    // --- Replication ---
    const replicationInfo = await client.info('replication');
    console.log('Replication info:\n', replicationInfo);

    // Example: connect this node as a replica
    // await client.sendCommand(['REPLICAOF', '127.0.0.1', '6379']);
    // await client.sendCommand(['REPLICAOF', 'NO', 'ONE']); // disable replication
  } finally {
    await client.quit();
  }
}

run().catch(console.error);
