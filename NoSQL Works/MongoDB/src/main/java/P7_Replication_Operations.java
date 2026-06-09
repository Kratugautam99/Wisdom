import com.mongodb.client.*;
import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;

public class P7_Replication_Operations{
    public static void main(String[] args) {
        // Replica set connection string (example)
        String replicaUri = "mongodb://host1:27017,host2:27017,host3:27017/?replicaSet=rs0";

        // Sharded cluster connection string (mongos routers)
        String shardedUri = "mongodb://mongos1:27017,mongos2:27017/?readPreference=primaryPreferred";

        // Build settings and create client for replica set
        ConnectionString cs = new ConnectionString(replicaUri);
        MongoClientSettings settings = MongoClientSettings.builder()
                .applyConnectionString(cs)
                .build();

        try (MongoClient client = MongoClients.create(settings)) {
            MongoDatabase db = client.getDatabase("testDB");
            System.out.println("Connected to: " + db.getName());
            // Normal operations proceed the same; driver handles replica/shard topology.
        }
    }
}
