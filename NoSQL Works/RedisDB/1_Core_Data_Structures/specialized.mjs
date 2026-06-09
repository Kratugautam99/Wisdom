import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    // Bitmaps
    await client.setBit('bitmap:day:2026-06-08', 42, 1);
    await client.setBit('bitmap:day:2026-06-08', 100, 1);
    console.log('bit 42:', await client.getBit('bitmap:day:2026-06-08', 42));
    console.log('active count:', await client.bitCount('bitmap:day:2026-06-08'));

    // HyperLogLog
    await client.pfAdd('hll:visitors', 'u1', 'u2', 'u3', 'u2');
    console.log('approx unique visitors:', await client.pfCount('hll:visitors'));

    // Geospatial
    await client.geoAdd('places', { longitude: 72.8777, latitude: 19.0760, member: 'Mumbai' });
    await client.geoAdd('places', { longitude: 77.1025, latitude: 28.7041, member: 'Delhi' });
    console.log('Mumbai-Delhi distance km:', await client.geoDist('places', 'Mumbai', 'Delhi', 'km'));

    // Correct way: use geoSearch
    const nearby = await client.geoSearch(
      'places',
      { longitude: 72.8777, latitude: 19.0760 }, // center point
      { radius: 2000, unit: 'km' },              // search radius
      { WITHDIST: true, COUNT: 10 }              // options
    );
    console.log('nearby:', nearby);
  } finally {
    await client.quit();
  }
}

run().catch(console.error);
