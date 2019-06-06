## haproxy-auth

sample setup to test haproxy authorizations

Uses lua to make a request to an authorization api to return user entitlements, which can then be forwarded via headers to the destination backend app (in this case, the same app)