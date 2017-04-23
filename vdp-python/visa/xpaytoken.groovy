import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
def hmac(String secretKey, String data) {
 Mac mac = Mac.getInstance("HmacSHA256")
 SecretKeySpec secretKeySpec = new SecretKeySpec(secretKey.getBytes(), "HmacSHA256")
 mac.init(secretKeySpec)
 byte[] digest = mac.doFinal(data.getBytes())
 return digest
}
// curl -X POST https://sandbox.api.visa.com/cybersource/payments/flex/v1/keys?apikey=BJOLWDT93I9FM7FR42J021IscXwwro9qYfdDACi3jWqtoiqo8 -d '{"encryptionType": "RsaOaep256"}' -H 'content-type: application/json' -H 'x-pay-token: xv2:1492876914:f17663778f08145eb544eae20a5cdf71e91952500ccb883d20a4190f628140cd'
def URI = "payments/flex/v1/keys"
def APIKey = "BJOLWDT93I9FM7FR42J021IscXwwro9qYfdDACi3jWqtoiqo8"
def sharedSecret = "jvbDcSN6XzDzqairDq2-{YWvi7lKyOFtQMx+}hRQ"
def QS = "apikey="+APIKey
def timeStampUTC = String.valueOf(System.currentTimeMillis().intdiv(1000L))
def payload = "{\"encryptionType\": \"RsaOaep256\"}"
def HMACDigest = hmac(sharedSecret, timeStampUTC + URI + QS + payload)
def encodedDigest = HMACDigest.encodeHex().toString()
def XPayToken = "xv2:"+ timeStampUTC + ":" + encodedDigest
print XPayToken
