import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.client.*;

public class P8_Security_Operations {
    public static void main(String[] args) {
        // Example: SCRAM auth with TLS
        String uri = "mongodb://appUser:secretPassword@dbhost:27017/?authSource=admin&tls=true";

        ConnectionString conn = new ConnectionString(uri);
        MongoClientSettings settings = MongoClientSettings.builder()
                .applyConnectionString(conn)
                .build();

        try (MongoClient client = MongoClients.create(settings)) {
            MongoDatabase db = client.getDatabase("secureDB");
            System.out.println("Authenticated and connected to: " + db.getName());
            // Ensure server has TLS configured and user roles set up on server side.
        }
    }
}
