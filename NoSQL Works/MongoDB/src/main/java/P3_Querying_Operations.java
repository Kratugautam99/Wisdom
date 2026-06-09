import com.mongodb.client.*;
import com.mongodb.client.model.*;
import org.bson.Document;
import java.util.Arrays;

public class P3_Querying_Operations {
    public static void main(String[] args) {
        try (MongoClient client = MongoClients.create("mongodb://localhost:27017")) {
            MongoCollection<Document> coll = client.getDatabase("testDB").getCollection("products");

            // Insert sample docs (idempotent for demo)
            coll.insertMany(Arrays.asList(
                new Document("name", "Apple").append("price", 120).append("tags", Arrays.asList("fruit","food")),
                new Document("name", "Banana").append("price", 40).append("tags", Arrays.asList("fruit")),
                new Document("name", "Laptop").append("price", 55000).append("tags", Arrays.asList("electronics"))
            ));

            // Operators: $eq, $gt, $in, $regex
            Document filter = new Document("$and", Arrays.asList(
                new Document("price", new Document("$gt", 100)),
                new Document("tags", new Document("$in", Arrays.asList("fruit", "electronics"))),
                new Document("name", new Document("$regex", "^A").append("$options", "i"))
            ));

            // Projection: include name and price only
            Document projection = new Document("name", 1).append("price", 1).append("_id", 0);

            // Sorting: price descending
            FindIterable<Document> results = coll.find(filter)
                                                 .projection(projection)
                                                 .sort(Sorts.descending("price"));

            for (Document d : results) {
                System.out.println(d.toJson());
            }
        }
    }
}
