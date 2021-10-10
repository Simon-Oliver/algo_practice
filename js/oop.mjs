import fs from "fs";

class Logger {
  constructor(func) {
    this.func = func;
  }
  Log(path, data) {
    fs.writeFile(path, data, () => console.log("File Saved"));
    this.func();
  }
}

const log1 = new Logger(() => console.log("Saved"));

log1.Log(
  "./data.txt",
  JSON.stringify({ test: "Hello World", data1: "Hello World 2" })
);
