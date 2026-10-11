(function () {
  const guideLists = document.querySelectorAll("[data-guide-list]");

  guideLists.forEach(function (guideList) {
    const overflow = guideList.querySelector("[data-guide-overflow]");
    const actions = guideList.querySelector("[data-guide-actions]");
    const toggle = guideList.querySelector("[data-guide-toggle]");

    if (!overflow || !actions || !toggle) return;

    const label = toggle.querySelector("[data-guide-toggle-label]");
    const icon = toggle.querySelector(".guide-list-toggle-icon");
    const collapsedLabel = toggle.dataset.collapsedLabel;
    const expandedLabel = toggle.dataset.expandedLabel;

    function setExpanded(expanded) {
      overflow.hidden = !expanded;
      toggle.setAttribute("aria-expanded", String(expanded));
      if (label) label.textContent = expanded ? expandedLabel : collapsedLabel;
      if (icon) icon.textContent = expanded ? "−" : "+";
    }

    setExpanded(false);
    actions.hidden = false;

    toggle.addEventListener("click", function () {
      setExpanded(toggle.getAttribute("aria-expanded") !== "true");
    });
  });
})();
