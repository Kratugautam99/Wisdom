import { createClient } from 'redis';

async function run() {
  // --- Authentication & ACLs ---
  // If Redis requires a password or ACL user, provide it in the URL
  const client = createClient({
    url: 'redis://default:yourpassword@localhost:6379'
    // For ACLs: 'redis://username:password@host:port'
  });

  await client.connect();

  try {
    // Test access
    await client.set('secure:key', 'secret');
    console.log('secure:key =', await client.get('secure:key'));

    // --- TLS/SSL Encryption ---
    // Requires Redis server configured with TLS certificates.
    // Example connection (replace with actual certs):
    /*
    const tlsClient = createClient({
      socket: {
        tls: true,
        ca: [fs.readFileSync('ca.crt')],
        cert: fs.readFileSync('client.crt'),
        key: fs.readFileSync('client.key')
      },
      url: 'rediss://localhost:6380'
    });
    await tlsClient.connect();
    */

    // --- Debugging & Profiling ---
    // Slow query log: configure in redis.conf (slowlog-log-slower-than, slowlog-max-len)
    // Inspect slow queries
    const slowlog = await client.sendCommand(['SLOWLOG', 'GET', '10']);
    console.log('Slowlog entries:', slowlog);

    // INFO command for profiling
    const infoStats = await client.info('stats');
    console.log('Stats info:\n', infoStats);

    // MONITOR (verbose, dev only)
    const monitorClient = client.duplicate();
    await monitorClient.connect();
    monitorClient.monitor((err, monitor) => {
      if (err) throw err;
      console.log('Monitoring started...');
      monitor.on('monitor', (time, args, source, db) => {
        console.log(time, args);
      });
    });

    // Stop monitoring after 3 seconds
    setTimeout(async () => {
      await monitorClient.quit();
      console.log('Monitoring stopped.');
    }, 3000);

  } finally {
    // Quit main client after delay to allow monitor demo
    setTimeout(async () => {
      await client.quit();
    }, 4000);
  }
}

run().catch(console.error);
