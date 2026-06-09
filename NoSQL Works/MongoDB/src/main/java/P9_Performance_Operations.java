import com.mongodb.client.*;
import com.mongodb.client.model.Projections;
import org.bson.Document;

public class P9_Performance_Operations {
    public static void main(String[] args) {
        try (MongoClient client = MongoClients.create("mongodb://localhost:27017")) {
            MongoCollection<Document> coll = client.getDatabase("testDB").getCollection("events");

            // Ensure index exists for query field
            coll.createIndex(new Document("userId", 1).append("timestamp", -1));

            // Use projection to return only needed fields
            FindIterable<Document> find = coll.find(new Document("userId", "user123"))
                                              .projection(Projections.fields(
                                                  Projections.include("timestamp", "type"),
                                                  Projections.excludeId()))
                                              .sort(new Document("timestamp", -1))
                                              .limit(50);

            for (Document doc : find) {
                System.out.println(doc.toJson());
            }

            // Use explain to analyze query plan
            Document explain = coll.find(new Document("userId", "user123"))
                                   .projection(Projections.include("timestamp"))
                                   .explain();   // <-- replaces .modifiers()
            System.out.println("Explain (simple): " + explain.toJson());

            // Alternative: run the explain command directly
            Document command = new Document("explain",
                                new Document("find", "events")
                                    .append("filter", new Document("userId", "user123")));
            Document explainCmd = client.getDatabase("testDB").runCommand(command);
            System.out.println("Explain (command): " + explainCmd.toJson());
        }
    }
}
