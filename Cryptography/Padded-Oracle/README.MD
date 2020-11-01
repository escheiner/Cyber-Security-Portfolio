Padded Oracle

Defeating a Padding Oracle can be as simple as implementing a Message
Authentication Codes, MAC, and not validating the padding at all, if the
verification on the MAC fails. Additionally, you can return generic error
messages that do not indicate the type of failure. 
