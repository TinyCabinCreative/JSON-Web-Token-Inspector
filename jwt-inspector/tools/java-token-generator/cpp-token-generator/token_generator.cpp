#include <iostream>
#include <openssl/hmac.h>
#include <openssl/evp.h>

int main()
{
    std::string header = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9";
    std::string payload = "eyJ1c2VyIjoiZGVtbyJ9";
    std::string secret = "weaksecret";

    std::string input = header + "." + payload;
    unsigned char result[EVP_MAX_MD_SIZE];
    unsigned int len;

    HMAC(EVP_sha256(), secret.c_str(), secret.size(),
         (unsigned char *)input.c_str(), input.size(),
         result, &len);

    std::cout << input << ".[signature]" << std::endl;
}
