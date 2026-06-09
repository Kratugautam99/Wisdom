import { createClient } from 'redis';

async function run() {
  const client = createClient();
  await client.connect();

  try {
    // Add members with scores
    await client.zAdd('leaderboard', [
      { score: 1500, value: 'player:1' },
      { score: 2000, value: 'player:2' },
      { score: 1800, value: 'player:3' }
    ]);

    // Get top 3 players (highest scores)
    const top = await client.zRangeWithScores('leaderboard', 0, 2, { REV: true });
    console.log('Top players:', top);

    // Increment score
    await client.zIncrBy('leaderboard', 50, 'player:1');
    console.log('player:1 new score:', await client.zScore('leaderboard', 'player:1'));

    // Rank (0-based, reverse order)
    const rank = await client.zRevRank('leaderboard', 'player:1');
    console.log('player:1 rank:', rank);
  } finally {
    await client.quit();
  }
}

run().catch(console.error);
