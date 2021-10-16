function nbMonths(
  startPriceOld,
  startPriceNew,
  savingperMonth,
  percentLossByMonth
) {
  let currentPriceOld = startPriceOld * ((100 - percentLossByMonth) / 100);
  let currentPriceNew = startPriceNew * ((100 - percentLossByMonth) / 100);
  let currentPercentLoss = percentLossByMonth;
  let savings = savingperMonth;
  let month = 1;

  if (startPriceNew - startPriceOld <= 0) {
    return [0, startPriceOld - startPriceNew];
  }

  while (currentPriceNew - currentPriceOld - savings >= 0) {
    if (month != 0 && month % 2 > 0) {
      currentPercentLoss += 0.5;
    }
    savings += savingperMonth;
    currentPriceOld = currentPriceOld * ((100 - currentPercentLoss) / 100);
    currentPriceNew = currentPriceNew * ((100 - currentPercentLoss) / 100);
    month++;
  }
  const leftOver = Math.round(savings + currentPriceOld - currentPriceNew);
  return [month, leftOver];
}

console.log(nbMonths(2000, 8000, 1000, 1.5));
console.log(nbMonths(8000, 8000, 1000, 1.5));
console.log(nbMonths(12000, 8000, 1000, 1.5));
