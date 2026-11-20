// Mobile menu
const toggle = document.querySelector(".nav-toggle");
const links = document.getElementById("nav-links");
if (toggle && links) {
  toggle.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
  links.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      links.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    })
  );
}

// Footer year
const year = document.getElementById("year");
if (year) year.textContent = new Date().getFullYear();

// Quote form -> emailed to LogoPack via FormSubmit (falls back to the visitor's email app)
const QUOTE_EMAIL = "logopackca@gmail.com";
const FORM_ENDPOINT = `https://formsubmit.co/ajax/${QUOTE_EMAIL}`;
const quoteForm = document.getElementById("quote-form");
if (quoteForm) quoteForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const d = new FormData(quoteForm);
  if (d.get("_honey")) return; // bot
  const status = quoteForm.querySelector(".form-status");
  const button = quoteForm.querySelector('button[type="submit"]');
  const products = d.getAll("products").join(", ") || "Not specified";
  const subject = `Quote request: ${d.get("business")} – ${products}`;
  const payload = {
    Name: d.get("name"),
    Business: d.get("business"),
    Email: d.get("email"),
    Phone: d.get("phone") || "-",
    Products: products,
    Quantity: d.get("quantity") || "-",
    Timeline: d.get("timeline"),
    Details: d.get("details") || "-",
    email: d.get("email"),
    _replyto: d.get("email"),
    _subject: subject,
    _template: "table",
  };

  button.disabled = true;
  const label = button.textContent;
  button.textContent = "Sending…";
  status.textContent = "";
  try {
    const res = await fetch(FORM_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(payload),
    });
    const out = await res.json().catch(() => ({}));
    if (!res.ok || String(out.success) === "false") throw new Error(out.message || res.status);
    quoteForm.reset();
    status.className = "form-status full ok";
    status.textContent = "Thanks! Your request was sent. We'll reply with a quote soon. You can email your logo to " + QUOTE_EMAIL + ".";
  } catch (err) {
    status.className = "form-status full err";
    status.innerHTML = `Sorry, that didn't go through. Please email us at <a href="mailto:${QUOTE_EMAIL}">${QUOTE_EMAIL}</a>.`;
    const body = Object.entries(payload).filter(([k]) => !k.startsWith("_") && k !== "email").map(([k, v]) => `${k}: ${v}`).join("\n");
    window.location.href = `mailto:${QUOTE_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  } finally {
    button.disabled = false;
    button.textContent = label;
  }
});
