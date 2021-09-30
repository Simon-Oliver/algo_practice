const num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17];

const search = (arr, target, start = 0, end = arr.length - 1) => {
  const mid = Math.floor((start + end) / 2);
  if (arr[mid] === target) {
    // if the mid point is the same as the target, we return the index.
    return mid;
  } else if (start >= end) {
    // if the start point is larger (shouldn't happen?) or the same as end point,
    // we were unable to find the taret.
    return -1;
  } else if (target < arr[mid]) {
    // if the target is smaller than the middle, we want to search the left half of the array.
    // we call search again but shift the mid point to the left one step. Start point stays the same.

    return search(arr, target, start, mid - 1);
  } else if (target > arr[mid]) {
    // if the target is larger than the mid point, we want to search to the right half of the array.
    // we call search again but shift the start point to the right by one. End point stays the same.
    return search(arr, target, mid + 1, end);
  }
  // return target < arr[mid] ? search(arr, target, start, mid - 1):search(arr, target, mid + 1, end);
};

console.log(search(num, 5));
