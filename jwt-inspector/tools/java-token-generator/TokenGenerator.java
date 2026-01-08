import java.util.Base64;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class TokenGenerator {
    public static void main(String[] args) throws Exception {
        String header = Base64.getUrlEncoder()
            .withoutPadding()
            .encodeToString("{\"alg\":\"HS256\",\"typ\":\"JWT\"}".getBytes());

        String payload = Base64.getUrlEncoder()
            .withoutPadding()
            .encodeToString("{\"user\":\"demo\",\"exp\":9999999999}".getBytes());

        String secret = "weaksecret";
        String signingInput = header + "." + payload;

        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(secret.getBytes(), "HmacSHA256"));
        byte[] sig = mac.doFinal(signingInput.getBytes());

        String signature = Base64.getUrlEncoder()
            .withoutPadding()
            .encodeToString(sig);

        System.out.println(signingInput + "." + signature);
    }
}
