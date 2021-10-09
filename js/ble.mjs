// Read the battery level of the first found peripheral exposing the Battery Level characteristic

import noble from "@abandonware/noble";

noble.on("discover", console.log(peripheral));
