import com.mongodb.client.*;
import com.mongodb.client.model.*;
import org.bson.Document;

public class P4_Indexing_Operations {
    public static void main(String[] args) {
        try (MongoClient client = MongoClients.create("mongodb://localhost:27017")) {
            MongoCollection<Document> coll = client.getDatabase("testDB").getCollection("places");

            // Single-field index
            coll.createIndex(Indexes.ascending("name"));

            // Compound index
            coll.createIndex(Indexes.compoundIndex(Indexes.ascending("category"), Indexes.descending("rating")));

            // Text index for search
            coll.createIndex(Indexes.text("description"));

            // Geospatial 2dsphere index
            coll.createIndex(Indexes.geo2dsphere("location"));

            // List indexes
            for (Document idx : coll.listIndexes()) {
                System.out.println(idx.toJson());
            }

            // Drop an index by name (example)
            // coll.dropIndex("name_1");
        }
    }
}
