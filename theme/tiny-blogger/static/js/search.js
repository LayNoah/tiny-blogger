// Client-side keyword search over search.json (replaces tiny-blogger's server-side ?q= search).
(function () {
  var results = document.getElementById('search-results');
  var header = document.getElementById('search-header');
  var empty = document.getElementById('search-empty');
  var queryLabel = document.getElementById('search-query');
  var input = document.getElementById('search-input');

  var params = new URLSearchParams(window.location.search);
  var q = (params.get('q') || '').trim();
  if (input) { input.value = q; }
  if (!q) { empty.hidden = false; empty.textContent = 'Type a keyword in the search box above.'; return; }

  queryLabel.textContent = q;
  header.hidden = false;

  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  fetch(results.dataset.index)
    .then(function (r) { return r.json(); })
    .then(function (posts) {
      var needle = q.toLowerCase();
      var hits = posts.filter(function (p) {
        return (p.title + ' ' + p.text).toLowerCase().indexOf(needle) !== -1;
      });
      if (!hits.length) { empty.hidden = false; return; }
      results.innerHTML = hits.map(function (p, i) {
        return (i ? '<hr>' : '') +
          '<article class="post"><header>' +
          '<h2><a href="' + p.url + '">' + escapeHtml(p.title) + '</a></h2>' +
          '<div class="text-muted">' + p.date + '&nbsp;&nbsp;·&nbsp;&nbsp;' +
          '<a class="text-muted" href="' + p.category_url + '">' + escapeHtml(p.category) + '</a></div>' +
          '</header><p class="body">' + escapeHtml(p.summary) + '</p></article>';
      }).join('');
    })
    .catch(function () { empty.hidden = false; empty.textContent = 'Search index could not be loaded.'; });
})();
