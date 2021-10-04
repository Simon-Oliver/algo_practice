import Controller from "node-pid-controller";
import { PIDController } from "@mariusrumpf/pid-controller";
import asciichart from "asciichart";

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
    // console.log("Heater strength ------", this.strength);
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
    this.obj.temp = this.obj.temp - 0.03;
    // console.log("Env diff ------", this.diff);
  };
}

class Sim {
  constructor(interval, length, func, stopFunc = false) {
    this.interval_id;
    this.interval = interval;
    this.func = func;
    this.isRunning = true;
    this.startTime = Date.now();
    this.length = length;
    this.stopFunc = stopFunc;
  }
  Start = () => {
    console.log("Future", this.startTime + this.length);
    console.log("Now", Date.now());
    this.interval_id = setInterval(() => {
      if (this.startTime + this.length > Date.now()) {
        this.func();
      } else {
        this.Stop();
      }
    }, this.interval);
  };

  Stop = () => {
    if (this.stopFunc) {
      this.stopFunc();
    }
    clearInterval(this.interval_id);
    console.log("Stopped");
  };
}

const tank = new Tank(5, 31);
const tankHeater = new Heater(tank, 2);
const env = new Env(tank, 5);
const ctr = new Controller({
  k_p: 0.25,
  k_i: 0.01,
  k_d: 0.01,
  dt: 1,
});

const controller = new PIDController({
  p: 10000,
  i: 50,
  d: 30,
  target: 32,
  sampleTime: 1000, // in ms
  outputMin: 0,
  //outputMax: 255,
  outputMax: 10000,
});

ctr.setTarget(500);

// //Specify the links and initial tuning parameters
// PID myPID(&Input, &Output, &Setpoint,2,5,1, DIRECT);

// int WindowSize = 5000;
// unsigned long windowStartTime;
// void setup()
// {
//   windowStartTime = millis();

//   //initialize the variables we're linked to
//   Setpoint = 100;

//   //tell the PID to range between 0 and the full window size
//   myPID.SetOutputLimits(0, WindowSize);

//   //turn the PID on
//   myPID.SetMode(AUTOMATIC);
// }

// void loop()
// {
//   Input = analogRead(0);
//   myPID.Compute();

//   /************************************************
//    * turn the output pin on/off based on pid output
//    ************************************************/
//   if(millis() - windowStartTime>WindowSize)
//   { //time to shift the Relay Window
//     windowStartTime += WindowSize;
//   }
//   if(Output < millis() - windowStartTime) digitalWrite(RelayPin,HIGH);
//   else digitalWrite(RelayPin,LOW);

// }
let windowStartTime = Date.now();
let count = 0;
let on = false;
const windowSize = 10000;
let temps = [];
var config = {
  offset: 3, // axis offset from the left (min 2)
  padding: "       ", // padding string for label formatting (can be overrided)
  height: 20, // any height you want
};

const stop = () => {
  console.log("Relay count is ", count);
};

const log = () => {
  let output = tank.temp; //this can be a function you use to get temperature from a hardware sensor or API
  // let input = ctr.update(output);
  if (temps.length < 100) {
    temps.push(output);
  } else {
    temps.shift();
    temps.push(output);
  }
  console.log(asciichart.plot(temps, config), "\r");

  let input = controller.update(output);

  if (Date.now() - windowStartTime > windowSize) {
    //time to shift the Relay Window
    windowStartTime += windowSize;
  }
  if (input < Date.now() - windowStartTime) {
    // console.log("input", input);
    env.Effect();
    console.log(input);

    if (on) {
      on = false;
      count++;
    }
    console.log("Heater on: ", on);
    // console.log("Temp", tank.temp);
    // console.log("digitalWrite(RelayPin,LOW)");

    // console.log("If date ", Date.now() - windowStartTime);
  } else {
    tankHeater.strength = 0.05;
    console.log(input);
    tankHeater.On();
    if (!on) {
      on = true;
      count++;
    }
    env.Effect();
    console.log("Heater on: ", on);
    // console.log("input", input);
    // console.log("After Heater", tank.temp);
    // console.log("digitalWrite(RelayPin,HIGH)");
  }

  // let input = controller.update(output);
  // tankHeater.strength = input;
  // console.log("Before", tank.temp);
  // tankHeater.On();
  // console.log("After Heater", tank.temp);
  // env.Effect();
  // console.log("After ENv", tank.temp);
  // console.log("Time ---- ", timeNow);
};

const sim = new Sim(1000, 600000, log, stop);
sim.Start();
