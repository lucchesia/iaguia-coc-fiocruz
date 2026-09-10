// Buscador por facetas de docs/encontrar.md. Carregado como <script type="module">,
// então import.meta.url aponta para este arquivo — usado para resolver o caminho do
// JSON de dados independentemente de onde o site for publicado (raiz ou subpasta).
//
// Assume que encontrar.md fica exatamente um nível abaixo da raiz do site
// (site/encontrar/index.html), igual a qualquer verbete — por isso os links dos
// resultados usam um prefixo "../" para voltar à raiz antes de entrar em
// ferramentas/<slug>/ ou conceitos/<slug>/.

const mount = document.getElementById("facet-finder");

if (mount) {
  init();
}

async function init() {
  const dataUrl = new URL("../assets/data/entries.json", import.meta.url);
  let entries = [];
  try {
    const response = await fetch(dataUrl);
    entries = await response.json();
  } catch (err) {
    mount.innerHTML = "<p>Não foi possível carregar os dados do glossário.</p>";
    return;
  }

  mount.innerHTML = layout();
  populateOptions(entries);
  mount.addEventListener("change", () => renderResults(entries));
  mount
    .querySelector(".facet-finder__reset")
    .addEventListener("click", () => resetAndRender(entries));

  renderResults(entries);
}

function layout() {
  return `
    <div class="facet-finder">
      <div class="facet-finder__filters">
        <fieldset class="facet-finder__group" data-group="types">
          <legend>Tipo de resultado</legend>
          <label><input type="checkbox" value="ferramenta" checked> Ferramentas</label>
          <label><input type="checkbox" value="conceito" checked> Conceitos e termos</label>
        </fieldset>

        <fieldset class="facet-finder__group">
          <legend>Categoria</legend>
          <div class="facet-finder__options facet-finder__options--scroll" data-options="categories"></div>
        </fieldset>

        <fieldset class="facet-finder__group">
          <legend>Temas (tags)</legend>
          <div class="facet-finder__options facet-finder__options--scroll" data-options="tags"></div>
        </fieldset>

        <fieldset class="facet-finder__group">
          <legend>Custo <span class="facet-finder__hint">(só ferramentas)</span></legend>
          <div class="facet-finder__options" data-options="access"></div>
        </fieldset>

        <fieldset class="facet-finder__group">
          <legend>Abertura <span class="facet-finder__hint">(só ferramentas)</span></legend>
          <div class="facet-finder__options" data-options="openness"></div>
        </fieldset>

        <button type="button" class="facet-finder__reset md-button">Limpar filtros</button>
      </div>

      <div class="facet-finder__results" data-results></div>
    </div>
  `;
}

function populateOptions(entries) {
  fillGroup("categories", uniqueSorted(entries.map((e) => e.category)));
  fillGroup("tags", uniqueSorted(entries.flatMap((e) => e.tags || [])));
  // uniqueSorted descarta valor ausente, então os conceitos, que não têm nenhum dos
  // dois campos, não geram opção "sem valor" e saem do resultado quando o filtro é usado.
  fillGroup("access", uniqueSorted(entries.map((e) => e.access_model)));
  fillGroup("openness", uniqueSorted(entries.map((e) => e.source_model)));
}

function fillGroup(name, values) {
  const container = mount.querySelector(`[data-options="${name}"]`);
  container.innerHTML = values
    .map(
      (v) =>
        `<label><input type="checkbox" value="${escapeHtml(v)}"> ${escapeHtml(v)}</label>`
    )
    .join("");
}

function resetAndRender(entries) {
  mount.querySelectorAll('input[type="checkbox"]').forEach((el) => {
    el.checked = Boolean(el.closest('[data-group="types"]'));
  });
  renderResults(entries);
}

function renderResults(entries) {
  const types = checkedValues('[data-group="types"] input');
  const categories = checkedValues('[data-options="categories"] input');
  const tags = checkedValues('[data-options="tags"] input');
  const access = checkedValues('[data-options="access"] input');
  const openness = checkedValues('[data-options="openness"] input');

  const filtered = entries.filter((e) => {
    if (types.length && !types.includes(e.entry_type)) return false;
    if (categories.length && !categories.includes(e.category)) return false;
    if (tags.length && !(e.tags || []).some((t) => tags.includes(t))) return false;
    if (access.length && !access.includes(e.access_model)) return false;
    if (openness.length && !openness.includes(e.source_model)) return false;
    return true;
  });

  const results = mount.querySelector("[data-results]");
  if (!filtered.length) {
    results.innerHTML =
      '<p class="facet-finder__empty">Nenhum resultado com esses filtros — tente remover algum.</p>';
    return;
  }

  results.innerHTML =
    `<p class="facet-finder__count">${filtered.length} resultado(s)</p>` +
    '<ul class="facet-finder__cards">' +
    filtered.map(cardHtml).join("") +
    "</ul>";
}

function cardHtml(entry) {
  const label = entry.entry_type === "ferramenta" ? "Ferramenta" : "Conceito";
  const excerpt = entry.excerpt
    ? `<p class="facet-finder__excerpt">${escapeHtml(entry.excerpt)}</p>`
    : "";
  return `
    <li class="facet-finder__card">
      <span class="facet-finder__badge facet-finder__badge--${entry.entry_type}">${label}</span>
      <a href="../${entry.url}"><strong>${escapeHtml(entry.title)}</strong></a>
      <div class="facet-finder__meta">${escapeHtml(entry.category || "")}</div>
      ${excerpt}
    </li>`;
}

function checkedValues(selector) {
  return Array.from(mount.querySelectorAll(selector))
    .filter((el) => el.checked)
    .map((el) => el.value);
}

function uniqueSorted(list) {
  return Array.from(new Set(list.filter(Boolean))).sort((a, b) =>
    a.localeCompare(b, "pt-BR")
  );
}

function escapeHtml(value) {
  return String(value).replace(
    /[&<>"']/g,
    (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
  );
}
