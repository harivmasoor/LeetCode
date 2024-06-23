greet("alvin"); // -> 'hey alvin'
greet("jason"); // -> 'hey jason'
greet("how now brown cow"); // -> 'hey how now brown cow'
const greet = (s) => {
  return "hey " + s
};


module.exports = {
  greet,
};

