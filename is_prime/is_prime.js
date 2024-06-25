isPrime(2); // -> true
isPrime(3); // -> true
isPrime(4); // -> false
isPrime(5); // -> true
isPrime(6); // -> false
isPrime(7); // -> true
isPrime(8); // -> false
isPrime(25); // -> false
isPrime(31); // -> true
isPrime(2017); // -> true
isPrime(2048); // -> false
isPrime(1); // -> false
isPrime(713); // -> false
const isPrime = (n) => {
  if(n === 1) return false;
  for(i=2;i < n; i++){
    if(n%i!==0){
      continue
    }
    else{
      return false
    }
    }
  return true
};


module.exports = {
  isPrime,
};

