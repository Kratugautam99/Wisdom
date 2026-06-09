import com.mongodb.client.*;
import com.mongodb.client.model.Filters;
import org.bson.Document;
import org.bson.types.ObjectId;

public class P6_Relationship_Operations {
    public static void main(String[] args) {
        try (MongoClient client = MongoClients.create("mongodb://localhost:27017")) {
            MongoDatabase db = client.getDatabase("testDB");
            MongoCollection<Document> users = db.getCollection("users");
            MongoCollection<Document> posts = db.getCollection("posts");

            // Embedded document example (profile embedded in user)
            Document userEmbedded = new Document("name", "Eve")
                    .append("profile", new Document("bio", "Developer").append("location", "Thane"));
            users.insertOne(userEmbedded);

            // Reference example: create a user and a post that references user _id
            Document userRef = new Document("_id", new ObjectId()).append("name", "Frank");
            users.insertOne(userRef);

            Document post = new Document("title", "Hello")
                    .append("content", "Post content")
                    .append("authorId", userRef.getObjectId("_id")); // reference
            posts.insertOne(post);

            // Reading referenced document (manual join)
            Document foundPost = posts.find(Filters.eq("title", "Hello")).first();
            if (foundPost != null) {
                ObjectId authorId = foundPost.getObjectId("authorId");
                Document author = users.find(Filters.eq("_id", authorId)).first();
                System.out.println("Post: " + foundPost.toJson());
                System.out.println("Author: " + (author != null ? author.toJson() : "not found"));
            }
        }
    }
}
