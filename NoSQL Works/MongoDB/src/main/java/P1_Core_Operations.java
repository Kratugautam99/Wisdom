import com.mongodb.client.*;
import org.bson.Document;
import org.bson.types.ObjectId;
import java.util.Arrays;
import java.util.List;

public class P1_Core_Operations {
    public static void main(String[] args) {
        // Connect to MongoDB (default localhost:27017)
        try (MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017")) {

            // Access database
            MongoDatabase database = mongoClient.getDatabase("testDB");

            // Access collection
            MongoCollection<Document> collection = database.getCollection("users");

            // Use List<String> instead of String[]
            List<String> skills = Arrays.asList("Java", "MongoDB");

            // Create a document with different data types
            Document user = new Document("_id", new ObjectId()) // ObjectId
                    .append("name", "Alice")                   // String
                    .append("age", 25)                         // Integer
                    .append("isActive", true)                  // Boolean
                    .append("skills", skills)                  // List instead of array
                    .append("address", new Document("city", "Mumbai").append("zip", 400001)) // Embedded object
                    .append("joinedDate", new java.util.Date()) // Date
                    .append("notes", null);                    // Null value

            // Insert document into collection
            collection.insertOne(user);

            // Find and print the document
            Document foundUser = collection.find(new Document("name", "Alice")).first();
            System.out.println("Found User: " + foundUser.toJson());
        }
    }
}
