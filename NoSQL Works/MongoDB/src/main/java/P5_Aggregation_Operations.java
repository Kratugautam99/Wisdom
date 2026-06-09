import com.mongodb.client.*;
import com.mongodb.client.model.*;
import org.bson.Document;
import org.bson.conversions.Bson;   // <-- add this

import java.util.Arrays;
import java.util.List;

public class P5_Aggregation_Operations {
    public static void main(String[] args) {
        try (MongoClient client = MongoClients.create("mongodb://localhost:27017")) {
            MongoCollection<Document> coll = client.getDatabase("testDB").getCollection("orders");

            // Example pipeline: total sales per product for orders in 2025, sorted desc
            List<Bson> pipeline = Arrays.asList(
                Aggregates.match(Filters.gte("orderDate", "2025-01-01")),
                Aggregates.unwind("$items"),
                Aggregates.group("$items.productId",
                        Accumulators.sum("totalQuantity", "$items.quantity"),
                        Accumulators.sum("totalRevenue", new Document("$multiply", Arrays.asList("$items.quantity", "$items.price")))),
                Aggregates.project(Projections.fields(
                        Projections.excludeId(),
                        Projections.computed("productId", "$_id"),
                        Projections.include("totalQuantity", "totalRevenue"))),
                Aggregates.sort(Sorts.descending("totalRevenue"))
            );

            AggregateIterable<Document> out = coll.aggregate(pipeline);
            for (Document d : out) System.out.println(d.toJson());
        }
    } 
}
