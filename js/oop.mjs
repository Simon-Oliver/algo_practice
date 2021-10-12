class TempSensor {
  get = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve(Math.random() * 10);
      }, 900);
    });
  };
}

const sense1 = new TempSensor();

setInterval(async () => {
  let temp = await sense1.get();
  console.log(temp);
}, 100);
