import Controller from "node-pid-controller";
import { PIDController } from "@mariusrumpf/pid-controller";

class Tank {
  constructor(size, temp) {
    this.size = size;
    this.temp = temp;
  }
}

class Heater {
  constructor(obj, strength) {
    this.obj = obj;
    this.strength = strength;
  }
  On = () => {
    this.obj.temp = this.obj.temp + this.strength;
    console.log("Heater strength ------", this.strength);
  };
}

class Env {
  constructor(obj, env_temp) {
    this.obj = obj;
    this.env_temp = env_temp;
    this.diff;
  }
  Effect = () => {
    this.diff = (this.env_temp - this.obj.temp) / 10;
    this.obj.temp = this.obj.temp + this.diff;
    console.log("Env diff ------", this.diff);
  };
}

class Sim {
  constructor(interval, func) {
    this.interval_id;
    this.interval = interval;
    this.func = func;
    this.isRunning = true;
  }
  Start = () => {
    this.interval_id = setInterval(() => {
      this.func();
    }, this.interval);
  };

  Stop = () => {
    clearInterval(this.interval_id);
    console.log("Stopped");
  };
}

const tank = new Tank(5, 10);
const tankHeater = new Heater(tank, 0);
const env = new Env(tank, 5);
const ctr = new Controller({
  k_p: 0.25,
  k_i: 0.01,
  k_d: 0.01,
  dt: 1,
});

const controller = new PIDController({
  p: 0.25,
  i: 0.025,
  d: 0.025,
  target: 250,
  sampleTime: 1000, // in ms
  outputMin: 0,
  outputMax: 255,
});

ctr.setTarget(500);

const log = () => {
  let output = tank.temp; //this can be a function you use to get temperature from a hardware sensor or API
  // let input = ctr.update(output);
  let input = controller.update(output);
  tankHeater.strength = input;
  console.log("Before", tank.temp);
  tankHeater.On();
  console.log("After Heater", tank.temp);
  env.Effect();
  console.log("After ENv", tank.temp);
};

const sim = new Sim(1000, log);
sim.Start();
