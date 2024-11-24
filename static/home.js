document.addEventListener("DOMContentLoaded", function() {
  let currentSlide = 0;

  function showSlide(index) {
    const slides = document.querySelector(".slides");
    const totalSlides = slides.children.length;

    if (index >= totalSlides) {
      currentSlide = 0;
    } else if (index < 0) {
      currentSlide = totalSlides - 1;
    } else {
      currentSlide = index;
    }

    slides.style.transform = `translateX(-${currentSlide * 100}%)`;
  }

  function nextSlide() {
    showSlide(currentSlide + 1);
  }

  function prevSlide() {
    showSlide(currentSlide - 1);
  }

  setInterval(() => {
    nextSlide();
  }, 5000);

  showSlide(currentSlide);

  const nextArrow = document.querySelector(".rightArrowStyle");
  const prevArrow = document.querySelector(".leftArrowStyle");

  if (nextArrow) {
    nextArrow.addEventListener("click", nextSlide);
  }

  if (prevArrow) {
    prevArrow.addEventListener("click", prevSlide);
  }
});
