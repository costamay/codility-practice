function solution(N) {
    // Implement your solution here
    let letters = "abcdefghijklmnopqrstuvwxyz";
    let me = "";
    let me2 = [];

    for(let i = 0; i <= N; i+=N){
        if(N > letters.length){
            let m = Math.floor(N / 15);
            let news = letters.split('').map(char => char.repeat(m)).join('');
            me2.push(news.slice(i, i+N));
            break;
        }else{
            me = (letters.slice(i, i + N));
        }
    }
    if(N > 26){
        console.log(me2.join("").length);
    return me2.join("");
    }else{
        return me;
    }
}
console.log(solution(30))