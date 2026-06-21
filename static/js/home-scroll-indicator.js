(() => {
  const indicator = document.getElementById("scrollIndicator");
  const cards = document.getElementById("home-cards");
  if (!indicator || !cards) return;

  let hidden = false;

  const hideIndicator = () => {
    if (hidden) return;
    hidden = true;
    indicator.classList.add("is-hidden");
    setTimeout(() => indicator.remove(), 260);
    window.removeEventListener("scroll", onScroll);
    window.removeEventListener("wheel", hideIndicator);
    window.removeEventListener("touchmove", hideIndicator);
    window.removeEventListener("keydown", hideIndicator);
  };

  const onScroll = () => {
    if (window.scrollY > 12) hideIndicator();
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("wheel", hideIndicator, {
    passive: true,
    once: true,
  });
  window.addEventListener("touchmove", hideIndicator, {
    passive: true,
    once: true,
  });
  window.addEventListener("keydown", hideIndicator, { once: true });

  indicator.addEventListener("click", (e) => {
    e.preventDefault();

    const navbarOffset = 56; // fixed navbar height
    const y = cards.getBoundingClientRect().top + window.scrollY - navbarOffset;

    window.scrollTo({ top: y, behavior: "smooth" });
    hideIndicator();
  });
})();
