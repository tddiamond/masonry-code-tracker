// "Ask the code" query panel — calls /api/query and renders results inline.
document.addEventListener("DOMContentLoaded", function () {
  const queryBtn = document.getElementById("query-btn");
  const queryInput = document.getElementById("query-input");
  const queryResults = document.getElementById("query-results");
  if (!queryBtn || !queryInput || !queryResults) return;

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  function runQuery() {
    const q = queryInput.value.trim();
    if (!q) return;
    queryResults.classList.remove("hidden-field");
    queryResults.innerHTML = '<div class="query-loading">Searching proposal records…</div>';
    queryResults.scrollIntoView({ behavior: "smooth", block: "start" });

    fetch("/api/query?q=" + encodeURIComponent(q))
      .then(function (r) { return r.json(); })
      .then(function (data) {
        let html = '<div class="query-answer">' +
          '<span class="query-answer-label">Answer</span>' +
          '<strong>' + escapeHtml(data.interpretation) + '</strong>' +
          '<button type="button" class="query-close" id="query-close">&times;</button>' +
          '</div>';
        if (data.results.length) {
          html += '<div class="query-result-list">';
          data.results.forEach(function (r) {
            html += '<a href="' + r.url + '" class="query-result-card status-' + r.status + '">' +
              '<span class="status-pill status-' + r.status + '">' + r.status.replace("_", " ") + '</span>' +
              '<span class="query-result-title">' + escapeHtml(r.title) + '</span>' +
              '<span class="query-result-meta">§ ' + escapeHtml(r.code_section || "—") +
              ' &middot; Filed ' + escapeHtml(r.date_submitted || "—") +
              (r.date_decided ? ' &middot; Decided ' + escapeHtml(r.date_decided) : '') +
              '</span></a>';
          });
          html += '</div>';
        } else {
          html += '<div class="query-empty">No matching proposals found.</div>';
        }
        queryResults.innerHTML = html;
        const closeBtn = document.getElementById("query-close");
        if (closeBtn) {
          closeBtn.addEventListener("click", function () {
            queryResults.classList.add("hidden-field");
            queryResults.innerHTML = "";
          });
        }
      })
      .catch(function () {
        queryResults.innerHTML = '<div class="query-empty">Something went wrong running that query.</div>';
      });
  }

  queryBtn.addEventListener("click", runQuery);
  queryInput.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      runQuery();
    }
  });

  const sectionSelect = document.getElementById("code-section-select");
  const customSectionInput = document.getElementById("custom-section-input");
  if (sectionSelect && customSectionInput) {
    sectionSelect.addEventListener("change", function () {
      customSectionInput.classList.toggle("hidden-field", sectionSelect.value !== "__other__");
    });
  }
});

// Sidebar filter tabs: "Full code" / "Accepted" / "Under review".
// Dims non-matching entries in the TOC and in the main content, and
// jumps to the first matching section when a filter is selected.
document.addEventListener("DOMContentLoaded", function () {
  const filterButtons = document.querySelectorAll(".toc-filter");
  if (!filterButtons.length) return;

  function applyFilter(filter) {
    filterButtons.forEach(function (btn) {
      btn.classList.toggle("active", btn.dataset.filter === filter);
    });

    const attr = filter === "acc" ? "hasAcc" : filter === "rev" ? "hasRev" : null;

    // Sidebar section links
    document.querySelectorAll(".toc-section-link").forEach(function (el) {
      const match = !attr || el.dataset[attr] === "true";
      el.classList.toggle("toc-dimmed", !match);
    });

    // Sidebar chapter headers — dim only if none of their sections match
    document.querySelectorAll(".toc-chapter").forEach(function (el) {
      const match = !attr || el.dataset[attr] === "true";
      el.classList.toggle("toc-dimmed", !match);
    });

    // Main content sections
    let firstMatch = null;
    document.querySelectorAll(".code-section").forEach(function (el) {
      const match = !attr || el.dataset[attr] === "true";
      el.classList.toggle("toc-dimmed", !match);
      if (match && !firstMatch && attr) firstMatch = el;
    });

    if (firstMatch) {
      firstMatch.scrollIntoView({ behavior: "smooth", block: "center" });
      firstMatch.classList.add("flash-target");
      setTimeout(function () { firstMatch.classList.remove("flash-target"); }, 1600);
    }
  }

  filterButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      applyFilter(btn.dataset.filter);
    });
  });
});

// Smooth-scroll to in-page anchors and briefly flash the target section
// so it's obvious where you landed when jumping from a proposal detail page.
document.addEventListener("DOMContentLoaded", function () {
  if (window.location.hash) {
    const target = document.querySelector(window.location.hash);
    if (target) {
      setTimeout(function () {
        target.scrollIntoView({ behavior: "smooth", block: "center" });
        target.classList.add("flash-target");
        setTimeout(function () {
          target.classList.remove("flash-target");
        }, 1600);
      }, 80);
    }
  }

  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener("click", function (e) {
      const id = link.getAttribute("href").slice(1);
      const el = document.getElementById(id);
      if (el) {
        e.preventDefault();
        el.scrollIntoView({ behavior: "smooth", block: "center" });
        history.pushState(null, "", "#" + id);
      }
    });
  });
});
