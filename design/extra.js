/* ---------- new layout: header button + section highlighting in the top bar ---------- */
(function () {
  var top = document.getElementById('reviewTop');
  if (top) top.addEventListener('click', review);
  var links = [].slice.call(document.querySelectorAll('#nav a'));
  if (!links.length || !('IntersectionObserver' in window)) return;
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      links.forEach(function (a) { a.classList.remove('on'); });
      var a = byId[en.target.id]; if (a) a.classList.add('on');
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  Object.keys(byId).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
})();
