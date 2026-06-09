import com.mongodb.client.*;
import com.mongodb.client.model.*;
import org.bson.Document;
import org.bson.types.ObjectId;
import com.mongodb.bulk.BulkWriteResult;   // <-- add this

import java.util.Arrays;


public class P2_CRUD_Operations {
    public static void main(String[] args) {
        try (MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017")) {
            MongoDatabase database = mongoClient.getDatabase("testDB");
            MongoCollection<Document> collection = database.getCollection("users");

            // --- CREATE ---
            Document user = new Document("_id", new ObjectId())
                    .append("name", "Bob")
                    .append("age", 30)
                    .append("email", "bob@example.com");
            collection.insertOne(user);
            System.out.println("Inserted: " + user.toJson());

            // --- READ ---
            Document foundUser = collection.find(new Document("name", "Bob")).first();
            System.out.println("Found: " + foundUser.toJson());

            // --- UPDATE ---
            collection.updateOne(
                    Filters.eq("name", "Bob"),
                    Updates.set("age", 31)
            );
            Document updatedUser = collection.find(Filters.eq("name", "Bob")).first();
            System.out.println("Updated: " + updatedUser.toJson());

            // --- DELETE ---
            collection.deleteOne(Filters.eq("name", "Bob"));
            Document deletedUser = collection.find(Filters.eq("name", "Bob")).first();
            System.out.println("After Deletion: " + deletedUser);

            // --- BULK OPERATIONS ---
            BulkWriteResult result = collection.bulkWrite(Arrays.asList(
                    new InsertOneModel<>(new Document("name", "Alice").append("age", 25)),
                    new InsertOneModel<>(new Document("name", "Charlie").append("age", 28)),
                    new UpdateOneModel<>(Filters.eq("name", "Alice"), Updates.set("age", 26)),
                    new DeleteOneModel<>(Filters.eq("name", "Charlie"))
            ));
            System.out.println("Bulk operation result: " + result);
        }
    }
}
