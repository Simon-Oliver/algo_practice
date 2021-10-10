// Read the battery level of the first found peripheral exposing the Battery Level characteristic
import noble from "@abandonware/noble";

noble.on("stateChange", function (state) {
  if (state === "poweredOn") {
    noble.startScanning();
  } else {
    noble.stopScanning();
  }
});

noble.on("discover", function (peripheral) {
  console.log(peripheral);
});
