function solution(R, V) {
    let balanceA = 0;
    let balanceB = 0;
  
    for (let i = 0; i < R.length; i++) {
      if (R[i] === "A") {
        balanceA += V[i];
      } else {
        balanceB += V[i];
      }
  
      if (balanceA < 0 && balanceB < 0) {
        // If both banks go into debt, adjust the initial balances for both banks.
        const debt = Math.min(balanceA, balanceB);
        balanceA -= debt;
        balanceB -= debt;
      } else if (balanceA < 0) {
        // If bank A goes into debt, we need to adjust the initial balance for bank A.
        balanceB -= balanceA;
        balanceA = 0;
      } else if (balanceB < 0) {
        // If bank B goes into debt, we need to adjust the initial balance for bank B.
        balanceA -= balanceB;
        balanceB = 0;
      }
    }
  
    return [balanceA, balanceB];
}