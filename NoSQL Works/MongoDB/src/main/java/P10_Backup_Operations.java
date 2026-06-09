import java.io.*;

public class P10_Backup_Operations {
    public static void main(String[] args) throws IOException, InterruptedException {
        // Example: run mongodump from Java (requires mongodump in PATH)
        ProcessBuilder dumpPb = new ProcessBuilder(
                "mongodump",
                "--uri=mongodb://localhost:27017/testDB",
                "--out=./backups/testDB-" + System.currentTimeMillis()
        );
        dumpPb.redirectErrorStream(true);
        Process dumpProc = dumpPb.start();
        try (BufferedReader r = new BufferedReader(new InputStreamReader(dumpProc.getInputStream()))) {
            String line;
            while ((line = r.readLine()) != null) System.out.println(line);
        }
        int dumpExit = dumpProc.waitFor();
        System.out.println("mongodump exit code: " + dumpExit);

        // Example: restore using mongorestore
        // ProcessBuilder restorePb = new ProcessBuilder("mongorestore", "--uri=mongodb://localhost:27017", "--dir=./backups/...");
        // ...
    }
}
