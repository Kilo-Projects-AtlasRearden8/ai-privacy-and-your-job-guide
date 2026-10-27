// Asdale Dynamics, LLC — AI Privacy at Work site script
document.addEventListener('DOMContentLoaded', function () {
  // Highlight the current page in the nav
  const current = location.pathname.split('/').pop() || 'index.html';
  const links = document.querySelectorAll('.nav-inner a');
  links.forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === current) {
      link.classList.add('active');
    }
    if (current === 'index.html' && href === 'index.html') {
      link.classList.add('active');
    }
  });

  // Print-friendly checklist formatting
  const printBtn = document.getElementById('print-checklist');
  if (printBtn) {
    printBtn.addEventListener('click', function () {
      window.print();
    });
  }
});
