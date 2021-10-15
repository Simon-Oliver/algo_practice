class TempSensor {
  get = async (delay = 1000) => {
    const delayPromise = (ms) => new Promise((res) => setTimeout(res, ms));
    await delayPromise(delay);

    return Math.random() * 10;
  };
}

const sense1 = new TempSensor();

let temp = await sense1.get();
console.log(temp);
