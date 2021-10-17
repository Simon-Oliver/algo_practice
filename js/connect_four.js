const arrTo2D = (arr) => {
  let board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
  ];
  const indexes = { A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6 };
  arr.forEach((element) => {
    const splitStr = element.split("_");
    const index = indexes[splitStr[0]];
    const player = splitStr[1][0];
    for (let i = board.length - 1; i >= 0; i--) {
      if (board[i][index] === 0) {
        board[i][index] = player;
        break;
      }
    }
  });

  let display = "";
  board.forEach((e) => (display += String(e) + "\n"));
  console.log(display);
  return board;
};

const checkWin = (board) =>{
    const direction
}

const yellowWins = [
  "C_Yellow",
  "E_Red",
  "G_Yellow",
  "B_Red",
  "D_Yellow",
  "B_Red",
  "B_Yellow",
  "G_Red",
  "C_Yellow",
  "C_Red",
  "D_Yellow",
  "F_Red",
  "E_Yellow",
  "A_Red",
  "A_Yellow",
  "G_Red",
  "A_Yellow",
  "F_Red",
  "F_Yellow",
  "D_Red",
  "B_Yellow",
  "E_Red",
  "D_Yellow",
  "A_Red",
  "G_Yellow",
  "D_Red",
  "D_Yellow",
  "C_Red",
];

arrTo2D(yellowWins);
