import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    await client.sAdd('tags:item:100', 'redis', 'nodejs', 'database');
    await client.sAdd('tags:item:101', 'redis', 'caching');

    console.log('is redis a tag?', await client.sIsMember('tags:item:100', 'redis'));
    console.log('common tags:', await client.sInter('tags:item:100', 'tags:item:101'));
    console.log('all tags:', await client.sUnion('tags:item:100', 'tags:item:101'));
    console.log('random tag:', await client.sRandMember('tags:item:100'));
  } finally {
    await client.quit();
  }
}

run().catch(console.error);
