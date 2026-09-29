(function () {
  const article = document.querySelector("[data-article-content]");
  const toc = document.getElementById("table-of-contents");
  if (!article || !toc) return;

  const headings = Array.from(article.querySelectorAll("h2, h3"));
  if (headings.length < 2) {
    const panel = toc.closest(".toc-panel");
    if (panel) panel.hidden = true;
    return;
  }

  const list = document.createElement("ol");
  headings.forEach(function (heading, index) {
    if (!heading.id) {
      const slug = heading.textContent
        .toLowerCase()
        .trim()
        .replace(/[^a-z0-9\s-]/g, "")
        .replace(/\s+/g, "-")
        .replace(/-+/g, "-");
      heading.id = slug || "section-" + (index + 1);
    }
    const item = document.createElement("li");
    if (heading.tagName === "H3") item.className = "toc-subitem";
    const link = document.createElement("a");
    link.href = "#" + heading.id;
    link.textContent = heading.textContent;
    item.appendChild(link);
    list.appendChild(item);
  });
  toc.appendChild(list);
})();

