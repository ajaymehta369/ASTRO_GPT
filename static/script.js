var quotes = [
  "Just as the stars rise and set, so too do the seasons of life. Embrace the cycles, for they bring growth and renewal.",
  "The moon’s phases remind us: even in darkness, there is light waiting to emerge.",
  "Retrogrades encourage reflection. Pause, review, and find wisdom in the past before moving forward.",
  "Like the planets orbiting the sun, each journey is unique but guided by cosmic rhythm.",
  "The constellations tell stories across time. Trust that your story, too, is part of a greater cosmic design.",
  "Eclipses teach that transformation often begins when the familiar is temporarily obscured.",
  "As the sun remains constant, rise each day with unwavering purpose and illuminate those around you.",
  "Venus shines brightest when it guides us toward love and beauty. Let it inspire your heart.",
  "Mercury’s swift orbit reminds us to communicate clearly and adapt quickly to change.",
  "The cosmos is vast, yet each star has its purpose. Trust that you are exactly where you need to be."
];

const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
console.log(randomQuote);

const quoteElement = document.getElementById("quote");
quoteElement.textContent = randomQuote;

const loading = document.getElementById('loading');
const form = document.querySelector('form');

form.addEventListener('submit', () => {
  loading.style.display = 'block';
});

// Lottie animation setup for loading spinner
var animationContainer = document.getElementById('loading');
var animationDataUrl = 'https://assets10.lottiefiles.com/packages/lf20_poqmycwy.json';

var animData = {
  container: animationContainer,
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: animationDataUrl
};

var anim = bodymovin.loadAnimation(animData);

// Auto-resize textarea on input
const textarea = document.querySelector('textarea');
textarea.addEventListener('input', function() {
  this.style.height = 'auto';
  this.style.height = this.scrollHeight + 'px';
});

// Button animation function
var animateButton = function(e) {
  e.preventDefault;
  e.target.classList.remove('animate');
  e.target.classList.add('animate');
  setTimeout(function(){
    e.target.classList.remove('animate');
  }, 700);
};







