import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    // --- Pub/Sub ---
    const subscriber = client.duplicate();
    await subscriber.connect();

    await subscriber.subscribe('news', (message) => {
      console.log('Received message on news channel:', message);
    });

    await client.publish('news', 'Breaking update: Redis is powerful!');
    await client.publish('news', 'Another event just happened.');

    // --- Lua Scripting ---
    const script = `
      local current = redis.call("GET", KEYS[1])
      if not current then
        redis.call("SET", KEYS[1], ARGV[1])
        return ARGV[1]
      else
        local newVal = current + ARGV[1]
        redis.call("SET", KEYS[1], newVal)
        return newVal
      end
    `;
    const result = await client.eval(script, {
      keys: ['counter'],
      arguments: ['5']
    });
    console.log('Lua script result (counter):', result);

    // --- Modules (RedisJSON, RediSearch) ---
    // Requires RedisJSON and RediSearch modules loaded in your Redis server.
    // JSON example
    await client.sendCommand(['JSON.SET', 'doc:1', '$', '{"title":"Redis Guide","views":100}']);
    const jsonDoc = await client.sendCommand(['JSON.GET', 'doc:1']);
    console.log('JSON doc:', jsonDoc);

    // RediSearch example: create index and query
    try {
      await client.sendCommand(['FT.CREATE', 'idx', 'ON', 'JSON', 'SCHEMA', '$.title', 'TEXT', '$.views', 'NUMERIC']);
    } catch {
      // ignore if already exists
    }
    await client.sendCommand(['FT.SEARCH', 'idx', 'Redis']);
    console.log('Search results for "Redis" done.');

    // --- Vector Search (GenAI embeddings) ---
    // Requires RediSearch with vector field support.
    // Example: store embedding vectors and query nearest neighbors.
    try {
      await client.sendCommand([
        'FT.CREATE', 'vec_idx', 'ON', 'HASH',
        'SCHEMA', 'embedding', 'VECTOR', 'HNSW', '6', 'TYPE', 'FLOAT32', 'DIM', '4', 'DISTANCE_METRIC', 'COSINE'
      ]);
    } catch {
      // ignore if already exists
    }

    // Insert a vector (4-dim float array encoded as binary)
    const buf = Buffer.from(new Float32Array([0.1, 0.2, 0.3, 0.4]).buffer);
    await client.hSet('vec:1', { embedding: buf.toString('base64') });

    // Query nearest neighbors
    const queryRes = await client.sendCommand([
      'FT.SEARCH', 'vec_idx',
      '*=>[KNN 1 @embedding $BLOB]',
      'PARAMS', '2', 'BLOB', buf.toString('base64'),
      'DIALECT', '2'
    ]);
    console.log('Vector search result:', queryRes);

  } finally {
    await client.quit();
  }
}

run().catch(console.error);
