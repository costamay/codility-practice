function solution(skills) {
    // Implement your solution here
    let ar = [...skills];
    let t = {};
    let r = 1;
    while (true) {
      if (ar.length === 0 || ar.length === 1) {
        let solAr = [];
        for (let s of skills) {
          solAr.push(t[s] ? t[s] : r - 1);
        }
        return solAr;
      }
      let s = completeRound(ar, r, t);
      ar = s.a;
      r++;
    }
  }
  function completeRound(skills, round = 1, t = {}) {
    let newArr = [];
    //console.log(skills);
    for (let i = 1; i < skills.length; i = i + 2) {
      let player1 = skills[i - 1];
      let player2 = skills[i];
      ////console.log(player1, player2);
      if (player1 === undefined || player2 === undefined) {
        newArr.push(player1 ? player1 : player2);
        t[player1 ? player1 : player2] = round;
        continue;
      }
      if (player1 > player2) {
        newArr.push(player1);
        t[player2] = round;
        continue;
      }
      t[player1] = round;
      newArr.push(player2);
    }
    return { a: newArr, t };
  }
  let A = [4, 2, 7, 3, 1, 8, 6, 5];
  console.log(solution(A));